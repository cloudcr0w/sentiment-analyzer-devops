from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Sentiment Analyzer API is running"}

@app.post("/predict")
def predict_sentiment(text: str):
    # TODO: Load model, vectorizer, and return prediction
    return {"input": text, "sentiment": "positive"}
