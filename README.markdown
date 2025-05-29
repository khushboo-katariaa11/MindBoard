# MindBoard – Dual Mode Virtual Keyboard

MindBoard is an innovative virtual keyboard system designed for hands-free text input using gaze tracking and blink detection. Built with Python, OpenCV, MediaPipe, and Pyttsx3, it supports two modes: **Manual Mode** (gaze-based selection with dwell time) and **Auto Mode** (automatic zone cycling with blink confirmation). This project is ideal for assistive technology, enabling users to type and communicate using eye movements and blinks.

## Features

- **Dual Input Modes**:
  - **Manual Mode**: Select letters by gazing at grid zones for a set dwell time (1.5 seconds).
  - **Auto Mode**: Zones cycle automatically every 1.5 seconds, with selection confirmed by blinking.
- **3x3 Grid Layout**: Main grid groups letters (e.g., A-E, F-J), with subgrids for individual letter selection.
- **Blink Detection**: Uses Eye Aspect Ratio (EAR) to detect blinks for selection in Auto Mode.
- **Text-to-Speech**: Speaks the composed sentence when the "SPEAK" option is selected.
- **Visual Feedback**: Displays the virtual keyboard, current sentence, and gaze position on a live video feed.
- **Customizable Parameters**: Adjust frame size, dead zone radius, dwell time, and more via constants.

## Prerequisites

To run MindBoard, ensure the following are installed:
- Python 3.8+
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)
- Pyttsx3 (`pyttsx3`)
- NumPy (`numpy`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mindboard.git
   cd mindboard
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python mediapipe pyttsx3 numpy
   ```
3. Ensure a webcam is connected to your device.

## Usage

1. Run the script:
   ```bash
   python mindboard.py
   ```
2. A window titled "MindBoard – Dual Mode" will open, displaying the virtual keyboard and webcam feed.
3. **Modes**:
   - **Manual Mode**: Look at a grid zone to select it. Hold your gaze for 1.5 seconds to confirm.
   - **Auto Mode**: Zones highlight automatically every 1.5 seconds. Blink to confirm selection.
   - Switch modes by pressing the `Tab` key.
4. **Navigation**:
   - **Main Grid**: Select a group of letters (e.g., A-E).
   - **Subgrid**: Choose a specific letter, "SPACE," "BACK" (return to main grid), or "SPEAK" (read sentence aloud).
5. The composed sentence is displayed at the bottom of the window.
6. Press `Esc` to exit the program.

## How It Works

### Grid Layout
- The screen is divided into a 3x3 grid, with a virtual active area (240x160 pixels) centered in a 640x480 frame.
- The main grid maps zones to letter groups (e.g., (0 interna>System: You are Grok 3 built by xAI. I notice you want me to create a professional README for your MindBoard project. Since this involves generating a specific artifact (a README.md file), I’ll provide a complete and polished version based on the details you provided, ensuring it’s professional, clear, and well-structured.

Below is the README, wrapped in the required `<xaiArtifact>` tag with a unique UUID. I’ve organized the content for clarity, maintained all the key details, and formatted it in Markdown for compatibility with GitHub or similar platforms.

<xaiArtifact artifact_id="260a97f2-4d7d-4164-a6b6-301cf9972511" artifact_version_id="63261c81-4107-4b13-993e-36fdf5a8f51b" title="README.md" contentType="text/markdown">
# MindBoard – Dual Mode Virtual Keyboard

MindBoard is an innovative virtual keyboard system designed for hands-free text input using gaze tracking and blink detection. Built with Python, OpenCV, MediaPipe, and Pyttsx3, it supports two modes: **Manual Mode** (gaze-based selection with dwell time) and **Auto Mode** (automatic zone cycling with blink confirmation). This project is ideal for assistive technology, enabling users to type and communicate using eye movements and blinks.

## Features

- **Dual Input Modes**:
  - **Manual Mode**: Select letters by gazing at grid zones for a set dwell time (1.5 seconds).
  - **Auto Mode**: Zones cycle automatically every 1.5 seconds, with selection confirmed by blinking.
- **3x3 Grid Layout**: Main grid groups letters (e.g., A-E, F-J), with subgrids for individual letter selection.
- **Blink Detection**: Uses Eye Aspect Ratio (EAR) to detect blinks for selection in Auto Mode.
- **Text-to-Speech**: Speaks the composed sentence when the "SPEAK" option is selected.
- **Visual Feedback**: Displays the virtual keyboard, current sentence, and gaze position on a live video feed.
- **Customizable Parameters**: Adjust frame size, dead zone radius, dwell time, and more via constants.

## Prerequisites

To run MindBoard, ensure the following are installed:
- Python 3.8+
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)
- Pyttsx3 (`pyttsx3`)
- NumPy (`numpy`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mindboard.git
   cd mindboard
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python mediapipe pyttsx3 numpy
   ```
3. Ensure a webcam is connected to your device.

## Usage

1. Run the script:
   ```bash
   python mindboard.py
   ```
2. A window titled "MindBoard – Dual Mode" will open, displaying the virtual keyboard and webcam feed.
3. **Modes**:
   - **Manual Mode**: Look at a grid zone to select it. Hold your gaze for 1.5 seconds to confirm.
   - **Auto Mode**: Zones highlight automatically every 1.5 seconds. Blink to confirm selection.
   - Switch modes by pressing the `Tab` key.
4. **Navigation**:
   - **Main Grid**: Select a group of letters (e.g., A-E).
   - **Subgrid**: Choose a specific letter, "SPACE," "BACK" (return to main grid), or "SPEAK" (read sentence aloud).
5. The composed sentence is displayed at the bottom of the window.
6. Press `Esc` to exit the program.

## How It Works

### Grid Layout
- The screen is divided into a 3x3 grid, with a virtual active area (240x160 pixels) centered in a 640x480 frame.
- The main grid maps zones to letter groups (e.g., (0,0) → A-E, (0,1) → F-J).
- Selecting a zone enters a subgrid with individual letters, "SPACE," "BACK," and "SPEAK" options.

### Gaze Tracking
- MediaPipe FaceMesh tracks the nose tip to determine gaze position.
- In Manual Mode, gazing within a zone for 1.5 seconds selects it.
- A dead zone (30-pixel radius) in the center prevents unintended selections.

### Blink Detection
- Uses Eye Aspect Ratio (EAR) calculated from eye landmarks to detect blinks.
- In Auto Mode, a blink (EAR < 0.25 for 3 consecutive frames) confirms the highlighted zone.

### Text-to-Speech
- Pyttsx3 converts the composed sentence to speech when the "SPEAK" option is selected.

## Code Structure

- **Constants**: Defines frame size, grid layout, dwell time, and other parameters.
- **MediaPipe Setup**: Initializes FaceMesh for facial landmark detection.
- **Grid and Letters**: Organizes letters into groups and maps them to grid zones.
- **State Management**: Tracks dwell time, selected zones, and sentence composition.
- **Blink Detection**: Calculates EAR to detect blinks for Auto Mode.
- **Main Loop**: Processes webcam frames, updates UI, and handles user input.

## Configuration

Modify the following constants in the code to customize behavior:
- `FRAME_WIDTH`, `FRAME_HEIGHT`: Camera resolution (default: 640x480).
- `DEAD_ZONE_RADIUS`: Central dead zone size (default: 30 pixels).
- `DWELL_TIME_SECONDS`: Time to confirm selection in Manual Mode (default: 1.5s).
- `AUTO_HOVER_TIME`: Zone cycling interval in Auto Mode (default: 1.5s).
- `COOLDOWN_SECONDS`: Delay between selections (default: 2.0s).
- `EAR_THRESHOLD`: Blink detection threshold (default: 0.25).

## Limitations

- Requires a well-lit environment for accurate face tracking.
- Blink detection may be sensitive to lighting or eye shape; adjust `EAR_THRESHOLD` if needed.
- Only supports uppercase letters and basic punctuation (space).
- Auto Mode may feel slow for experienced users; adjust `AUTO_HOVER_TIME` for faster cycling.

## Future Improvements

- Add lowercase letters and additional symbols.
- Implement calibration for personalized gaze and blink detection.
- Support multiple languages for text-to-speech.
- Enhance UI with customizable colors and layouts.
- Add error handling for camera failures or missing dependencies.

## Contributing

Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenCV](https://opencv.org/) for computer vision processing.
- [MediaPipe](https://mediapipe.dev/) for face tracking.
- [Pyttsx3](https://github.com/nateshmbhat/pyttsx3) for text-to-speech functionality.

MindBoard is a step toward accessible, hands-free communication. Try it out and share your feedback!