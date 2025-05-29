# 🧠 MindBoard – Hands-Free Communication for the Speech & Motor Impaired
# Made with ❤️ by OINK BOINK

**MindBoard** is an innovative, AI-powered, real-time communication system designed to empower individuals with speech or motor disabilities. It enables users to type and speak using only nose movements captured by a standard webcam—no external hardware required.

---

## 🚀 Features

### ✅ Core Functionalities
- **Nose-based Grid Navigation:** Intuitively navigate a letter grid using head/nose movements.
- **Dwell-based Selection:** Automatically select letters or commands by hovering the nose pointer over a target (default: 1.5s).
- **Dynamic Subgrid System:** Navigate through a 3x3 parent grid that expands into subgrids for efficient character selection.
- **Sentence Construction:** Build complete phrases using an intuitive zone-based interface.
- **Text-to-Speech (TTS):** Typed text is vocalized in real time for seamless conversation.
- **Google Meet/Zoom Integration:** Communicate during live meetings using OBS Virtual Camera.
- **Optional ML Predictive Typing:** Enhance speed with offline predictive text using HuggingFace Transformers.

---

## 🧠 Accessibility Impact

MindBoard enhances quality of life for individuals affected by:
- Amyotrophic Lateral Sclerosis (ALS)
- Cerebral Palsy
- Spinal Cord Injuries
- Stroke
- Other conditions impairing speech and motor control

> A truly hands-free communication tool—no keyboard, no mouse, no voice commands.

---

## 🖥️ Modes of Use

### 🔹 Real-Time Google Meet/Zoom Mode
1. Uses OpenCV to create a virtual camera feed with the communication grid.
2. Feed is streamed to OBS Studio.
3. OBS Virtual Camera is selected in video conferencing tools (e.g., Meet, Zoom).
4. Sentences typed via nose movements are spoken aloud and visually highlighted.

### 🔹 Standalone Mode
- Use MindBoard offline for typing and TTS without internet access.
- Includes optional ML-based predictive text for improved speed.

---

## 🔧 Tech Stack

| Component              | Technology                     |
|------------------------|--------------------------------|
| Programming Language   | Python                         |
| UI & Grid Overlay      | OpenCV                         |
| Nose Tracking          | MediaPipe FaceMesh             |
| TTS Engine             | pyttsx3                        |
| ML Predictive Text     | HuggingFace Transformers       |
| Video Integration      | OBS Studio + Virtual Camera    |
| Alt Virtual Cam        | pyvirtualcam (optional)        |

---

## 🛠️ Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/mindboard.git
cd mindboard
```

### 2. Set Up Python Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
#Install all required packages using the requirements file:
```
pip install -r requirements.txt
```
# If requirements.txt is not available, install manually:

```
pip install opencv-python mediapipe pyttsx3 pyvirtualcam
```
# For optional ML predictive text:

```
pip install transformers torch torchvision torchaudio
# or, for TensorFlow
pip install transformers tensorflow

```
## 4. Install OBS Studio & Virtual Camera

1.  **Download OBS Studio**: Go to [https://obsproject.com/](https://obsproject.com/)
2.  **Install and open OBS Studio**.
3.  Ensure **Virtual Camera** is available (it's enabled by default in modern OBS versions).
4.  In OBS, click **Start Virtual Camera** in the **Controls** dock.

## ▶️ How to Run

After completing the [Installation Instructions](#️-installation-instructions), follow these steps to launch and use MindBoard.

### 1. Run the MindBoard Application

Open your terminal or command prompt, navigate to the `mindboard` directory (where you cloned the repository and installed dependencies), and execute the main script:

```bash
python mindboard.py

```
## How it Works
Once the application starts, you'll see your webcam feed with an overlaid grid and various text elements.

1.  **Position Yourself:** Ensure your face is well-lit and clearly visible to the webcam.

2.  **Mode Switching:**
    * The current mode is displayed at the top left.
    * Press the **`TAB`** key on your keyboard to switch between "MANUAL" and "AUTO" modes.

3.  **Typing in Manual Mode:**
    * **Selection:** Move your head to position your **nose tip** over the desired grid zone.
    * **Confirmation:** Hold your gaze on the zone for approximately **1.5 seconds** (dwell time). The zone will be highlighted in yellow to indicate selection.
    * **Keyboard Interaction:**
        * When the **main grid** is active, zones represent groups of letters (e.g., [A-E], [F-J]).
        * Selecting a main grid zone switches to a **sub-grid**, displaying individual characters from that group, plus "**BACK**" (to return to the main grid), "**SPACE**", and "**SPEAK**".
        * Selecting a **character** adds it to your sentence.
        * Selecting "**SPACE**" adds a space to your sentence.
        * Selecting "**SPEAK**" converts the current sentence to speech.
    * **Word Predictions:** Look at the bottom row of the grid. If prediction words appear, you can select one of the three prediction zones to append the suggested word to your sentence.

4.  **Typing in Auto Mode:**
    * **Scanning:** The system will automatically highlight each grid zone in a cycling pattern.
    * **Selection:** When the desired zone is highlighted, **blink** your eyes to select it.
    * The subsequent interactions for main grid, sub-grid, and actions are the same as in Manual Mode.

5.  **Exiting:**
    * Press the **`ESC`** key to close the application.

---

## ⚙️ Configuration & Usage

### 🔹 Google Meet/Zoom Integration (Real-Time Mode)

1.  **Run MindBoard App**
    ```bash
    python mindboard_meet.py
    ```
    This will launch a webcam feed with the communication grid overlay.

2.  **Set Up OBS Studio**
    * Open **OBS Studio**.
    * Add a **Window Capture** source:
        * Click the `+` button in the **Sources** dock.
        * Choose **Window Capture**.
        * Select the **MindBoard application window**.
        * Resize and position as needed.
    * Click **Start Virtual Camera** in the **Controls** dock.

3.  **Configure Google Meet/Zoom**
    * **Google Meet**:
        * Click the **three dots** → **Settings** → **Video** → **Camera** → **OBS Virtual Camera**.
    * **Zoom**:
        * Click the arrow next to **Start/Stop Video** → **Video Settings** → **Camera** → **OBS Virtual Camera**.

    Your nose-controlled MindBoard interface will now appear in the meeting, and TTS will vocalize your typed text.


📄 License
Include your license information here (e.g., MIT, GPL, Apache 2.0).

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.













