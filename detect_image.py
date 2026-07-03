from ultralytics import YOLO

# Modelni yuklash
model = YOLO("model/best.pt")

# Rasmni tekshirish
results = model.predict(
    source="data/test_images/test1.jpg",
    conf=0.5,
    save=True,
    project="outputs",
    name="image_result"
)

print("Detection tugadi!")