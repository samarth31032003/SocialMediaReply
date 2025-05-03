import os
import datetime
from transformers import pipeline
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus
import certifi
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Load .env variables
load_dotenv()

# Hugging Face Pipelines
reply_generator = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")
sentiment_analyzer = pipeline("sentiment-analysis")
zero_shot_classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

# MongoDB connection
db_user = "Samarthvekariya"
db_password = quote_plus(os.getenv("DB_PASSWORD", "Samarth@31"))
mongo_uri = f"mongodb+srv://{db_user}:{db_password}@cluster0.m7pl9yh.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(mongo_uri, tls=True, tlsCAFile=certifi.where())
    db = client["reply_generator"]
    collection = db["post_replies"]
    print("✅ MongoDB connected!")
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")
    raise

# FastAPI App
app = FastAPI(title="Human-like Reply Generator API 🚀")

# Request model
class PostRequest(BaseModel):
    platform: str
    post_text: str

# Tone detection
def detect_tone(text: str) -> str:
    sentiment = sentiment_analyzer(text)[0]['label']
    return sentiment

# Intent classification
def detect_intent(text: str) -> str:
    labels = ["informative", "promotional", "question", "opinion"]
    result = zero_shot_classifier(sequences=text, candidate_labels=labels)
    return result['labels'][0]  # Best match

# Reply Generation
def generate_reply(platform: str, post_text: str) -> str:
    tone = detect_tone(post_text)
    intent = detect_intent(post_text)

    prompt = (
        f"Platform: {platform}\n"
        f"Tone: {tone}\n"
        f"Intent: {intent}\n"
        f"Post: {post_text}\n"
        f"Reply (write like a real human user on {platform} matching tone and context):"
    )

    response = reply_generator(prompt, max_new_tokens=100)[0]['generated_text']
    return response.strip()

# API Endpoint (renamed handler)
@app.post("/reply")
def generate_reply_api(request: PostRequest):
    try:
        reply = generate_reply_text(request.platform, request.post_text)

        # Store in DB
        record = {
            "platform": request.platform,
            "post_text": request.post_text,
            "generated_reply": reply,
            "timestamp": datetime.datetime.utcnow()
        }
        collection.insert_one(record)
        return {"generated_reply": reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Uvicorn Runner (for local testing)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
