import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    全域設定與環境變數載入。
    之後若要加入真實 LLM API key、資料庫連線等，可以直接擴充這個設定類別。
    """

    APP_NAME: str = "AI Agent Workflow API"
    APP_ENV: str = os.getenv("APP_ENV", "local")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    # 預留給未來的 LLM 設定欄位
    OPENAI_API_KEY: str | None = None
    LLM_PROVIDER: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """
    使用 lru_cache 確保設定只建立一次，避免重複讀取環境變數。
    """

    return Settings()

