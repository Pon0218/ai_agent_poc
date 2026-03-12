from fastapi import APIRouter

from ..schemas.common import BaseAPIResponse
from ..schemas.session import SessionCreateRequest
from ..services.session_service import session_service


router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.post("", response_model=BaseAPIResponse)
async def create_session(payload: SessionCreateRequest) -> BaseAPIResponse:
    """
    建立一筆新的分析任務 Session。
    """

    result = session_service.create_session(payload)
    return BaseAPIResponse(
        success=True,
        data=result.dict(),
    )

