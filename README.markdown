# 🧠 MindBoard – Hands-Free Communication for the Speech & Motor Impaired

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
