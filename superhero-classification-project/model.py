import torch
import pickle
from torchvision import transforms, models
from PIL import Image
import os

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model info (classes + transform)
info_path = os.path.join("models", "model_info.pkl")
if not os.path.exists(info_path):
    raise FileNotFoundError(f"{info_path} not found")

with open(info_path, "rb") as f:
    info = pickle.load(f)

classes = info["classes"]
transform = info["transform"]

# Load the full model
model_path = os.path.join("models", "full_superhero_model.pth")
if not os.path.exists(model_path):
    raise FileNotFoundError(f"{model_path} not found")

try:
    model = torch.load(model_path, map_location=device, weights_only=False)
except Exception:
    # fallback: load as state_dict
    print("Loading as state_dict")
    model = models.resnet18(num_classes=len(classes))
    model.load_state_dict(torch.load(model_path, map_location=device))

model.eval()

# Predict function
def predict(model, classes, transform, image_path):
    img = Image.open(image_path).convert("RGB")
    img_tensor = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(img_tensor)
        _, predicted = torch.max(outputs, 1)
    return classes[predicted.item()]
