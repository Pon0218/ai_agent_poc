from fastapi import APIRouter, Body, Path

from ..schemas.answer import AnswerSubmitRequest
from ..schemas.common import BaseAPIResponse
from ..services.answer_service import answer_service


router = APIRouter(prefix="/sessions", tags=["answers"])


@router.post(
    "/{session_id}/answers",
    response_model=BaseAPIResponse,
)
async def submit_answers(
    session_id: str = Path(..., description="分析任務 session ID"),
    payload: AnswerSubmitRequest = Body(..., description="各題回答列表"),
) -> BaseAPIResponse:
    """
    接收使用者對追問問題的回答，儲存至 Session 中。
    Request body 必填，避免漏傳 body 時誤存空回答。
    """

    result = answer_service.submit_answers(session_id, payload)
    return BaseAPIResponse(
        success=True,
        data=result.model_dump(),
    )

