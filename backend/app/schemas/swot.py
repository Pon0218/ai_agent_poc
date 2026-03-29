from pydantic import BaseModel

from .common import SessionStatusEnum


class SWOTGenerateResponse(BaseModel):
    """簡化流程：依 session 產品資訊由 LLM 一次產出 SWOT 分析，回傳 Markdown。"""

    session_id: str
    status: SessionStatusEnum
    swot_markdown: str
