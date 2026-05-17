# AI Virtual Mouse

A computer vision-based project that enables hands-free control of your computer mouse using real-time hand gesture recognition. Control your cursor movements and perform clicks using just your webcam!

## Features

- **Hand Gesture Recognition**: Uses MediaPipe for real-time hand tracking and landmark detection
- **Cursor Movement**: Move your mouse pointer by tracking your index finger position
- **Click Gesture**: Perform clicks by bringing your thumb and index finger close together (pinch gesture)
- **Exit Command**: Show all five fingers to smoothly exit the application
- **Real-time Feedback**: Visual feedback displaying distance metrics and finger count
- **Smooth Tracking**: Optimized for responsive and fluid cursor movement

## Tech Stack

- **Python 3.x**
- **OpenCV** - Video processing and frame manipulation
- **MediaPipe** - Hand detection and landmark tracking
- **PyAutoGUI** - System cursor control
- **Webcam** - Real-time video input

## Requirements

```bash
python >= 3.8
opencv-python >= 4.5.0
mediapipe >= 0.8.0
pyautogui >= 0.9.53  
