from fastapi import APIRouter


router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check() -> dict:
    """
    健康檢查端點，供前端或監控系統確認服務是否正常運作。
    """

    return {"status": "ok"}

