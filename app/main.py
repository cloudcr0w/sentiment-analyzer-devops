from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel
import joblib
import os
import time
import logging
from collections import defaultdict

app = FastAPI()

# ===== Security Config =====
API_KEY = "supersecrettoken"
RATE_LIMIT = 5  # max 5 reqs
TIME_WINDOW = 60  # seconds

rate_limit_cache = defaultdict(list)

# ===== Logging Setup =====
logging.basicConfig(filename="security.log", level=logging.INFO)

# ===== Security Dependencies =====
def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if token != f"Bearer {API_KEY}":
        logging.warning(f"Unauthorized access attempt from {request.client.host}")
        raise HTTPException(status_code=403, detail="Unauthorized")

def rate_limiter(request: Request):
    ip = request.client.host
    now = time.time()
    requests = rate_limit_cache[ip]

    # keep only requests within TIME_WINDOW
    rate_limit_cache[ip] = [t for t in requests if now - t < TIME_WINDOW]

    if len(rate_limit_cache[ip]) >= RATE_LIMIT:
        logging.warning(f"Rate limit exceeded for {ip}")
        raise HTTPException(status_code=429, detail="Too Many Requests")

    rate_limit_cache[ip].append(now)

# ===== ML Model Loading =====
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
vectorizer_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
except Exception:
    model = None
    vectorizer = None
    import traceback
    print("Failed to load model:")
    traceback.print_exc()

# ===== Data Schema =====
class TextInput(BaseModel):
    text: str

# ===== Endpoints =====
@app.get("/")
def read_root():
    return {"message": "Sentiment Analyzer API is running"}

@app.post("/predict")
def predict_sentiment(
    data: TextInput,
    _: None = Depends(verify_token),
    __: None = Depends(rate_limiter)
):
    if not model or not vectorizer:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    text_vector = vectorizer.transform([data.text])
    prediction = model.predict(text_vector)[0]
    return {"input": data.text, "sentiment": prediction}

@app.get("/health")
def health_check():
    """Health check endpoint – returns basic service status"""
    return {"status": "ok"}
