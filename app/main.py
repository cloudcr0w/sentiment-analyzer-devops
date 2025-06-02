from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import os
import time
import logging
from collections import defaultdict
# from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
# Instrumentator().instrument(app).expose(app)

# === CORS configuration ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],  # leave empty to block all external origins (adjust when frontend is added)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Security settings ===
API_KEY = os.getenv("API_KEY", "supersecrettoken")
RATE_LIMIT = 5         # max number of requests
TIME_WINDOW = 60       # time window in seconds

rate_limit_cache = defaultdict(list)

# === Logging setup ===
logging.basicConfig(
    filename="security.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# === Token verification ===
def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if token != f"Bearer {API_KEY}":
        logging.warning(f"Unauthorized request from IP {request.client.host}")
        raise HTTPException(status_code=403, detail="Unauthorized")

# === Basic IP rate limiter ===
def rate_limiter(request: Request):
    ip = request.client.host
    now = time.time()
    recent = [t for t in rate_limit_cache[ip] if now - t < TIME_WINDOW]
    rate_limit_cache[ip] = recent

    if len(recent) >= RATE_LIMIT:
        logging.warning(f"Rate limit exceeded for IP {ip}")
        raise HTTPException(status_code=429, detail="Too Many Requests")

    rate_limit_cache[ip].append(now)

# === Load ML model and vectorizer ===
try:
    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    vectorizer_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
except Exception as e:
    print("Failed to load model:", e)
    model = None
    vectorizer = None

# === Input schema with validation ===
class TextInput(BaseModel):
    text: str = Field(..., min_length=3, description="Text must be at least 3 characters long")

# === API Endpoints ===
@app.get("/")
def root():
    return {"message": "Sentiment Analyzer API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}

@app.post("/predict")
def predict(
    data: TextInput,
    _: None = Depends(verify_token),
    __: None = Depends(rate_limiter)
):
    if not model or not vectorizer:
        raise HTTPException(status_code=500, detail="Model not loaded")

    text_vector = vectorizer.transform([data.text])
    prediction = model.predict(text_vector)[0]
    return {"input": data.text, "sentiment": prediction}

@app.get("/logs")
def get_logs():
    try:
        with open("security.log", "r") as f:
            lines = f.readlines()
            return {"logs": lines[-10:]}  # it gives last 10 lines 
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Log file not found")
