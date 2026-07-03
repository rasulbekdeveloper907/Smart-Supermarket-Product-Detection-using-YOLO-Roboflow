# 🛒 Supermarket Product Detection using YOLOv11 & Roboflow

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![YOLO](https://img.shields.io/badge/YOLO-v11-green?style=for-the-badge)
![Roboflow](https://img.shields.io/badge/Roboflow-Object_Detection-purple?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-red?style=for-the-badge)

### 🚀 AI-powered Supermarket Product Detection System

Detect supermarket products in images and real-time webcam using **YOLOv11**, **Roboflow**, and **OpenCV**.

</div>

---

# 📌 Project Overview

This project is an Object Detection application that identifies supermarket products using a custom-trained YOLOv11 model.

The model can detect the following products:

- 🥤 Coca-Cola
- 🥤 Pepsi
- 🍟 Lays Chips
- 🍪 Oreo
- 🍫 KitKat

The project demonstrates a complete Computer Vision pipeline:

- Data Collection
- Image Annotation
- Dataset Augmentation
- Model Training
- Image Detection
- Real-Time Webcam Detection

---

# 🎯 Project Goal

Build a simple AI system capable of detecting supermarket products automatically from images or live camera feed.

---

# 🧠 Detected Classes

| Product | Class Name |
|----------|------------|
| 🥤 Coca-Cola | coca_cola |
| 🥤 Pepsi | pepsi |
| 🍟 Lays Chips | lays |
| 🍪 Oreo | oreo |
| 🍫 KitKat | kitkat |

---

# 🛠 Technologies Used

- Python
- YOLOv11
- Roboflow
- OpenCV
- NumPy
- Ultralytics

---

# 📂 Project Structure

```text
Supermarket_Product_Detection/
│
├── data/
│   ├── images/
│   └── test_images/
│
├── model/
│   └── best.pt
│
├── outputs/
│
├── detect_image.py
├── detect_video.py
├── webcam.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Supermarket_Product_Detection.git
```

Go to project folder

```bash
cd Supermarket_Product_Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run Image Detection

```bash
python detect_image.py
```

---

# 🎥 Run Webcam Detection

```bash
python webcam.py
```

Press **Q** to exit.

---

# 📊 Model Information

| Item | Value |
|------|-------|
| Model | YOLOv11 |
| Task | Object Detection |
| Framework | Ultralytics |
| Dataset | Roboflow |
| Classes | 5 |

---

# 📸 Example Detection

Detected objects:

✅ Coca-Cola

✅ Pepsi

✅ Lays Chips

✅ Oreo

✅ KitKat

Each detected object is displayed with:

- Bounding Box
- Class Name
- Confidence Score

---

# 🔮 Future Improvements

- Product Counting
- Barcode Detection
- Price Recognition
- Smart Checkout System
- Inventory Monitoring
- Shelf Analysis
- Streamlit Dashboard
- FastAPI REST API

---

# 📈 Learning Outcomes

Through this project, I learned:

- Object Detection Fundamentals
- Roboflow Annotation
- Dataset Augmentation
- YOLOv11 Training
- Model Evaluation
- OpenCV Integration
- Real-Time Object Detection

---

# 👨‍💻 Author

**Rasulbek Ruzmetov**

Python Developer | Machine Learning | Computer Vision

GitHub: https://github.com/yourusername

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps support future AI and Computer Vision projects.