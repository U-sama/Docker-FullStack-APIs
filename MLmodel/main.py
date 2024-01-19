from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
from io import BytesIO
import tensorflow as tf
from keras.preprocessing import image
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your image classification model
model = tf.keras.models.load_model('./my_model.h5')
class_labels = ["Cat", "Dog"]  # Replace with your actual class labels

def preprocess_image(file):
    img = Image.open(BytesIO(file))
    img = img.resize((200, 200))  # Adjust the size based on your model's input requirements
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    start_time = time.time()
    try:
        img_array = preprocess_image(await file.read())
        predictions = model.predict(img_array)
        predicted_class_index = np.argmax(predictions)
        predicted_class_label = class_labels[predicted_class_index]
        end_time = time.time()
        response_time = end_time - start_time
        print(f"Predicted class: {predicted_class_label}, response_time: {response_time}")
        return JSONResponse(content={"class": predicted_class_label, "response_time": response_time}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)