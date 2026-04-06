from __future__ import annotations

from fastapi import HTTPException, status

from ..schemas.common import SessionStatusEnum
from ..schemas.swot import SWOTGenerateResponse
from ..services.session_service import session_service
from ..services.llm_service import llm_service
from ..storage.memory_store import memory_store, SessionStatus


class SWOTService:
    """依 session 的產品資訊呼叫 LLM，一次產出 SWOT（Markdown）。"""

    def generate_swot(self, session_id: str) -> SWOTGenerateResponse:
        session = session_service.get_session_or_404(session_id)

        try:
            swot_markdown = llm_service.generate_swot(session)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=str(e),
            ) from e
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=f"LLM 呼叫失敗：{e!s}",
            ) from e

        session.swot_markdown = swot_markdown
        session.status = SessionStatus.SWOT_GENERATED
        memory_store.update_session(session)

        return SWOTGenerateResponse(
            session_id=session_id,
            status=SessionStatusEnum.swot_generated,
            swot_markdown=swot_markdown,
        )


swot_service = SWOTService()
