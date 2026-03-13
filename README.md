🌽 Maize Disease Detection using Deep Learning
📌 Project Overview

# Maize (corn) is one of the most important crops worldwide. Early detection of leaf diseases helps farmers reduce crop loss and improve yield.
# This project is an AI-powered web application that detects maize leaf diseases from uploaded images using a deep learning model.
# The system uses a trained Convolutional Neural Network (CNN) model to classify maize leaf images into different disease categories and provide recommendations for treatment.

🚀 Features
# Upload maize leaf image for disease detection
# AI-powered prediction using a trained deep learning model
# Displays disease name and prediction confidence
# Provides recommended solution for detected disease
# Simple and interactive web interface

🧠 Technologies Used
**Frontend**
 React.js
**Backend**
 FastAPI (Python)
**Machine Learning**
 TensorFlow / Keras
 Convolutional Neural Network (CNN)
**Other Tools**
Node.js
JavaScript
HTML / CSS
Python

📊 Dataset
The model was trained using the Corn or Maize Leaf Disease Dataset from Kaggle.
Dataset Link:
https://www.kaggle.com/datasets/smaranjitghose/corn-or-maize-leaf-disease-dataset
Dataset contains images of maize leaves belonging to multiple disease classes.

🗂 Project Structure
maize-disease-detection
│
├── maizecare-frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── main.py
├── model_full.h5
├── requirements.txt
└── README.md

⚙️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/yourusername/maize-disease-detection.git
cd maize-disease-detection
2️⃣ Install Backend Dependencies
pip install fastapi uvicorn tensorflow pillow numpy python-multipart
3️⃣ Start the Backend Server
py -m uvicorn main:app --reload
Backend will run at:
http://127.0.0.1:8000
API documentation:
http://127.0.0.1:8000/docs
4️⃣ Start the Frontend
Go to frontend folder:
cd maizecare-frontend
Install dependencies:
npm install
Run the React app:
npm start
Frontend will run at:
http://localhost:3000

🖥️ Application Workflow
#User uploads a maize leaf image
#Image is sent to the FastAPI backend
#Backend processes the image using the trained TensorFlow model
#Model predicts the disease class
#Prediction and confidence are returned to the frontend

📸 Example Output
#The application displays:
#Detected disease name
#Prediction confidence
#Recommended solution for farmers

🌱 Future Improvements
#Mobile app version
#Real-time camera detection
#Integration with agricultural advisory systems
#Support for more crop diseases
👤 Author
Sivasankari M
