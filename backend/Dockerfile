# FastAPI 後端映像
#
# 建置方式（請在 backend 目錄執行，context 必須是 backend/）：
#   cd backend
#   docker build -t ai-agent-backend .
#
# Cloud Run：gcloud run deploy --source ./backend 會自動使用此目錄下的 Dockerfile
#
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

# Cloud Run 注入 PORT 時可覆寫；預設 8080
ENV PORT=8080

EXPOSE 8080

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
