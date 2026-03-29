from fastapi import APIRouter, Path

from ..schemas.common import BaseAPIResponse
from ..services.report_service import report_service


router = APIRouter(prefix="/sessions", tags=["report"])


@router.post(
    "/{session_id}/report/generate",
    response_model=BaseAPIResponse,
)
async def generate_report(
    session_id: str = Path(..., description="分析任務 session ID"),
) -> BaseAPIResponse:
    """
    根據產品原始資料 + 問題 + 回答產生結構化報告。
    """

    result = report_service.generate_report(session_id)
    return BaseAPIResponse(
        success=True,
        data=result.model_dump(),
    )

