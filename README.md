# FarmShakti - AI-Based Crop Disease Detection System 🌿🤖

[![Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?logo=streamlit&logoColor=white)](https://farmshakti-ai-based-crop-disease-detection.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/phalkemm159/FarmShakti-AI-Based-Crop-Disease-Detection-System)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌱 Overview

FarmShakti is an AI-powered web app that helps farmers detect plant diseases by simply uploading an image of the affected crop leaf.  
It leverages a deep learning model trained to classify multiple crop diseases and uses **Google Gemini AI** to provide easy-to-understand treatment advice for detected diseases — making it farmer-friendly and accessible to everyone! 👨‍🌾👩‍🌾

---

## 🚀 Live Demo

Try the live app here:  
👉 [https://farmshakti-ai-based-crop-disease-detection.streamlit.app/](https://farmshakti-ai-based-crop-disease-detection.streamlit.app/)

![image](https://github.com/user-attachments/assets/cd48d94b-3a7f-4a04-89cf-137a22560ec8)


---

## ✨ Key Features

- 📤 **Image Upload & Disease Prediction** - Upload crop leaf images for instant disease classification
- ⚡ **Automated Model Download** - Large trained model (~547 MB) auto-downloads from Google Drive on first run
- 🌿 **AI-Generated Treatment Advice** - Google Gemini API provides easy, emoji-rich treatment instructions
- 🎨 **Simple & Intuitive UI** - Streamlit-powered interface for seamless user experience
- 🔒 **Secure API Handling** - Environment variable protection for sensitive keys

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?logo=google&logoColor=white)

---

## 💻 Local Installation Guide

### Prerequisites
- Python 3.8+
- [Google API Key](https://makersuite.google.com/app/apikey) 🔑

### Setup Steps:

# 1. Clone repository
git clone https://github.com/phalkemm159/FarmShakti-AI-Based-Crop-Disease-Detection-System.git
cd FarmShakti-AI-Based-Crop-Disease-Detection-System

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
echo "GOOGLE_API_KEY=your_api_key_here" > .env  # Replace with your actual key

# 4. Launch application
streamlit run app.py

---

## 📂 Project Structure

.

├── app.py                      # 🚀 Main Streamlit application

├── class_indices.json          # 📝 Disease class mappings

├── trained_model/              # 🤖 Auto-downloaded model directory

├── requirements.txt            # 📦 Dependency list

├── .gitignore                  # 👻 Ignore patterns

├── .env                        # 🔒 API keys (example: GOOGLE_API_KEY)

└── README.md                   # 📖 You are here!

---

## ⚠️ Important Notes

🔐 Never commit your .env file - Add it to .gitignore to protect your API keys

📦 Model (~547 MB) downloads automatically from Google Drive on first launch

☁️ For cloud deployment, use Streamlit's Secrets Management

⏳ Initial model download may take several minutes depending on connection speed

---

## 🤝 Contributing

🍴 Fork the repository

🌿 Create a new branch (git checkout -b feature/amazing-feature)

💻 Make your changes

✅ Commit your changes (git commit -m 'Add amazing feature')

🚀 Push to branch (git push origin feature/amazing-feature)

🔄 Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See LICENSE file for details.

---

## 📬 Contact

Phalkemm159
Gmail
LinkedIn

---

## 🌾 Happy farming with AI-powered disease detection! 🌱
