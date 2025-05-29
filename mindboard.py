import cv2
import mediapipe as mp
import numpy as np
import time
import string
import itertools
import pyttsx3
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Constants
FRAME_WIDTH, FRAME_HEIGHT = 640, 480
ZONES_X, ZONES_Y = 3, 3
ZONE_WIDTH, ZONE_HEIGHT = FRAME_WIDTH // ZONES_X, FRAME_HEIGHT // ZONES_Y
VIRTUAL_WIDTH, VIRTUAL_HEIGHT = 240, 160
X_OFFSET, Y_OFFSET = (FRAME_WIDTH - VIRTUAL_WIDTH) // 2, (FRAME_HEIGHT - VIRTUAL_HEIGHT) // 2
DEAD_ZONE_RADIUS = 30
DWELL_TIME_SECONDS = 1.5
COOLDOWN_SECONDS = 2.0
AUTO_HOVER_TIME = 1.5
PREDICTION_GRID_POSITIONS = [(2, 0), (2, 1), (2, 2)]

# Mediapipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)
NOSE_TIP_INDEX = 1
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]
EAR_THRESHOLD = 0.25
CONSEC_FRAMES = 3

# Text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)
def speak_text(text): engine.say(text); engine.runAndWait()

# Load GPT-2 model for prediction
tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')
model = GPT2LMHeadModel.from_pretrained('distilgpt2')
model.eval()

def predict_top3_words(prompt):
    prompt = prompt.strip()
    if not prompt or len(prompt) < 2:
        return []
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    with torch.no_grad():
        outputs = model.generate(
            input_ids,
            max_length=len(input_ids[0]) + 8,
            num_return_sequences=1,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.9,
            pad_token_id=tokenizer.eos_token_id
        )
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    next_part = result[len(prompt):].strip().split()
    return next_part[:3]

# Grid and letters
letters = list(string.ascii_uppercase)
letter_groups = [letters[i:i + 5] for i in range(0, 25, 5)]
letter_groups.append(letters[25:])
main_zones = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)]
main_grid_group_map = dict(zip(main_zones, letter_groups))
subgrid_positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)]
subgrid_layout_by_zone = {}
for zone, group_letters in main_grid_group_map.items():
    layout = {}
    for i, letter in enumerate(group_letters):
        layout[subgrid_positions[i]] = letter
    layout[(2, 0)] = "BACK"
    layout[(2, 1)] = "SPACE"
    layout[(2, 2)] = "SPEAK"
    subgrid_layout_by_zone[zone] = layout

# States
dwell_tracker = {"last_zone": None, "start_time": None, "confirmed": False}
sentence = ""
typed_characters = []
main_grid_active = True
selected_zone = None
current_subgrid = {}
last_selection_time = 0
blink_counter = 0
blink_total = 0
mode = "manual"
auto_zone_cycle = itertools.cycle([(i, j) for i in range(3) for j in range(3)])
auto_current_zone = next(auto_zone_cycle)
last_auto_time = time.time()

# Prediction state
prediction_words = []

def get_zone_from_nose(nose_x, nose_y):
    nose_px = int(nose_x * FRAME_WIDTH) - X_OFFSET
    nose_py = int(nose_y * FRAME_HEIGHT) - Y_OFFSET
    nose_px = max(0, min(nose_px, VIRTUAL_WIDTH - 1))
    nose_py = max(0, min(nose_py, VIRTUAL_HEIGHT - 1))
    col = nose_px * ZONES_X // VIRTUAL_WIDTH
    row = nose_py * ZONES_Y // VIRTUAL_HEIGHT
    return row, col

def update_dwell_tracker(current_zone, active):
    if not active or current_zone is None:
        dwell_tracker["last_zone"] = None
        dwell_tracker["start_time"] = None
        dwell_tracker["confirmed"] = False
        return None
    if dwell_tracker["last_zone"] != current_zone:
        dwell_tracker["last_zone"] = current_zone
        dwell_tracker["start_time"] = time.time()
        dwell_tracker["confirmed"] = False
        return None
    elapsed = time.time() - dwell_tracker["start_time"]
    if elapsed >= DWELL_TIME_SECONDS and not dwell_tracker["confirmed"]:
        dwell_tracker["confirmed"] = True
        return current_zone
    return None

def calculate_EAR(eye_landmarks):
    def euclidean(p1, p2): return np.linalg.norm(np.array(p1) - np.array(p2))
    hor = euclidean(eye_landmarks[0], eye_landmarks[3])
    ver1 = euclidean(eye_landmarks[1], eye_landmarks[5])
    ver2 = euclidean(eye_landmarks[2], eye_landmarks[4])
    return (ver1 + ver2) / (2.0 * hor)

def detect_blink(landmarks, w, h):
    global blink_counter, blink_total
    def coords(indices): return [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in indices]
    left_eye = coords(LEFT_EYE)
    right_eye = coords(RIGHT_EYE)
    left_EAR = calculate_EAR(left_eye)
    right_EAR = calculate_EAR(right_eye)
    avg_EAR = (left_EAR + right_EAR) / 2.0
    blink = False
    if avg_EAR < EAR_THRESHOLD:
        blink_counter += 1
    else:
        if blink_counter >= CONSEC_FRAMES:
            blink_total += 1
            blink = True
        blink_counter = 0
    return blink, avg_EAR

def highlight_current_zone(frame, zone, color=(0, 255, 255), thickness=4):
    if zone:
        r, c = zone
        x0, y0 = c * ZONE_WIDTH, r * ZONE_HEIGHT
        x1, y1 = x0 + ZONE_WIDTH, y0 + ZONE_HEIGHT
        cv2.rectangle(frame, (x0, y0), (x1, y1), color, thickness)

# Main loop
cap = cv2.VideoCapture(0)
cap.set(3, FRAME_WIDTH)
cap.set(4, FRAME_HEIGHT)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)
    h, w = frame.shape[:2]
    zone_chosen = False
    current_zone = None
    nose_px, nose_py = -1, -1

    if results.multi_face_landmarks:
        face = results.multi_face_landmarks[0]
        landmarks = face.landmark
        blink, ear = detect_blink(landmarks, w, h)

        if mode == "manual":
            nose_tip = landmarks[NOSE_TIP_INDEX]
            nose_px, nose_py = int(nose_tip.x * w), int(nose_tip.y * h)
            dist = np.linalg.norm([nose_px - FRAME_WIDTH//2, nose_py - FRAME_HEIGHT//2])
            if dist >= DEAD_ZONE_RADIUS:
                current_zone = get_zone_from_nose(nose_tip.x, nose_tip.y)
                highlight_current_zone(frame, current_zone)
                confirmed = update_dwell_tracker(current_zone, True)
                if confirmed and time.time() - last_selection_time > COOLDOWN_SECONDS:
                    zone_chosen = True
                    current_zone = confirmed
        else:
            if time.time() - last_auto_time >= AUTO_HOVER_TIME:
                auto_current_zone = next(auto_zone_cycle)
                last_auto_time = time.time()
            highlight_current_zone(frame, auto_current_zone, (255, 0, 255))
            if blink and time.time() - last_selection_time > COOLDOWN_SECONDS:
                zone_chosen = True
                current_zone = auto_current_zone

        if zone_chosen:
            if main_grid_active and current_zone in main_grid_group_map:
                selected_zone = current_zone
                current_subgrid = subgrid_layout_by_zone[selected_zone]
                main_grid_active = False
            elif not main_grid_active and current_zone in current_subgrid:
                item = current_subgrid[current_zone]
                if item == "BACK":
                    main_grid_active = True
                    selected_zone = None
                    current_subgrid = {}
                elif item == "SPACE":
                    sentence += " "
                    typed_characters.append(" ")
                elif item == "SPEAK":
                    speak_text(sentence)
                else:
                    sentence += item
                    typed_characters.append(item)
                    prediction_words = predict_top3_words(sentence)
            elif current_zone in PREDICTION_GRID_POSITIONS and prediction_words:
                idx = PREDICTION_GRID_POSITIONS.index(current_zone)
                if idx < len(prediction_words):
                    sentence += " " + prediction_words[idx]
                    prediction_words = []

            last_selection_time = time.time()
            dwell_tracker["confirmed"] = False

    if nose_px > 0 and nose_py > 0:
        cv2.circle(frame, (nose_px, nose_py), 6, (255, 0, 0), -1)

    for i in range(1, ZONES_X):
        cv2.line(frame, (i * ZONE_WIDTH, 0), (i * ZONE_WIDTH, FRAME_HEIGHT), (200, 200, 200), 1)
    for j in range(1, ZONES_Y):
        cv2.line(frame, (0, j * ZONE_HEIGHT), (FRAME_WIDTH, j * ZONE_HEIGHT), (200, 200, 200), 1)

    cv2.rectangle(frame, (X_OFFSET, Y_OFFSET), (X_OFFSET + VIRTUAL_WIDTH, Y_OFFSET + VIRTUAL_HEIGHT), (150, 150, 150), 2)
    cv2.circle(frame, (FRAME_WIDTH // 2, FRAME_HEIGHT // 2), DEAD_ZONE_RADIUS, (0, 0, 255), 1)

    if main_grid_active:
        for zone, letters in main_grid_group_map.items():
            x = zone[1] * ZONE_WIDTH + 10
            y = zone[0] * ZONE_HEIGHT + 40
            label = "[" + "-".join([letters[0], letters[-1]]) + "]"
            cv2.putText(frame, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        for (r, c), item in current_subgrid.items():
            x = c * ZONE_WIDTH + 20
            y = r * ZONE_HEIGHT + 60
            color = (255, 255, 0)
            if item == "BACK": color = (0, 100, 255)
            elif item == "SPACE": color = (200, 200, 200)
            elif item == "SPEAK": color = (0, 255, 0)
            cv2.putText(frame, item, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    # Draw prediction grid at bottom
    if main_grid_active and prediction_words:
        for i, word in enumerate(prediction_words):
            r, c = PREDICTION_GRID_POSITIONS[i]
            x = c * ZONE_WIDTH + 20
            y = r * ZONE_HEIGHT + 60
            cv2.putText(frame, word, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 200, 255), 2)
            cv2.rectangle(frame, (c * ZONE_WIDTH, r * ZONE_HEIGHT), ((c + 1) * ZONE_WIDTH, (r + 1) * ZONE_HEIGHT), (0, 200, 255), 2)

    cv2.putText(frame, "Sentence: " + sentence, (20, FRAME_HEIGHT - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    cv2.putText(frame, f"MODE: {mode.upper()} (Press TAB to switch)", (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    cv2.imshow("MindBoard – Dual Mode + GPT-2 Predictions", frame)
    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break
    elif key == 9:
        mode = "auto" if mode == "manual" else "manual"

cap.release()
cv2.destroyAllWindows()