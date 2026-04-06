from __future__ import annotations

from openai import OpenAI

from ..core.config import get_settings
from ..storage.memory_store import SessionRecord


class LLMService:
    """
    負責與 LLM 溝通；目前 SWOT 使用 OpenAI Chat Completions。
    """

    def generate_swot(self, session: SessionRecord) -> str:
        """
        依 session 內的產品名稱、網址、敘述，呼叫 LLM 一次產出 SWOT 分析（Markdown）。
        使用 .env 中的 OPENAI_API_KEY；若未設定則拋出 ValueError。
        """
        settings = get_settings()
        if not settings.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY 未設定，請在 .env 中設定後再試")

        product_info = f"""
產品名稱：{session.product_name}
產品網址：{session.website_url or "未提供"}
產品敘述：{session.product_description or "未提供"}
""".strip()

        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "你是一位商業分析師。請僅根據使用者提供的產品資訊，產出一份 SWOT 分析，以 Markdown 格式回傳。結構需包含：## Strengths、## Weaknesses、## Opportunities、## Threats，每個標題下用條列或短段落說明，內容簡潔、可直接用於報告。不要輸出多餘前言或結尾。",
                },
                {
                    "role": "user",
                    "content": f"請針對以下產品產出 SWOT 分析（Markdown）：\n\n{product_info}",
                },
            ],
            temperature=0.3,
        )
        content = response.choices[0].message.content
        return content.strip() if content else "# SWOT 分析\n\n（未取得內容）"


llm_service = LLMService()
