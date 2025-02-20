# File: scripts/preprocess.py
import os
from PIL import Image
import torchvision.transforms as transforms

def preprocess_images(input_dir, output_dir):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    os.makedirs(output_dir, exist_ok=True)
    for file_name in os.listdir(input_dir):
        img_path = os.path.join(input_dir, file_name)
        img = Image.open(img_path).convert("RGB")
        img = transform(img)
        img.save(os.path.join(output_dir, file_name))

if __name__ == "__main__":
    preprocess_images("dataset/train", "dataset/preprocessed")