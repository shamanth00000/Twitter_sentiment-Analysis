from flask import Flask, render_template, request
import joblib
import json
from textblob import TextBlob

app = Flask(__name__)
model = joblib.load("sentiment_model.pkl")

# Load accuracy from training
with open("metrics.json") as f:
    metrics = json.load(f)
accuracy = metrics.get("accuracy", 0.0)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    polarity = None
    confidence = None
    tweet = ""

    if request.method == "POST":
        tweet = request.form["tweet"]

        # Predict sentiment
        prediction = model.predict([tweet])[0]

        # Get probability
        probas = model.predict_proba([tweet])[0]
        labels = model.classes_
        pred_index = list(labels).index(prediction)
        confidence = round(probas[pred_index] * 100, 2)

        # Polarity score
        polarity = round(TextBlob(tweet).sentiment.polarity, 2)

    return render_template("index.html", prediction=prediction, polarity=polarity,
                           confidence=confidence, accuracy=accuracy, tweet=tweet)

if __name__ == "__main__":
    app.run(debug=True)
