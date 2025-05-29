# 🧠 MindBoard – Hands-Free Communication for the Speech & Motor Impaired

MindBoard is an AI-powered, real-time communication system that enables individuals with speech or motor disabilities to express themselves using nothing but **nose movement** and a **webcam**. The system allows users to type, speak, and participate in live **Google Meet or Zoom meetings**, with no external hardware.

---

## 🚀 Features

### ✅ Core Functionalities
- **Nose-based Grid Navigation:** Select letters using head/nose movement.
- **Dwell-based Selection:** Auto-select letters after hovering for 1.5 seconds.
- **Dynamic Subgrid System:** Navigate a 3x3 parent grid and select from letter subgrids.
- **Sentence Construction:** Build full phrases using intuitive zone-based typing.
- **Text-to-Speech Support:** Automatically speak typed sentences.
- **Standalone ML Version:** Includes predictive text using HuggingFace (optional).
- **Google Meet Integration:** Works via OBS Virtual Camera.

### 🧠 Accessibility Impact
- Designed for users with ALS, cerebral palsy, spinal cord injuries, and stroke survivors.
- No keyboard, no mouse, no voice required.

---

## 🖥️ Modes of Use

### 🔹 Real-Time Google Meet Mode
Control a virtual camera feed via OpenCV, stream it to OBS, and share directly in Google Meet.

### 🔹 Standalone Mode
Use the grid system with optional ML prediction and text-to-speech offline.

---

## 🔧 Tech Stack

- **Frontend/UI:** OpenCV + Python overlay
- **CV & Tracking:** MediaPipe FaceMesh
- **Integration:** OBS Studio + Virtual Camera
- **Speech:** pyttsx3 (offline TTS)
- **ML (Optional):** HuggingFace Transformers
- **Virtual Camera (Alt):** pyvirtualcam

---

## 🛠️ Installation Instructions

### 📌 1. Clone the Repository

```bash
git clone https://github.com/your-repo/mindboard.git
cd mindboard
📌 2. Set Up Environment
bash
Always show details

Copy
pip install -r requirements.txt
If requirements.txt is not provided, manually install:

bash
Always show details

Copy
pip install opencv-python mediapipe pyttsx3 pyvirtualcam
For ML prediction:

bash
Always show details

Copy
pip install transformers
📌 3. Install OBS Studio
Download OBS Studio

Install OBS Virtual Camera

Open OBS → Click “Start Virtual Camera”

📌 4. Google Meet Integration
Run your mindboard_meet.py script (or main_meet_mode.py).

In OBS:

Add Window Capture → Select the MindBoard window.

Start Virtual Camera.

In Google Meet:

Go to Settings → Video → Choose OBS Virtual Camera.

You're now speaking via webcam input and nose-based navigation.

🧠 Project Architecture
scss
Always show details

Copy
Webcam → MediaPipe → Nose Tip Tracker
       ↓
   Grid Zone Detection (3x3)
       ↓
Dwell Selector → Sentence Builder
       ↓         ↘
   TTS (pyttsx3)  ML Prediction (HuggingFace)
       ↓
OpenCV Window → OBS Studio → Google Meet
🧪 How to Run (All Modes)
▶️ Meet Mode (OBS + Virtual Cam)
bash
Always show details

Copy
python mindboard_meet.py
▶️ Standalone Offline Mode
bash
Always show details

Copy
python mindboard_standalone.py
This version uses predictive models (optional), speaks via pyttsx3, and runs fully offline.

📂 File Structure
bash
Always show details

Copy
mindboard/
├── mindboard_meet.py             # Google Meet integration version
├── mindboard_standalone.py       # Offline ML + TTS version
├── requirements.txt
├── README.md
└── assets/                       # Icons, visuals, or ML files
🛡️ Known Issues & Mitigations
Issue	Fix/Strategy
OBS not detected in Meet	Ensure Virtual Camera is started in OBS
Webcam conflict	Close all other apps using the webcam
Gaze detection unstable	Switched to nose tip tracking for reliability
Auto-selection too fast	Adjustable dwell timer in script (default: 1.5s)

🧠 Why This Matters
Over 1.3 billion people globally live with some form of disability. MindBoard removes one of the most essential barriers — communication — using only a webcam and intelligent software. No installation, no hardware, just possibility.

📞 Contact & Credits
Made with ❤️ by Gopesh Bajaj
For hackathons, accessibility research, and real-world deployment.

🏁 License
MIT License – Free to use, modify, and distribute.
