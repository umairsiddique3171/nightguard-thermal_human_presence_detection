# import libraries
from ultralytics import YOLO
import os 
import cv2
import json
import numpy as np

# load model
model = YOLO("last.pt")
# C:\Users\US593\OneDrive\Desktop\New folder\custom_yolov8\runs\detect\train\weights\last.pt
# load frames
cap = cv2.VideoCapture('sample.mp4')

# saving frames
ret,frame = cap.read()
output_video = cv2.VideoWriter(os.path.join('.','results.mp4'),
                              cv2.VideoWriter_fourcc(*'MP4V'),
                              20,
                              (frame.shape[1],frame.shape[0]))

# read frames
ret = True
while ret:
    ret, frame = cap.read()
    if cv2.waitKey(25) & 0xFF == ord('n'):
        break

    # detections
    detections  = model(frame)   
    for detection in detections[0].boxes.data.tolist():
        if detection is not None: 
            x1, y1, x2, y2, score, class_id = detection
            if score > 0.75:
                score = f"{score:.2f}"
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f"threat {score}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 800, 600) 
    cv2.imshow('frame', frame)

    output_video.write(frame)

cap.release()
cv2.destroyAllWindows()