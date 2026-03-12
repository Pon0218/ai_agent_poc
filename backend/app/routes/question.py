from fastapi import APIRouter, Path

from ..schemas.common import BaseAPIResponse
from ..services.question_service import question_service


router = APIRouter(prefix="/sessions", tags=["questions"])


@router.post(
    "/{session_id}/questions/generate",
    response_model=BaseAPIResponse,
)
async def generate_questions(
    session_id: str = Path(..., description="分析任務 session ID"),
) -> BaseAPIResponse:
    """
    根據 Session 內的產品資料產生摘要與追問問題列表。
    目前使用 mock LLM 實作。
    """

    result = question_service.generate_questions(session_id)
    return BaseAPIResponse(
        success=True,
        data=result.dict(),
    )

