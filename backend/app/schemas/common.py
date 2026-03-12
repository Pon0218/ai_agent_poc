from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class SessionStatusEnum(str, Enum):
    created = "created"
    questions_generated = "questions_generated"
    answers_submitted = "answers_submitted"
    report_generated = "report_generated"
    failed = "failed"


class QuestionTypeEnum(str, Enum):
    text = "text"
    single_select = "single_select"
    multi_select = "multi_select"


class APIResponseMeta(BaseModel):
    """
    通用回應中可附帶的 meta 資訊。
    目前僅示意用，之後可以加入 trace_id、耗時等欄位。
    """

    message: Optional[str] = None


class BaseAPIResponse(BaseModel):
    """
    統一 API 回傳格式的基底模型。
    - success: 是否成功
    - data: 實際 payload
    - error: 若失敗時的錯誤描述（簡單字串即可，詳細錯誤留在 log）
    - meta: 額外資訊
    """

    success: bool = True
    data: dict
    error: Optional[str] = None
    meta: Optional[APIResponseMeta] = None


class QuestionSchema(BaseModel):
    question_id: str
    question_text: str
    question_type: QuestionTypeEnum
    required: bool = True
    options: Optional[List[str]] = None


class AnswerSchema(BaseModel):
    question_id: str
    answer_text: str

