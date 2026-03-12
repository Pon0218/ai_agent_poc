from typing import Optional, List

from pydantic import BaseModel, AnyHttpUrl, Field

from .common import SessionStatusEnum, QuestionSchema, AnswerSchema


class SessionCreateRequest(BaseModel):
    """
    建立分析任務所需的產品基本資訊。
    """

    product_name: str = Field(..., description="產品名稱")
    website_url: Optional[AnyHttpUrl] = Field(
        None, description="產品網站網址（選填）"
    )
    product_description: Optional[str] = Field(
        None, description="產品描述（可為行銷文案或功能說明）"
    )


class SessionCreateResponse(BaseModel):
    session_id: str
    status: SessionStatusEnum
    message: str


class SessionDetail(BaseModel):
    """
    供內部或除錯用的 Session 全貌資料結構。
    目前 API 不直接提供，但預留未來擴充空間。
    """

    session_id: str
    product_name: str
    website_url: Optional[AnyHttpUrl]
    product_description: Optional[str]
    status: SessionStatusEnum
    product_summary: Optional[str] = None
    questions: List[QuestionSchema] = []
    answers: List[AnswerSchema] = []

