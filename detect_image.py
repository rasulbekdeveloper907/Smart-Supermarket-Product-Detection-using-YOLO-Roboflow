from ultralytics import YOLO
from pathlib import Path

# Model manzili
MODEL_PATH = "runs/detect/train/weights/best.pt"

# Test rasmi
IMAGE_PATH = "data/test_images/test1.jpg"

# Natijalar saqlanadigan papka
OUTPUT_DIR = "outputs"

# Modelni yuklash
model = YOLO(MODEL_PATH)

# Detection
results = model.predict(
    source=IMAGE_PATH,
    conf=0.5,
    save=True,
    project=OUTPUT_DIR,
    name="image_detection",
    exist_ok=True
)

print("=" * 50)
print("✅ Detection completed successfully!")
print(f"📷 Image : {IMAGE_PATH}")
print(f"📁 Results saved in: {OUTPUT_DIR}/image_detection")
print("=" * 50)

# Aniqlangan obyektlarni chiqarish
for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        print(
            f"Object: {model.names[class_id]} | "
            f"Confidence: {confidence:.2f}"
        )