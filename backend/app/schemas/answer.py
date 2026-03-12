from typing import List

from pydantic import BaseModel, Field

from .common import AnswerSchema, SessionStatusEnum


class AnswerSubmitRequest(BaseModel):
    """
    使用者提交回答的請求 body。
    """

    answers: List[AnswerSchema] = Field(
        ..., description="針對問題的回答列表"
    )


class AnswerSubmitResponse(BaseModel):
    session_id: str
    status: SessionStatusEnum
    message: str

