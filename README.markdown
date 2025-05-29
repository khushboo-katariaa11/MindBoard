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













