# ✋ Volume Control using Hand Gestures

A computer vision-based application that enables users to control system volume using hand gestures captured through a webcam. The system detects hand landmarks in real time and maps finger distance to volume levels, providing a completely touch-free interaction experience.

---

## 📌 Project Overview

This project leverages MediaPipe and OpenCV to detect hand landmarks and interpret gestures. By measuring the distance between the thumb and index finger, the system dynamically adjusts the system volume.

It is designed for:

- Touch-free interaction systems
- Smart environments
- Assistive technologies

---

## 🚀 Features

- 🎥 Real-time webcam-based hand tracking
- ✋ 21 hand landmarks detection using MediaPipe
- 📏 Distance-based gesture recognition (thumb–index)
- 🔊 Smooth system volume control (0%–100%)
- 📊 Live analytics and performance metrics
- 📈 Graphs:
    - Distance → Volume mapping
    - Volume history
- 🎛 Adjustable detection parameters
- 🟢 Visual UI feedback (gesture, volume, FPS, etc.)
- ▶️ Start / Stop / Capture controls

---

## 🧠 How It Works

1. Hand Detection
    - Webcam feed is processed using MediaPipe Hands
    - 21 landmarks are detected per hand
2. Gesture Recognition
    - Thumb tip (Landmark 4) and Index tip (Landmark 8) are tracked
    - Euclidean distance between them is calculated
3. Volume Mapping
    - Distance is normalized between predefined min and max values
    - Mapped linearly to system volume (0–100%)
4. Volume Control
    - System volume is updated using Pycaw
    - History of last 20 values is stored
5. UI & Feedback
    - Real-time camera feed with landmark overlay
    - Volume bar and percentage display
    - Performance metrics:
      - Response time
      - Gesture quality
      - Accuracy

---

## 🖥️ User Interface

Before Starting Camera
- Camera inactive
- UI panels visible
- Graph placeholders initialized

After Starting Camera
- Live hand tracking with landmarks
- Distance measurement between fingers
- Real-time volume updates
- Dynamic graphs and metrics

---

## 🏗️ Project Structure

```
Volume_Control_with_Hand_Gestures/
│
├── app.py              # Main application with UI
├── milestone1.py       # Hand detection module
├── milestone2.py       # Gesture recognition module
├── milestone3.py       # Volume control module
├── milestone4.py       # Performance metrics module
├── requirements.txt   # Dependencies
├── .gitignore

```

---

## ⚙️ Installation


1. Clone the repository
```
git clone https://github.com/Nazneen-1/Volume_Control_with_Hand_Gestures.git
cd Volume_Control_with_Hand_Gestures
```
2. Create virtual environment (recommended)
```
python -m venv venv
venv\Scripts\activate   # Windows
```
4. Install dependencies
```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
python app.py
```
---

## 📊 Modules Implemented

Milestone 1: Hand Detection

- Webcam integration using OpenCV
- Hand landmark detection using MediaPipe

Milestone 2: Gesture Recognition

- Distance calculation between fingers
- Gesture classification (Closed, Pinch, Open)

Milestone 3: Volume Control

- Distance → Volume mapping
- System volume adjustment using Pycaw
- Volume smoothing and history tracking

Milestone 4: UI & Feedback
- Interactive Tkinter UI
- Real-time performance metrics
- Graph analytics

---

## 📈 Performance Metrics

- Accuracy: 100% (gesture detection logic-based)
- Response Time: ~140 ms (real-time)
- Gesture Quality: Good / Moderate / Poor

---

## 🔮 Future Improvements

- Multi-gesture support (brightness, media control)
- Machine learning-based gesture classification
- Cross-platform audio support (Linux/macOS)
- Custom gesture training
- Mobile integration

---

## 👨‍💻 Credits

- Developed as part of Infosys Virtual Internship 6.0
- Based on mentor-guided milestone implementation
- Technologies: OpenCV, MediaPipe, Pycaw, Tkinter

---

## 📜 License

This project is for academic and educational purposes.

---

## ⭐ Final Note

This project demonstrates how computer vision + human interaction can replace traditional input devices, enabling intuitive and touch-free control systems.

