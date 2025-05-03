from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.routes import reply

app = FastAPI(title="Human-like Social Media Reply Generator")

app.include_router(reply.router)
