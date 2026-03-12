from __future__ import annotations

from fastapi import HTTPException, status

from ..schemas.common import SessionStatusEnum
from ..schemas.report import ReportGenerateResponse
from ..services.session_service import session_service
from ..services.llm_service import llm_service
from ..storage.memory_store import memory_store, SessionStatus, ReportRecord


class ReportService:
    """
    負責產生分析報告的服務。
    """

    def generate_report(self, session_id: str) -> ReportGenerateResponse:
        """
        根據 Session 內的產品資料與回答生成報告。
        """

        session = session_service.get_session_or_404(session_id)

        if session.status not in {
            SessionStatus.ANSWERS_SUBMITTED,
            SessionStatus.REPORT_GENERATED,
        }:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="目前狀態不允許產生報告，請先提交回答",
            )

        report_content = llm_service.generate_report(session)

        # 將報告寫回 Session（轉成 storage 層的 ReportRecord）
        session.report = ReportRecord(
            summary=report_content.summary,
            market_analysis=report_content.market_analysis,
            strengths=report_content.strengths,
            risks=report_content.risks,
            suggestions=report_content.suggestions,
        )
        session.status = SessionStatus.REPORT_GENERATED
        memory_store.update_session(session)

        return ReportGenerateResponse(
            session_id=session_id,
            status=SessionStatusEnum.report_generated,
            report=report_content,
        )


report_service = ReportService()

