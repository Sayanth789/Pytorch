from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

import torch
import io
from PIL import Image

from app.model import model, transform, classes

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Home page
@app.get("/", response_class=HTMLResponse)
def home():
    return FileResponse("app/static/index.html")


# Prediction endpoint
@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):

    contents = await file.read()

    image = Image.open(io.BytesIO(contents)).convert("RGB")

    image = transform(image).unsqueeze(0)

    model.eval()

    with torch.no_grad():

        outputs = model(image)

        probs = torch.softmax(outputs, dim=1)

        confidence, predicted = torch.max(probs, 1)

    prediction = classes[predicted.item()]

    confidence = float(confidence.item())

    return {
        "prediction": prediction,
        "confidence": confidence
    }
