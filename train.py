from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

model.train(data='/home/davidjiang/下载/detect/data.yaml', epochs=50, batch=16, imgsz=640)