
from pydantic import BaseModel

class PostRequest(BaseModel):
    platform: str
    post_text: str
