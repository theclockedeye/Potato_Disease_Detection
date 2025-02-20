# File: scripts/test.py
import torch
from torchvision import transforms, datasets

def test_model():
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    test_data = datasets.ImageFolder("dataset/test", transform=transform)
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=32, shuffle=False)
    
    model = torch.load("models/model.pth")
    model.eval()
    correct = 0
    total = 0
    
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)
    
    print(f"Accuracy: {100 * correct / total:.2f}%")

if __name__ == "__main__":
    test_model()