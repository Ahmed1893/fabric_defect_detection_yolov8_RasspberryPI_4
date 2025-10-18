import cv2
import os
import RPi.GPIO as GPIO
from ultralytics import YOLO
import threading
import queue
from picamera2 import Picamera2
import numpy as np
# Load the YOLOv8 model
model = YOLO('/home/du/Desktop/fabric_defect_detection_yolov8/Fabric-Defect-Detection-main/runs/detect/train/weights/fabric_defect_detection_speedy_5v.pt')

# Set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
led_pin = 18
GPIO.setup(led_pin, GPIO.OUT)

# Open webcam
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

# Queue for passing frames from detection thread to main thread
frame_queue = queue.Queue()

def capture_frames():
    while True:
        frame1 = picam2.capture_array()
        frame1_rgb = cv2.cvtColor(frame1, cv2.COLOR_BGRA2BGR)
        frame_queue.put(frame1_rgb)
        
        cv2.imshow('window', frame1_rgb)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

def defect_detection():
    # Create a folder to save frames when defect is detected
    defect_folder = 'defect_frames'
    if not os.path.exists(defect_folder):
        os.makedirs(defect_folder)

    while True:
        frame2 = frame_queue.get()
        results = model(frame2)

        if len(results) > 0 and len(results[0].boxes) > 0:
            GPIO.output(led_pin, GPIO.HIGH)
            frame_name = os.path.join(defect_folder, f"defect_frame_{len(os.listdir(defect_folder))}.jpg")
            
            annotated_frame = results[0].plot()
            cv2.imwrite(frame_name, annotated_frame)
            frame_queue.put(annotated_frame)  # Put annotated frame back in queue for display
        else:
            GPIO.output(led_pin, GPIO.LOW)
            frame_queue.put(frame2)  # Put original frame back in queue for display if no defect

# def display_frames():
    # while True:
        # frame3 = frame_queue.get()
        # cv2.imshow('frame', frame3)
        # if cv2.waitKey(1) & 0xFF == ord("q"):
            # break

def cleanup():
    GPIO.cleanup()
    cv2.destroyAllWindows()

# Create and start threads
capture_thread = threading.Thread(target=capture_frames)
detection_thread = threading.Thread(target=defect_detection)
# display_thread = threading.Thread(target=display_frames)

capture_thread.start()
detection_thread.start()
# display_thread.start()

# Wait for the capture thread to finish
capture_thread.join()

cleanup()
