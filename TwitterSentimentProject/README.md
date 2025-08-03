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
---
## 🚀 Running the Web App
Start the Flask app using:

```bash
python app.py
```
Then open your browser and visit:

#### http://127.0.0.1:5000
---
## 🧠 Retrain the Model
If you want to retrain the sentiment model using dataset.csv, run:

```
python train_model.py
```
This will:

📥 Load the dataset from dataset.csv

🧠 Train a machine learning model for sentiment classification

💾 Save the trained model to sentiment_model.pkl

📊 Evaluate the model on a test split

📁 Store evaluation metrics (e.g., accuracy, precision, recall) in metrics.json

---
## 📈 Example
Input:

```
I love using this product!
```
Output:
```
Sentiment: Positive
```
---
## 📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

---
## 🙌 Acknowledgements
Developed with Flask and scikit-learn

---
## 👤 Author
Shamanth
* GitHub: @shamanth00000

Inspired by real-world Natural Language Processing applications




