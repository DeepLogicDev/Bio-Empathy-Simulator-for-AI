# 🧠 Bio Empathy Simulator AI

Bio Empathy Simulator AI is a full-stack project that simulates empathy by detecting human emotions in real-time using facial expressions. It uses a deep learning model trained on FER-2013, a Flask backend for inference, and a React frontend for user interaction.

---

## 🚀 Features

- 🎥 Real-time webcam-based emotion recognition
- 🧠 Deep learning model trained on FER-2013
- 🔌 REST API for prediction
- 🌐 Frontend built with React

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/bio-empathy-simulator-ai.git
cd bio-empathy-simulator-ai
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
cd ../frontend
npm install
```

---

## 💻 Running the App

### Start the Backend Server

```bash
cd backend
python app.py
```

### Start the Frontend (React) App

```bash
cd ../frontend
npm start
```

The React app will run at [http://localhost:3000](http://localhost:3000) and the Flask backend at [http://localhost:5000](http://localhost:5000).

---

## 📦 Model Setup

### Option 1: Use a Pre-trained Model

Download a pre-trained emotion recognition model from one of the following sources:

- [HuggingFace (geeknix)](https://huggingface.co/geeknix/emotion-reg/blob/main/emotion_model.h5)
- [GitHub (dinuduke)](https://github.com/dinuduke/Facial-Emotion-Recognition/blob/master/models/emotion_model.hdf5)
- [HuggingFace (Hammad712)](https://huggingface.co/Hammad712/Emotion_Detection/blob/main/emotion_detection_model.h5)

After downloading, place the file here:

```
backend/models/emotion_model.h5
```

---

### Option 2: Train Your Own Model

1. Download the FER-2013 dataset from [Kaggle](https://www.kaggle.com/datasets/msambare/fer2013).
2. Place `fer2013.csv` in:

```
datasets/emotions/fer2013.csv
```

3. Run the training script:

```bash
cd backend
python train_model.py
```

This will train and save a model to `backend/models/emotion_model.h5`.

---

## 🤖 Emotion Classes

The model predicts one of the following 7 emotions:

- Angry
- Disgust
- Fear
- Happy
- Sad
- Surprise
- Neutral


---

## 📄 License

This project is for educational and research use.

---

