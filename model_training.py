from ultralytics import YOLO

# Load a YOLO11 model
model = YOLO("yolo11n.pt")

# Train the model
model.train(data="/home/justinlamlamlam/warwick/es3h3/full_dataset/data.yaml", epochs=50)

# Validate on training data
model.val()
success = model.export(format="onnx")