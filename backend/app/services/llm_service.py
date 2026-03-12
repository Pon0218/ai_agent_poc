from __future__ import annotations

from typing import List, Tuple

from ..schemas.common import QuestionSchema, QuestionTypeEnum
from ..schemas.report import ReportContent
from ..storage.memory_store import SessionRecord


class LLMService:
    """
    負責與 LLM 溝通的服務層。

    目前為 mock 實作，僅依照產品資訊產生假資料。
    未來若要改為呼叫 OpenAI 或其他 LLM，只要在這個 service 中替換實作即可，
    其他 routes/services 不需要改動。
    """

    def summarize_product_and_generate_questions(
        self, session: SessionRecord
    ) -> Tuple[str, List[QuestionSchema]]:
        """
        根據 Session 內的產品資訊產生：
        - 產品摘要
        - 追問問題列表

        現階段以固定樣板回傳，示意未來的 LLM 行為。
        """

        base_summary = (
            "此產品為智慧設備，主打遠端控制與監控功能。"
        )
        if session.product_description:
            product_summary = (
                f"{base_summary} 產品描述中提到：{session.product_description[:60]}..."
            )
        else:
            product_summary = base_summary

        questions: List[QuestionSchema] = [
            QuestionSchema(
                question_id="q_001",
                question_text="目前主要銷售市場是哪裡？",
                question_type=QuestionTypeEnum.text,
                required=True,
            ),
            QuestionSchema(
                question_id="q_002",
                question_text="產品售價區間大約是多少？",
                question_type=QuestionTypeEnum.text,
                required=True,
            ),
            QuestionSchema(
                question_id="q_003",
                question_text="目標客群是 B2B 還是 B2C？",
                question_type=QuestionTypeEnum.single_select,
                required=True,
                options=["B2B", "B2C", "Both"],
            ),
        ]

        return product_summary, questions

    def generate_report(self, session: SessionRecord) -> ReportContent:
        """
        根據產品原始資料 + 問題 + 回答產生結構化報告。

        目前為固定樣板，會簡單利用已存在的回答文字，示意未來 LLM 可生成更智慧的內容。
        """

        markets_answer = next(
            (a.answer_text for a in session.answers if a.question_id == "q_001"),
            "尚未提供",
        )
        price_answer = next(
            (a.answer_text for a in session.answers if a.question_id == "q_002"),
            "尚未提供",
        )
        segment_answer = next(
            (a.answer_text for a in session.answers if a.question_id == "q_003"),
            "尚未提供",
        )

        summary = (
            "本產品屬於智慧設備，具備遠端控制與監控功能。"
        )
        market_analysis = (
            f"主要目標市場包含：{markets_answer}。"
            "在這些地區，智慧裝置與寵物相關產品的接受度逐年提升，"
            "若搭配適當的在地化行銷，有機會建立差異化定位。"
        )

        strengths = [
            "具遠端控制與監控功能，提升使用者便利性",
            f"目前規劃售價區間為：{price_answer}",
        ]

        risks = [
            "需確認不同市場的法規與認證要求",
            "市場上可能已有類似智慧設備競品，需強調獨特價值",
        ]

        suggestions = [
            f"優先針對 {markets_answer} 進行市場規模與競品分析。",
            "補充競品價格、功能比較，強化產品定位敘事。",
            f"針對 {segment_answer} 客群調整溝通語氣與行銷素材。",
        ]

        return ReportContent(
            summary=summary,
            market_analysis=market_analysis,
            strengths=strengths,
            risks=risks,
            suggestions=suggestions,
        )


# 單一全域實例，供其他 service 呼叫
llm_service = LLMService()

