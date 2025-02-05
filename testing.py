from ultralytics import YOLO
import cv2

# Load the trained YOLO model
model_path = "runs/detect/train3/weights/best.pt"  # Path to trained model
model = YOLO(model_path)

# Load the video
video_path = "testing.mp4"
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define output video writer
output_path = "output.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Process each frame
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break  # Stop when video ends

    # Run YOLO detection
    results = model(frame)

    # Render results on the frame
    for r in results:
        frame = r.plot()  # Draw detections on the frame

    # Save frame to output video
    out.write(frame)

    # Show frame (optional)
    cv2.imshow("YOLO Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processed video saved as {output_path}")
