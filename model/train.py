import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training data
texts = [
    "I love this product",
    "This is the best thing ever",
    "I hate it",
    "This is terrible",
    "Absolutely fantastic experience",
    "Worst purchase I’ve made"
]
labels = ["positive", "positive", "negative", "negative", "positive", "negative"]

# Create vectorizer and model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

# Save to disk
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model and vectorizer saved.")
