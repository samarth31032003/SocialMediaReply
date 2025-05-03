 Human-like Social Media Reply Generator

Generates human-like replies for Twitter, LinkedIn, and Instagram posts using AI. Built with FastAPI + Hugging Face Transformers + MongoDB + Docker.

🚀 Features

🤖 LLM-powered, context-aware reply generator

🎯 Matches tone & style per platform (Twitter, LinkedIn, Instagram)

⚡ FastAPI REST API (/reply endpoint)

💾 Stores every post-reply in MongoDB Atlas

🧪 Pytest-based testing suite

🐳 Docker & Docker Compose support

📦 Setup & Installation

1. Clone the repo

git clone https://github.com/yourusername/social_media_reply_generator.git
cd social_media_reply_generator

2. Run using Docker Compose (Recommended)

docker-compose up --build

This will spin up:

FastAPI API on http://localhost:8000

MongoDB container

3. (Optional) Run locally without Docker

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

📚 API Usage Example

POST /reply

curl -X POST "http://localhost:8000/reply" \
     -H "Content-Type: application/json" \
     -d '{
          "platform": "Twitter",
          "post_text": "Just reached 10K followers! 🎉"
        }'

Sample Response

{
  "generated_reply": "Congratulations on hitting 10K! Well deserved! 🚀"
}

🛠️ Tech Stack

FastAPI (API Framework)

Hugging Face Transformers (LLMs)

MongoDB Atlas (Database)

Pydantic (Validation)

Pytest (Testing)

Docker & Docker Compose (Containerization)

🏗️ Architecture

User → FastAPI REST API → Huggingface LLM Pipeline → Reply
                         ↓
                    MongoDB (Stores post-reply pairs)

💡 Approach & Decisions

Prompt Chaining: Uses platform detection → sentiment analysis → reply generation for authentic replies.

Tone Matching: Platform-specific style rules applied (e.g., casual for Twitter, formal for LinkedIn).

MongoDB Atlas: Chosen for easy cloud-hosted, scalable storage.

Docker: Ensures smooth cross-platform deployment.

✅ Tests

pytest

📄 License

MIT

👨‍💻 Author

Samarth Vekariya