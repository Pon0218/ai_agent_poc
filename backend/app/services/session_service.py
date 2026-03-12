from __future__ import annotations

from fastapi import HTTPException, status

from ..schemas.session import SessionCreateRequest, SessionCreateResponse
from ..schemas.common import SessionStatusEnum
from ..storage.memory_store import (
    memory_store,
    SessionRecord,
    SessionStatus,
)


class SessionService:
    """
    負責處理分析任務 Session 生命週期的商業邏輯。
    """

    def create_session(self, payload: SessionCreateRequest) -> SessionCreateResponse:
        """
        建立一筆新的分析任務 Session，並儲存在 in-memory store。
        """

        session_id = memory_store.generate_session_id()
        record = SessionRecord(
            session_id=session_id,
            product_name=payload.product_name,
            website_url=str(payload.website_url) if payload.website_url else None,
            product_description=payload.product_description,
        )

        memory_store.save_session(record)

        return SessionCreateResponse(
            session_id=session_id,
            status=SessionStatusEnum.created,
            message="分析任務已建立",
        )

    def get_session_or_404(self, session_id: str) -> SessionRecord:
        """
        取得 Session；若不存在則回傳 404。
        """

        session = memory_store.get_session(session_id)
        if not session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Session {session_id} 不存在",
            )
        return session

    def update_status(self, session_id: str, new_status: SessionStatus) -> None:
        """
        更新 Session 狀態，若找不到會回 404。
        """

        session = self.get_session_or_404(session_id)
        session.status = new_status
        memory_store.update_session(session)


session_service = SessionService()

