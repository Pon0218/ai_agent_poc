from typing import Optional

from pydantic import BaseModel, AnyHttpUrl, Field

from .common import SessionStatusEnum


class SessionCreateRequest(BaseModel):
    """建立分析任務所需的產品基本資訊。"""

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
