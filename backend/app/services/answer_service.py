from __future__ import annotations

from fastapi import HTTPException, status

from ..schemas.answer import AnswerSubmitRequest, AnswerSubmitResponse
from ..schemas.common import SessionStatusEnum
from ..services.session_service import session_service
from ..storage.memory_store import memory_store, AnswerRecord, SessionStatus


class AnswerService:
    """
    負責接收並儲存使用者回答的服務。
    """

    def submit_answers(
        self, session_id: str, payload: AnswerSubmitRequest
    ) -> AnswerSubmitResponse:
        """
        接收前端送來的回答列表，寫入 Session。
        """

        session = session_service.get_session_or_404(session_id)

        if session.status not in {
            SessionStatus.QUESTIONS_GENERATED,
            SessionStatus.ANSWERS_SUBMITTED,
        }:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="目前狀態不允許提交回答，請先產生問題",
            )

        # 簡單覆蓋所有回答，實務上可考慮 append 或版本控制
        session.answers = [
            AnswerRecord(
                question_id=a.question_id,
                answer_text=a.answer_text,
            )
            for a in payload.answers
        ]

        session.status = SessionStatus.ANSWERS_SUBMITTED
        memory_store.update_session(session)

        return AnswerSubmitResponse(
            session_id=session_id,
            status=SessionStatusEnum.answers_submitted,
            message="回答已儲存",
        )


answer_service = AnswerService()

