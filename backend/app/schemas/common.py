from enum import Enum
from typing import Optional

from pydantic import BaseModel


class SessionStatusEnum(str, Enum):
    created = "created"
    swot_generated = "swot_generated"


class APIResponseMeta(BaseModel):
    """通用回應中可附帶的 meta 資訊。"""

    message: Optional[str] = None


class BaseAPIResponse(BaseModel):
    """
    統一 API 回傳格式。
    """

    success: bool = True
    data: dict
    error: Optional[str] = None
    meta: Optional[APIResponseMeta] = None
