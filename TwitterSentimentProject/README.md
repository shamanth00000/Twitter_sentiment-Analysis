# 🐦 Twitter Sentiment Analysis

A machine learning web application that analyzes the sentiment of tweets. It classifies text input as **Positive**, **Negative**, or **Neutral** using a trained model, and presents results via a simple Flask-based web interface.

---

## 📌 Features

- 🔍 Sentiment classification using machine learning
- 📊 Pre-trained model with evaluation metrics
- 🧪 Easy retraining with `train_model.py`
- 🌐 Web interface with Flask
- 🧱 Modular and easy-to-understand project structure

---

## 🗂️ Project Structure
twitter-sentiment-analysis/

├── static/               # CSS and static assets (images, JS, etc.)

├── templates/            # HTML templates for the web UI

├── app.py                # Flask app entry point

├── train_model.py        # Script to train the sentiment analysis model

├── sentiment_model.pkl   # Serialized trained model (pickle file)

├── dataset.csv           # Labeled dataset used for training

├── metrics.json          # Evaluation results (accuracy, precision, recall, etc.)

├── LICENSE               # License information

└── README.md             # Project documentation



---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/shamanth00000/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
```

