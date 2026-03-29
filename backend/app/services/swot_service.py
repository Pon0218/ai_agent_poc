from __future__ import annotations

from fastapi import HTTPException, status

from ..schemas.common import SessionStatusEnum
from ..schemas.swot import SWOTGenerateResponse
from ..services.session_service import session_service
from ..services.llm_service import llm_service
from ..storage.memory_store import memory_store, SessionStatus


class SWOTService:
    """
    簡化流程：依 session 的產品資訊呼叫 LLM，一次產出 SWOT 分析（Markdown）。
    """

    def generate_swot(self, session_id: str) -> SWOTGenerateResponse:
        """
        取得 session → 呼叫 LLM 產生 SWOT Markdown → 寫回 session 並回傳。
        """
        session = session_service.get_session_or_404(session_id)

        # 允許 created 或已產生過 swot 的 session 再產生一次
        if session.status not in {
            SessionStatus.CREATED,
            SessionStatus.SWOT_GENERATED,
        }:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="此 session 已進入問答流程，請另建新 session 使用 SWOT 簡化流程",
            )

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
