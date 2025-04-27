# 📡 Tello Drone Educational Control & Video Streaming

This project demonstrates **basic control** of a DJI Tello drone while **simultaneously recording and displaying** its video feed using Python.

It is intended **for educational purposes**, to help beginners learn about:
- Drone programming
- Real-time video processing
- Threading in Python
- Basic OpenCV usage

---

## ✈️ Features
- Connect to the Tello drone over WiFi.
- Stream the drone’s live video feed.
- Display and record the video while flying.
- Execute simple **pre-programmed flight routines**.
- Clean shutdown of resources (camera, files, and drone connection).

---

## 📚 Educational Focus
This project is designed to teach and demonstrate:
- How to interact with the Tello SDK using `djitellopy`.
- Basics of concurrent programming using Python’s `threading` module.
- Real-time video capture, processing, and display with `OpenCV`.
- Handling drone movement commands safely.

> ⚠️ **Disclaimer:**  
> This project is **not intended for production** or autonomous operations.  
> It is meant purely for **learning, experimentation, and classroom use**.

---

## 🛠 Requirements
- Python 3.7+
- DJI Tello Drone
- WiFi connection to the drone
- Python libraries:
  - `djitellopy`
  - `opencv-python`
- (Optional) `numpy` (usually installed automatically with OpenCV)
