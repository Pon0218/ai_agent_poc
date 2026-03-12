from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Any


class SessionStatus(str, Enum):
    CREATED = "created"
    QUESTIONS_GENERATED = "questions_generated"
    ANSWERS_SUBMITTED = "answers_submitted"
    REPORT_GENERATED = "report_generated"
    FAILED = "failed"


@dataclass
class QuestionRecord:
    question_id: str
    question_text: str
    question_type: str
    required: bool = True
    options: Optional[List[str]] = None


@dataclass
class AnswerRecord:
    question_id: str
    answer_text: str


@dataclass
class ReportRecord:
    summary: str
    market_analysis: str
    strengths: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)


@dataclass
class SessionRecord:
    session_id: str
    product_name: str
    website_url: Optional[str]
    product_description: Optional[str]
    status: SessionStatus = SessionStatus.CREATED
    product_summary: Optional[str] = None
    questions: List[QuestionRecord] = field(default_factory=list)
    answers: List[AnswerRecord] = field(default_factory=list)
    report: Optional[ReportRecord] = None
    # 可附加額外欄位（例如 trace id、meta 資訊）
    metadata: Dict[str, Any] = field(default_factory=dict)


class InMemoryStore:
    """
    簡單的 in-memory 資料儲存。

    - 實作為單一進程、單執行緒情境下的 MVP 用途
    - 若之後要換成資料庫，只要更換這一層的實作即可
    """

    def __init__(self) -> None:
        self._sessions: Dict[str, SessionRecord] = {}
        self._session_counter: int = 0

    # ---- Session 相關操作 ----

    def generate_session_id(self) -> str:
        self._session_counter += 1
        return f"sess_{self._session_counter:06d}"

    def save_session(self, session: SessionRecord) -> None:
        self._sessions[session.session_id] = session

    def get_session(self, session_id: str) -> Optional[SessionRecord]:
        return self._sessions.get(session_id)

    def update_session(self, session: SessionRecord) -> None:
        self._sessions[session.session_id] = session


# 單一全域實例，供 services 使用
memory_store = InMemoryStore()

