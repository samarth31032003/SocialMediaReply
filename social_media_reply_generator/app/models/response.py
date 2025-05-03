
from pydantic import BaseModel

class ReplyResponse(BaseModel):
    generated_reply: str
