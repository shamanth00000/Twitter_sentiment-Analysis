import pandas as pd
import joblib
import json
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay

# Load data
df = pd.read_csv("dataset.csv")
X = df["tweet"]
y = df["sentiment"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=300))
])
pipeline.fit(X_train, y_train)

# Save model
joblib.dump(pipeline, "sentiment_model.pkl")

# Evaluate
y_pred = pipeline.predict(X_test)
accuracy = round(accuracy_score(y_test, y_pred) * 100, 2)

# Save accuracy
with open("metrics.json", "w") as f:
    json.dump({"accuracy": accuracy}, f)

# Confusion matrix
disp = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title(f"Confusion Matrix (Accuracy: {accuracy}%)")
plt.tight_layout()
plt.savefig("static/confusion_matrix.png")
plt.close()

