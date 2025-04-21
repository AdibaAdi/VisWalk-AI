import torch
import cv2
import pyttsx3

import time
last_spoken = {}

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize text-to-speech
engine = pyttsx3.init()

print("Starting webcam... Press Q to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    detections = results.pandas().xyxy[0]

    for _, row in detections.iterrows():
        cls = row['name']
        conf = row['confidence']
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, f"{cls} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        # Speak only once every 5 seconds per class
        if conf > 0.5 and cls in ['person', 'car', 'chair', 'bench', 'dog', 'bicycle']:
            now = time.time()
            if cls not in last_spoken or (now - last_spoken[cls]) > 5:
                engine.say(f"Caution. {cls} ahead.")
                engine.runAndWait()
                last_spoken[cls] = now

    # Show webcam frame
    cv2.imshow('VisWalk Obstacle Detection', frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
