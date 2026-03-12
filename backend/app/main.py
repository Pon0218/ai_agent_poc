from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import get_settings
from .routes import health, session, question, answer, report


def create_app() -> FastAPI:
    """
    建立並回傳 FastAPI 應用程式實例。
    把所有 router 與中介層註冊集中在這裡，方便日後擴充。
    """

    settings = get_settings()

    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
    )

    # CORS 設定：目前先開放全部來源，方便前端 MVP 串接
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 註冊 routers
    app.include_router(health.router)
    app.include_router(session.router)
    app.include_router(question.router)
    app.include_router(answer.router)
    app.include_router(report.router)

    return app


app = create_app()

