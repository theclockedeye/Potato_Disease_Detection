# 🍃 Potato Leaf Disease Detection

This project is an AI-powered **Potato Leaf Disease Detection** system that helps farmers and researchers diagnose diseases in potato plants from leaf images.

## 📌 Features
✅ Upload an image of a potato leaf.
✅ AI model analyzes the image and predicts the disease.
✅ Provides three possible classifications:
   - **Healthy** 🍃
   - **Early Blight** 🌿
   - **Late Blight** 🍂
✅ Responsive user interface with a clean design.
✅ Image preview before prediction.
✅ Instant results with a loading animation.


## 🛠️ Technologies Used
| Technology       | Purpose                     |
|-----------------|---------------------------|
| HTML, CSS       | Frontend UI Design        |
| JavaScript      | Client-side Interactions  |
| Flask (Python)  | Backend API               |
| TensorFlow/Keras| AI Model for Prediction   |

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/theclockedeye/Potato_Disease_Detection
cd potato-leaf-disease
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask Server
```bash
python app.py
```

The server will start at `http://127.0.0.1:5000/`.

## 📸 Usage Guide
1️⃣ **Upload an Image** 📷: Click the `Choose Image` button and select a potato leaf image.
2️⃣ **Get Predictions** 🤖: The AI model processes the image and displays the disease classification.
3️⃣ **View Results** 📊: The detected disease is shown with an image preview.

## 🔥 API Endpoints
| Method | Endpoint  | Description            |
|--------|----------|------------------------|
| POST   | `/predict` | Uploads image & returns prediction |

## 🧠 Model Training
The model is trained on a dataset of potato leaf images using **Convolutional Neural Networks (CNNs)**. It classifies images into three categories:
- **Healthy** 🍃
- **Early Blight** 🌿
- **Late Blight** 🍂


## 👨‍💻 Contributors
- **Your Name** ([@theclockedeye](https://github.com/theclockedeye))

---
🔗 **[GitHub Repository](https://github.com/theclockedeye/Potato_Disease_Detection)**

