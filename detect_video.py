from ultralytics import YOLO

model = YOLO("model/best.pt")

results = model.predict(
    source="video.mp4",
    conf=0.5,
    save=True,
    project="outputs",
    name="video_result"
)