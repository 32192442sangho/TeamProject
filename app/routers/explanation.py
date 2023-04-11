from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from app.schemas.explanation import ExplainDTO
from app.services.explanation_ai.final.explanation import final
from typing import Dict

router = APIRouter()


@router.post("/aifeedback")
async def explain_video():
    a = final("app/services/video_data/13-1_KR-6331999909_11.webm")
    b = final("app/services/video_data/13-1_KR-6331999909_21.webm")
    c = final("app/services/video_data/13-1_KR-6331999909_29.webm")
    d = final("app/services/video_data/13-1_KR-6331999909_39.webm")
    return {"a": a, "b": b, "c": c, "d": d}
# {"videopath":"app/services/video_data/13-1_KR-6331999909_11.webm"}
