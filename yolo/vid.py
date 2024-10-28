from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Run inference on 'bus.jpg' with arguments
results = model.predict("room.mp4", save=True, conf=0.5, classes=[0], save_txt=False, show_conf=False)
