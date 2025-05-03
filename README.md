🤖 Human-like Social Media Reply Generator

An AI-powered system that generates authentic, human-like replies for Twitter, LinkedIn, and Instagram posts.

Built with FastAPI, Hugging Face Transformers, and MongoDB Atlas. Fully tested, Dockerized, and ready for production.



🚀 Features

* Context-aware, natural language replies
* Tone & style adapted for each platform
* REST API with FastAPI (/reply endpoint)
* Request-response logging in MongoDB
* Dockerized for seamless deployment
* Automated tests with Pytest



📦 Setup & Installation

1. Clone the Repository


git clone https://github.com/yourusername/social_media_reply_generator.git
cd social_media_reply_generator


2. Install Dependencies


python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


3. Run the API


uvicorn app.main:app --reload


Access API docs: [http://localhost:8000/docs](http://localhost:8000/docs)



🐳 Run with Docker

1. Build Docker Image


docker build -t social-media-reply-generator .


2. Run Docker Container


docker run -d -p 8000:8000 social-media-reply-generator




📚 API Usage

POST /reply

Request Example:


{
  "platform": "Twitter",
  "post_text": "Excited to attend PyCon 2025!"
}


Response Example:


{
  "generated_reply": "That sounds amazing! Can't wait to hear about your experience at PyCon 2025! 🐍🎉"
}


Explore interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)



🧠 Approach: Human-like Reply Generation

Techniques:

* Prompt Chaining → Detect tone → Analyze intent → Generate reply
* Platform Style Matching:

  * Twitter: Short, witty, emoji-friendly
  * LinkedIn: Professional, encouraging
  * Instagram: Casual, emoji-rich
* AI Giveaway Avoidance: Avoids repetitive, formal, and generic outputs



🏗️ Architecture & Decisions

| Component        | Decision                  | Why                             |
| ---------------- | ------------------------- | ------------------------------- |
| API Framework    | FastAPI                   | Async, OpenAPI-ready, modern    |
| LLM Engine       | Hugging Face Transformers | Free-tier, flexible prompting   |
| Database         | MongoDB Atlas             | Scalable, flexible schema       |
| Containerization | Docker                    | Portable, consistent deployment |

Trade-offs:

* Hugging Face free-tier models (good, but lighter than GPT-4)
* Chose NoSQL (MongoDB) for flexibility over structured SQL

---

🧪 Running Tests

Run all tests with:

pytest


Tests cover API endpoints and response validation.



📂 Project Structure


social_media_reply_generator/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── utils.py
├── tests/
│   └── test_main.py
├── posts.xlsx
├── Dockerfile
├── requirements.txt
└── README.md




🛠️ Tech Stack

* Python 3.8+
* FastAPI
* Hugging Face Transformers
* MongoDB Atlas
* Docker
* Pytest

---

📄 License

MIT License © 2025 Samarth Vekariya
