# Fabric-Defect-Detection

Real-time fabric defect segmentation using **YOLOv8** on a **Raspberry Pi 4 (8GB)**.

---

## Author

**AKY Tricks**  

This project has been adapted for Raspberry Pi 4 (8GB) with Python, OpenCV, GPIO, and Picamera2 integration for real-time fabric defect detection.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Hardware Requirements](#hardware-requirements)  
- [Software Requirements](#software-requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Folder Structure](#folder-structure)  
- [License](#license)

---

## Overview

This project uses **YOLOv8** to detect defects in fabrics in real-time. It integrates a **Raspberry Pi camera**, GPIO-controlled LED indicators, and threading to manage live video capture and defect detection efficiently.

---

## Features

- Real-time fabric defect detection using YOLOv8.
- Raspberry Pi GPIO integration to indicate defects via LED.
- Saves frames containing defects automatically.
- Multi-threaded design for smooth capture and detection.
- Easy adaptation for different YOLOv8 models.

---

## Hardware Requirements

- Raspberry Pi 4 (8GB recommended)  
- Raspberry Pi Camera v2 or compatible (using Picamera2)  
- LED (connected to GPIO 18) for defect indication  
- Jumper wires and breadboard (optional)

---

## Software Requirements

- Python 3.10+  
- OpenCV  
- RPi.GPIO  
- Ultralyics YOLO library  
- Picamera2  
- NumPy  

**System-level dependencies:**  
See [`Apt_Get_Install.txt`](#apt-get-install) for required packages.

---

## Installation

### 1. System dependencies

Run the following commands on your Raspberry Pi terminal:

```bash
sudo apt install libcamera-dev
sudo apt install -y python3-libcamera python3-kms++ libcap-dev
sudo apt-get install libcap2
sudo apt-get install libpcap0.8
sudo apt install -y ffmpeg
sudo apt install -y libkms++-dev libfmt-dev libdrm-dev
sudo apt install -y libcamera-dev libgtk2.0-dev pkg-config

```

You can also refer to `Apt_Get_Install.txt` included in this repo.

---

### 2. Python dependencies

Install Python packages from `requirements.txt`:

```bash
pip3 install -r requirements.txt
```

**requirements.txt example:**

```
opencv-python
numpy
RPi.GPIO
ultralytics
picamera2
```

---

## Usage

1. Clone the repository to your Raspberry Pi:

```bash
git clone https://github.com/Yohanes213/Fabric-Defect-Detection.git
cd Fabric-Defect-Detection
```

2. Place your YOLOv8 `.pt` model in the specified path:

```
/home/pi/Desktop/fabric_defect_detection_yolov8/Fabric-Defect-Detection-main/runs/detect/train/weights/fabric_defect_detection_speedy_5v.pt
```

3. Run the main Python script:

```bash
python3 fabric_defect_detection_rpi.py
```

4. The camera window will display the live feed.  
   - LED turns **ON** when defects are detected.  
   - Frames with defects are saved to the `defect_frames` folder.

5. Press **q** in the OpenCV window to quit.

---

## Folder Structure

```
Fabric-Defect-Detection/
│
├─ defect_frames/          # Saved defect frames
├─ runs/                   # YOLOv8 training output
├─ fabric_defect_detection_rpi.py
├─ requirements.txt
├─ Apt_Get_Install.txt
└─ README.md
```

## Credit

This project is based on and adapted from the work of **Yohanes Teshome Kebede**:

   Original Repository: [Fabric-Defect-Detection](https://github.com/Yohanes213/Fabric-Defect-Detection/tree/main)
---

