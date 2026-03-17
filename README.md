### ✋ Volume Control using Hand Gestures

A computer vision-based application that enables users to control system volume using hand gestures captured through a webcam. The system detects hand landmarks in real time and maps finger distance to volume levels, providing a completely touch-free interaction experience.

📌 Project Overview

This project leverages MediaPipe and OpenCV to detect hand landmarks and interpret gestures. By measuring the distance between the thumb and index finger, the system dynamically adjusts the system volume.

It is designed for:

Touch-free interaction systems

Smart environments

Assistive technologies

🚀 Features

🎥 Real-time webcam-based hand tracking

✋ 21 hand landmarks detection using MediaPipe

📏 Distance-based gesture recognition (thumb–index)

🔊 Smooth system volume control (0%–100%)

📊 Live analytics and performance metrics

📈 Graphs:

Distance → Volume mapping

Volume history

🎛 Adjustable detection parameters

🟢 Visual UI feedback (gesture, volume, FPS, etc.)

▶️ Start / Stop / Capture controls

🧠 How It Works

Hand Detection

Webcam feed is processed using MediaPipe Hands

21 landmarks are detected per hand

Gesture Recognition

Thumb tip (Landmark 4) and Index tip (Landmark 8) are tracked

Euclidean distance between them is calculated

Volume Mapping

Distance is normalized between predefined min and max values

Mapped linearly to system volume (0–100%)

Volume Control

System volume is updated using Pycaw

History of last 20 values is stored

UI & Feedback

Real-time camera feed with landmark overlay

Volume bar and percentage display

Performance metrics:

Response time

Gesture quality

Accuracy

🖥️ User Interface
🔹 Before Starting Camera
