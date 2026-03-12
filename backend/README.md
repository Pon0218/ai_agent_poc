## AI Agent Workflow Backend (FastAPI)

本專案是一個使用 **FastAPI** 實作的後端服務，提供「workflow 型 AI Agent」的 MVP 版本。
目前所有 AI 行為皆為 **mock**，未實際呼叫 LLM，但已預留 `llm_service` 方便日後接上 OpenAI 或其他模型。

---

### 專案功能簡述

- **建立分析任務 Session**：接收產品資訊並建立一筆分析任務。
- **產生追問問題**：依產品資訊產生產品摘要與一組追問問題（目前為 mock）。
- **接收使用者回答**：儲存使用者針對問題的回答。
- **產出結構化報告**：根據原始產品資料與使用者回答，產生一份結構化報告（目前為 mock）。
- **Health Check**：簡單回傳服務狀態。

---

### 專案結構

```text
backend/
  app/
    main.py                  # FastAPI 入口，註冊所有 router
    routes/
      health.py              # 健康檢查 API
      session.py             # 建立分析任務 Session 的 API
      question.py            # 產生追問問題的 API
      answer.py              # 接收回答的 API
      report.py              # 產生報告的 API
    schemas/
      session.py             # Session 相關 Pydantic 模型
      question.py            # 問題產生回應模型
      answer.py              # 回答提交請求/回應模型
      report.py              # 報告回應模型
      common.py              # 共用枚舉、通用回應格式等
    services/
      session_service.py     # Session 生命週期商業邏輯
      question_service.py    # 問題產生流程
      answer_service.py      # 回答儲存流程
      report_service.py      # 報告產生流程
      llm_service.py         # 預留 LLM 介面，目前為 mock
    core/
      config.py              # 設定與環境變數管理
    storage/
      memory_store.py        # In-memory 存儲實作（Session / 問題 / 回答 / 報告）
  requirements.txt
  .env.example
  README.md
```

---

### 安裝方式

1. 進入專案目錄

```bash
cd backend
```

2. 建議建立並啟用虛擬環境（可選）

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. 安裝相依套件

```bash
pip install -r requirements.txt
```

4. 建立環境設定檔

```bash
copy .env.example .env  # Windows PowerShell 可用：Copy-Item .env.example .env
```

---

### 啟動方式

在 `backend` 目錄下執行：

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

啟動後預設服務位於：

- API 根路徑：`http://localhost:8000`
- OpenAPI 文件：`http://localhost:8000/docs`

---

### API 概觀與回應格式

除了 `GET /health` 以外，主要業務 API 皆採用統一回傳格式：

```json
{
  "success": true,
  "data": { ...實際 payload... },
  "error": null,
  "meta": {
    "message": "optional message"
  }
}
```

若發生錯誤（例如 Session 不存在），則會回傳 FastAPI 的預設錯誤結構，例如：

```json
{
  "detail": "Session sess_000001 不存在"
}
```

---

### API 詳細說明與測試方式

以下範例皆以 `http://localhost:8000` 為基底網址，可使用：
- `curl`
- Postman
- Insomnia
- 或直接在 `http://localhost:8000/docs` 透過 Swagger UI 測試。

#### 1. Health Check

- **Method**: `GET`
- **URL**: `/health`

**範例回應**

```json
{
  "status": "ok"
}
```

---

#### 2. 建立分析任務 Session

- **Method**: `POST`
- **URL**: `/sessions`

**Request Body 範例**

```json
{
  "product_name": "智慧寵物餵食器",
  "website_url": "https://example.com",
  "product_description": "可透過手機 App 遠端控制，支援定時餵食、攝影監控、語音互動"
}
```

**成功回應範例**

```json
{
  "success": true,
  "data": {
    "session_id": "sess_000001",
    "status": "created",
    "message": "分析任務已建立"
  },
  "error": null,
  "meta": null
}
```

---

#### 3. 產生追問問題

- **Method**: `POST`
- **URL**: `/sessions/{session_id}/questions/generate`

**成功回應範例**

```json
{
  "success": true,
  "data": {
    "session_id": "sess_000001",
    "status": "questions_generated",
    "product_summary": "此產品為智慧設備，主打遠端控制與監控功能。",
    "questions": [
      {
        "question_id": "q_001",
        "question_text": "目前主要銷售市場是哪裡？",
        "question_type": "text",
        "required": true
      },
      {
        "question_id": "q_002",
        "question_text": "產品售價區間大約是多少？",
        "question_type": "text",
        "required": true
      },
      {
        "question_id": "q_003",
        "question_text": "目標客群是 B2B 還是 B2C？",
        "question_type": "single_select",
        "required": true,
        "options": ["B2B", "B2C", "Both"]
      }
    ]
  },
  "error": null,
  "meta": null
}
```

若 `session_id` 不存在，會回傳 404：

```json
{
  "detail": "Session sess_xxx 不存在"
}
```

---

#### 4. 提交回答

- **Method**: `POST`
- **URL**: `/sessions/{session_id}/answers`

**Request Body 範例**

```json
{
  "answers": [
    {
      "question_id": "q_001",
      "answer_text": "台灣、日本、美國"
    },
    {
      "question_id": "q_002",
      "answer_text": "120-150 USD"
    },
    {
      "question_id": "q_003",
      "answer_text": "B2C"
    }
  ]
}
```

**成功回應範例**

```json
{
  "success": true,
  "data": {
    "session_id": "sess_000001",
    "status": "answers_submitted",
    "message": "回答已儲存"
  },
  "error": null,
  "meta": null
}
```

若尚未產生問題就提交回答，會得到 400：

```json
{
  "detail": "目前狀態不允許提交回答，請先產生問題"
}
```

---

#### 5. 產生報告

- **Method**: `POST`
- **URL**: `/sessions/{session_id}/report/generate`

**成功回應範例**

```json
{
  "success": true,
  "data": {
    "session_id": "sess_000001",
    "status": "report_generated",
    "report": {
      "summary": "本產品屬於智慧設備，具備遠端控制與監控功能。",
      "market_analysis": "主要目標市場包含：台灣、日本、美國。在這些地區，智慧裝置與寵物相關產品的接受度逐年提升，若搭配適當的在地化行銷，有機會建立差異化定位。",
      "strengths": [
        "具遠端控制與監控功能，提升使用者便利性",
        "目前規劃售價區間為：120-150 USD"
      ],
      "risks": [
        "需確認不同市場的法規與認證要求",
        "市場上可能已有類似智慧設備競品，需強調獨特價值"
      ],
      "suggestions": [
        "優先針對 台灣、日本、美國 進行市場規模與競品分析。",
        "補充競品價格、功能比較，強化產品定位敘事。",
        "針對 B2C 客群調整溝通語氣與行銷素材。"
      ]
    }
  },
  "error": null,
  "meta": null
}
```

若尚未提交回答就產生報告，會得到 400：

```json
{
  "detail": "目前狀態不允許產生報告，請先提交回答"
}
```

---

### 狀態設計補充說明

`Session` 狀態枚舉包含：

- `created`
- `questions_generated`
- `answers_submitted`
- `report_generated`
- `failed`

服務內部會依照呼叫順序自動更新狀態，若在錯誤的狀態下呼叫 API，會回傳 400 並附上錯誤描述。

---

### 後續擴充建議

- 將 `memory_store` 替換為真實資料庫（例如 PostgreSQL / MySQL / MongoDB）。
- 在 `llm_service.py` 中實作實際的 LLM 呼叫（例如 OpenAI Chat Completions）。
- 加入驗證與權限控制（例如 API Key、JWT）。
- 將錯誤與請求記錄到集中式 Log / APM。

# Backend
