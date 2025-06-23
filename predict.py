from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best.pt')  # 根据实际路径调整

results = model.predict(
    conf=0.5,                    # 置信度阈值
    save=True,                   # 保存预测结果
    show=True,                   # 显示预测结果（可选）
    imgsz=640                    # 推理尺寸（与训练一致）
)