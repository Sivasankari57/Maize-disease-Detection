import os
import io
import numpy as np
import tensorflow as tf
from PIL import Image
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Disease classes
class_names = [
    "Blight",
    "Common_Rust",
    "Gray_Leaf_Spot",
    "Healthy"
]

# Load model
model = None

def load_model():
    global model
    try:
        model = tf.keras.models.load_model("model_full.h5")
        print("✅ Model loaded successfully")
    except Exception as e:
        print("❌ Model failed to load:", e)

load_model()


# Home route
@app.get("/")
def home():
    return {
        "status": "API running",
        "model_loaded": model is not None
    }


# Image preprocessing
def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image


# Prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    try:
        image_bytes = await file.read()

        image = preprocess_image(image_bytes)

        prediction = model.predict(image)

        predicted_class = int(np.argmax(prediction[0]))
        confidence = float(np.max(prediction[0]))

        disease_mapping = {
            0: {
                "name": "Blight",
                "solution": "Use resistant hybrids and rotate crops."
            },
            1: {
                "name": "Common Rust",
                "solution": "Use resistant varieties and apply fungicides."
            },
            2: {
                "name": "Gray Leaf Spot",
                "solution": "Use fungicide and maintain proper field drainage."
            },
            3: {
                "name": "Healthy",
                "solution": "No action needed. Your maize plant is healthy."
            }
        }

        disease = disease_mapping[predicted_class]

        return {
            "prediction": disease["name"],
            "confidence": confidence,
            "solution": disease["solution"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Optional test endpoint
@app.post("/test-image")
async def test_image(file: UploadFile = File(...)):

    image_bytes = await file.read()

    try:
        image = preprocess_image(image_bytes)
        prediction = model.predict(image)

        results = {
            class_names[i]: float(prediction[0][i])
            for i in range(len(class_names))
        }

        return {
            "all_class_confidence": results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run server directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)