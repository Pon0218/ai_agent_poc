from __future__ import annotations

from fastapi import HTTPException, status

from ..schemas.common import SessionStatusEnum, QuestionSchema
from ..schemas.question import QuestionGenerationResponse
from ..services.session_service import session_service
from ..services.llm_service import llm_service
from ..storage.memory_store import memory_store, SessionStatus, QuestionRecord


class QuestionService:
    """
    負責處理「產生追問問題」的流程。
    """

    def generate_questions(
        self, session_id: str
    ) -> QuestionGenerationResponse:
        """
        根據 Session 內的產品資訊產生摘要與追問問題列表。
        實際產生邏輯由 LLMService 負責，這裡只做流程控制與狀態更新。
        """

        session = session_service.get_session_or_404(session_id)

        if session.status not in {
            SessionStatus.CREATED,
            SessionStatus.QUESTIONS_GENERATED,
        }:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="目前狀態不允許重新產生問題",
            )

        product_summary, questions = llm_service.summarize_product_and_generate_questions(
            session
        )

        # 將問題與摘要寫回 session（轉為 storage 層的 QuestionRecord）
        session.product_summary = product_summary
        session.questions = [
            QuestionRecord(
                question_id=q.question_id,
                question_text=q.question_text,
                question_type=q.question_type.value,
                required=q.required,
                options=q.options,
            )
            for q in questions
        ]

        session.status = SessionStatus.QUESTIONS_GENERATED
        memory_store.update_session(session)

        return QuestionGenerationResponse(
            session_id=session_id,
            status=SessionStatusEnum.questions_generated,
            product_summary=product_summary,
            questions=[
                QuestionSchema(
                    question_id=q.question_id,
                    question_text=q.question_text,
                    question_type=q.question_type,  # type: ignore[arg-type]
                    required=q.required,
                    options=q.options,
                )
                for q in questions
            ],
        )


question_service = QuestionService()

