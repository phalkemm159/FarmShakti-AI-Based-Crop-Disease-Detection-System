import os
import json
from PIL import Image
import numpy as np
import tensorflow as tf
import streamlit as st
from dotenv import load_dotenv
import gdown  # Added for downloading from Google Drive

import google.generativeai as genai

load_dotenv()  # This will read from the .env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get disease solution from Gemini
def get_disease_solution_from_gemini(disease_name):
    prompt = (
        f"Please explain the treatment or solution for the plant disease called '{disease_name}' "
        f"in a simple way that a farmer can easily understand. "
        f"Use friendly language and include helpful emojis to make it easier. 🌾😊"
    )
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

# Setup paths and model download
working_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(working_dir, "trained_model")
model_path = os.path.join(model_dir, "plant_disease_prediction_model.h5")

if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Google Drive file ID from your link
FILE_ID = "1mK0HiZl_yye9wXi5fYUCzF7CpCVksgup"
download_url = f"https://drive.google.com/uc?id={FILE_ID}"

if not os.path.exists(model_path):
    st.info("Downloading trained model from Google Drive, please wait...")
    gdown.download(download_url, model_path, quiet=False)

# Load the pre-trained model
model = tf.keras.models.load_model(model_path, compile=False)

# Load the class indices
class_indices = json.load(open(f"{working_dir}/class_indices.json"))

# Function to Load and Preprocess the Image
def load_and_preprocess_image(image_path, target_size=(224, 224)):
    img = Image.open(image_path)
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.
    return img_array

# Function to Predict Image Class
def predict_image_class(model, image_path, class_indices):
    preprocessed_img = load_and_preprocess_image(image_path)
    predictions = model.predict(preprocessed_img)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)]
    return predicted_class_name

# Streamlit App
st.title('🌿🔍FarmSathi: AI based Crop Disease Classifier🦠🍃')

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)

    with col1:
        resized_img = image.resize((150, 150))
        st.image(resized_img)

    with col2:
        if st.button('Classify'):
            prediction = predict_image_class(model, uploaded_image, class_indices)
            st.success(f'Prediction: {str(prediction)}')

            with st.spinner('Fetching treatment from Gemini AI...'):
                try:
                    solution = get_disease_solution_from_gemini(prediction)
                    st.markdown(f"### 🌱 Treatment / Solution:\n{solution}")
                except Exception as e:
                    st.error(f"Failed to fetch solution: {e}")
