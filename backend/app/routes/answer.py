from fastapi import APIRouter, Path

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
    payload: AnswerSubmitRequest | None = None,
) -> BaseAPIResponse:
    """
    接收使用者對追問問題的回答，儲存至 Session 中。
    """

    # FastAPI 會保證 payload 存在（由 Pydantic 驗證），這裡加上型別保護
    if payload is None:
        payload = AnswerSubmitRequest(answers=[])

    result = answer_service.submit_answers(session_id, payload)
    return BaseAPIResponse(
        success=True,
        data=result.dict(),
    )

