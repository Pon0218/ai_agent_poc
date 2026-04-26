# ai_agent_poc

## 本地開發啟動

### 1. 建立後端環境變數

在 `backend/` 目錄下建立 `.env` 檔：

```bash
cp backend/.env.example backend/.env   # 若有範本
# 或直接建立
touch backend/.env
```

`.env` 內容範例：

```env
OPENAI_API_KEY=sk-...
```

> `OPENAI_API_KEY` 為呼叫 LLM 必填。`APP_ENV`、`DEBUG` 等選填，不填會使用預設值。

### 2. 啟動前後端

```bash
docker compose up --build
```

| 服務 | 網址 |
|------|------|
| 前端 | http://localhost:5173 |
| 後端 API | http://localhost:8000 |
| 後端 API Docs | http://localhost:8000/docs |
