from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import torch
import torchvision.transforms as transforms
from PIL import Image
import os

app = Flask(__name__, template_folder="templates")
CORS(app)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), "../models/model.pth")
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

model = torch.load(model_path, map_location=torch.device("cpu"),weights_only=False)
model.eval()

# Image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Class labels
labels = {2: "Healthy 🍃", 0: "Early Blight 🌿", 1: "Late Blight 🍂"}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    try:
        img = Image.open(file.stream).convert("RGB")
        img = transform(img).unsqueeze(0)

        with torch.no_grad():
            output = model(img)
            _, predicted = torch.max(output, 1)

        return jsonify({"prediction": predicted.item(), "disease": labels.get(predicted.item(), "Unknown")})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
