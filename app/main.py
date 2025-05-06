from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os

app = FastAPI()

# Load model and vectorizer
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
vectorizer_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
except Exception as e:
    model = None
    vectorizer = None
    import traceback
    print("Failed to load model:")
    traceback.print_exc()


# Request schema
class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Sentiment Analyzer API is running"}

@app.post("/predict")
def predict_sentiment(data: TextInput):
    if not model or not vectorizer:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    text_vector = vectorizer.transform([data.text])
    prediction = model.predict(text_vector)[0]
    return {"input": data.text, "sentiment": prediction}
