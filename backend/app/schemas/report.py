from typing import List

from pydantic import BaseModel

from .common import SessionStatusEnum


class ReportContent(BaseModel):
    """
    報告內容的結構化格式。
    """

    summary: str
    market_analysis: str
    strengths: List[str]
    risks: List[str]
    suggestions: List[str]


class ReportGenerateResponse(BaseModel):
    session_id: str
    status: SessionStatusEnum
    report: ReportContent

