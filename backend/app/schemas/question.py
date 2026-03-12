from typing import List, Optional

from pydantic import BaseModel

from .common import SessionStatusEnum, QuestionSchema


class QuestionGenerationResponse(BaseModel):
    """
    產生追問問題的回應結構。
    """

    session_id: str
    status: SessionStatusEnum
    product_summary: str
    questions: List[QuestionSchema]

