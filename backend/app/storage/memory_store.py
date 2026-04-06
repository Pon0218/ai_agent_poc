from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional


class SessionStatus(str, Enum):
    CREATED = "created"
    SWOT_GENERATED = "swot_generated"


@dataclass
class SessionRecord:
    session_id: str
    product_name: str
    website_url: Optional[str]
    product_description: Optional[str]
    status: SessionStatus = SessionStatus.CREATED
    swot_markdown: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


class InMemoryStore:
    """
    簡單的 in-memory 資料儲存。
    若之後要換成資料庫，只要更換這一層的實作即可。
    """

    def __init__(self) -> None:
        self._sessions: Dict[str, SessionRecord] = {}
        self._session_counter: int = 0

    def generate_session_id(self) -> str:
        self._session_counter += 1
        return f"sess_{self._session_counter:06d}"

    def save_session(self, session: SessionRecord) -> None:
        self._sessions[session.session_id] = session

    def get_session(self, session_id: str) -> Optional[SessionRecord]:
        return self._sessions.get(session_id)

    def update_session(self, session: SessionRecord) -> None:
        self._sessions[session.session_id] = session


memory_store = InMemoryStore()
