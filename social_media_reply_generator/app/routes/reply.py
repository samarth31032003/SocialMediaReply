
from fastapi import APIRouter, HTTPException
from app.models.request import PostRequest
from app.models.response import ReplyResponse
from app.services.generator import generate_reply


router = APIRouter()

@router.post("/reply", response_model=ReplyResponse)
async def get_reply(post_request: PostRequest):
    try:
        # Heavy model calls (sync), so wrap with run_in_threadpool
        from starlette.concurrency import run_in_threadpool
        reply = await run_in_threadpool(
            generate_reply, post_request.platform, post_request.post_text
        )
        return ReplyResponse(generated_reply=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

