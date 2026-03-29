from fastapi import APIRouter, Path

from ..schemas.common import BaseAPIResponse
from ..services.swot_service import swot_service


router = APIRouter(prefix="/sessions", tags=["swot"])


@router.post(
    "/{session_id}/swot/generate",
    response_model=BaseAPIResponse,
)
async def generate_swot(
    session_id: str = Path(..., description="分析任務 session ID"),
) -> BaseAPIResponse:
    """
    簡化流程：依 session 的產品名稱、網址、敘述，呼叫 LLM 一次產出 SWOT 分析，回傳 Markdown。
    需先在 POST /sessions 建立 session 並填入產品資訊。
    """
    result = swot_service.generate_swot(session_id)
    return BaseAPIResponse(
        success=True,
        data=result.model_dump(),
    )
