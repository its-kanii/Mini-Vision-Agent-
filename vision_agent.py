import cv2
import pyttsx3
from ultralytics import YOLO

# Initialize TTS engine
engine = pyttsx3.init()

# Load YOLOv8 pre-trained model
model = YOLO(r"C:\Users\kanim\Desktop\Mini Vision Agent\yolov8n.pt")  # Use raw string to avoid Unicode escape error

# Start video capture (webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Capture frame by frame
    if not ret:
        break
    
    # Perform object detection on the frame
    results = model(frame)
    
    # Access the bounding boxes, labels, and confidences
    boxes = results[0].boxes
    for box in boxes:
        # Ensure that we're accessing a valid bounding box
        if len(box.xyxy) > 0:
            # Extract the coordinates and other details from the bounding box
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            confidence = box.conf[0].cpu().numpy()
            class_id = int(box.cls[0].cpu().numpy())
            label = model.names[class_id]  # Get the label for the detected object
            print(f"Detected: {label}")
            
            # Draw rectangle and label on the frame
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Speak the label
            engine.say(f"I see a {label}")
            engine.runAndWait()

    # Show the frame with detections
    cv2.imshow("YOLOv8 Object Detection", frame)
    
    # Break on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()


