# model/train.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample dataset
data = {
    "text": [
        "I love this product",
        "This is the worst experience ever",
        "Amazing quality and fast delivery",
        "Terrible, I want my money back",
        "Very satisfied with the service",
        "Awful, do not recommend"
    ],
    "label": [1, 0, 1, 0, 1, 0]  # 1 = positive, 0 = negative
}

df = pd.DataFrame(data)

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model and vectorizer saved.")
