# File: scripts/train.py
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models

def train_model():
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    train_data = datasets.ImageFolder("dataset/train", transform=transform)
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=32, shuffle=True)
    
    model = models.resnet18(pretrained=True)
    model.fc = nn.Linear(512, len(train_data.classes))
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    for epoch in range(5):
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")
    
    torch.save(model, "models/model.pth")
    print("Model saved successfully.")

if __name__ == "__main__":
    train_model()