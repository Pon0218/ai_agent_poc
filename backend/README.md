## AI Agent Backend (FastAPI)

本專案使用 **FastAPI** 實作後端，**目前正式對外流程為兩步驟**：

1. **用戶輸入**：產品名稱、產品網址、產品敘述（建立 Session）
2. **LLM**：依 Session 內產品資訊**一次**產出 **SWOT 分析**，以 **Markdown 字串**回傳

SWOT 會透過 **OpenAI API** 產生，需在 `.env` 設定 `OPENAI_API_KEY`（並於 OpenAI 帳戶啟用計費／額度）。

---

### 專案功能簡述

| 步驟 | 說明 |
|------|------|
| 建立 Session | `POST /sessions` 接收產品名稱、網址、敘述 |
| 產生 SWOT | `POST /sessions/{session_id}/swot/generate` 呼叫 LLM，回傳 `swot_markdown`（Markdown） |
| Health | `GET /health` 檢查服務是否正常 |

---

### 專案結構

```text
backend/
  app/
    main.py                  # FastAPI 入口，註冊所有 router
    routes/
      health.py
      session.py             # POST /sessions
      swot.py                # POST /sessions/{id}/swot/generate
    schemas/
      session.py, swot.py, common.py
    services/
      session_service.py, swot_service.py, llm_service.py
    core/
      config.py              # .env / OPENAI_API_KEY
    storage/
      memory_store.py
  Dockerfile                 # 映像建置（請在 backend 目錄 docker build .）
  requirements.txt
  .env.example
  README.md
```

**Docker**：`Dockerfile` 放在 `backend/` 根目錄，建置時 **working directory 必須是 `backend`**。

- 本機建映像前請先 **啟動 Docker Desktop**（否則會出現 `dockerDesktopLinuxEngine` / 無法連線錯誤）。
- 測試 API 請用 **http://localhost:8000/docs** 或 **http://127.0.0.1:8000**，**勿**在瀏覽器網址列輸入 `0.0.0.0`（會顯示無效位址）。

本機建置並執行（僅本機 tag）：

```bash
cd backend
docker build -t ai-agent-backend .
docker run -p 8080:8080 --rm ai-agent-backend
```

本機建置並推上 **Artifact Registry**（映像檔名與標籤可自訂，範例與常見設定一致）：

```bash
cd backend
gcloud config set project YOUR_PROJECT_ID
gcloud auth configure-docker REGION-docker.pkg.dev

docker build -t REGION-docker.pkg.dev/YOUR_PROJECT_ID/REPOSITORY_NAME/ai_agent_poc:v0.1.0 .
docker push REGION-docker.pkg.dev/YOUR_PROJECT_ID/REPOSITORY_NAME/ai_agent_poc:v0.1.0
```

將 `REGION`（例如 `us-central1`）、`YOUR_PROJECT_ID`、`REPOSITORY_NAME`（Artifact Registry **存放區名稱**，例如 `aiagentpoc`）換成你的值。完整路徑格式為：`區域-docker.pkg.dev/專案ID/存放區/映像檔名稱:標籤`。

**Cloud Run 部署**（擇一）：

1. **從映像檔部署**（已 push 至 Artifact Registry 時）：

   ```bash
   gcloud run deploy YOUR_SERVICE_NAME \
     --image REGION-docker.pkg.dev/YOUR_PROJECT_ID/REPOSITORY_NAME/ai_agent_poc:v0.1.0 \
     --region REGION \
     --allow-unauthenticated \
     --port 8080
   ```

   建議 **Cloud Run 區域** 與 **Artifact Registry 區域** 相同（例如皆為 `us-central1`），並在服務的「變數與密碼」設定 `OPENAI_API_KEY` 等（容器內沒有本機 `.env`）。

2. **從原始碼部署**（由 GCP 在雲端建置）：在 monorepo 根目錄執行  
   `gcloud run deploy ... --source ./backend`（會使用 `backend/Dockerfile`）。

---

### 安裝方式

1. 進入專案目錄

```bash
cd backend
```

2. 安裝相依套件（pip 或 Poetry 擇一）

```bash
pip install -r requirements.txt
# 或
poetry install
```

3. 建立環境設定檔

```bash
copy .env.example .env   # Windows：Copy-Item .env.example .env
```

在 `.env` 填入至少：

```env
OPENAI_API_KEY=你的_OpenAI_API_Key
```

---

### 啟動方式

在 `backend` 目錄下：

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
# 或
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- API：`http://localhost:8000`
- Swagger：`http://localhost:8000/docs`

---

### API 回應格式

除 `GET /health` 外，多數業務 API 使用：

```json
{
  "success": true,
  "data": { },
  "error": null,
  "meta": null
}
```

錯誤時常見為 `{"detail": "..."}`。

---

### 主流程：API 測試（建議照順序）

#### 1. Health Check

- `GET /health` → `{"status":"ok"}`

#### 2. 建立 Session（用戶輸入產品資訊）

- **POST** `/sessions`
- Body：

```json
{
  "product_name": "智慧寵物餵食器",
  "website_url": "https://example.com",
  "product_description": "可透過手機 App 遠端控制，支援定時餵食、攝影監控、語音互動"
}
```

- 回傳中取得 `data.session_id`（例如 `sess_000001`）。

#### 3. 產生 SWOT（Markdown）

- **POST** `/sessions/{session_id}/swot/generate`（**無 request body**）
- 後端會用該 Session 已存的產品資訊呼叫 OpenAI，一次回傳 SWOT。

**成功回應範例**

```json
{
  "success": true,
  "data": {
    "session_id": "sess_000001",
    "status": "swot_generated",
    "swot_markdown": "## Strengths\n- ...\n\n## Weaknesses\n- ...\n\n## Opportunities\n- ...\n\n## Threats\n- ..."
  },
  "error": null,
  "meta": null
}
```

前端將 `data.swot_markdown` 當 Markdown 渲染即可。

- 若 `OPENAI_API_KEY` 未設定或 LLM 失敗，會回傳對應 HTTP 錯誤與 `detail` 說明。

---

### 部署（Cloud Run 等）

- 容器內**沒有**本機 `.env`，請在 Cloud Run **變數與密碼**設定 `OPENAI_API_KEY`（必填 SWOT）、可選 `APP_ENV`、`DEBUG` 等。
- 流程可為：**本機 `docker build` → `docker push` 至 Artifact Registry → Cloud Run 選該映像檔**；或使用上一節的 `gcloud run deploy --source ./backend`。

---

### 後續擴充建議

- 將 `memory_store` 換成資料庫。
- API Key、JWT、Rate limit、集中式 Log。
