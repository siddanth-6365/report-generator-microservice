from fastapi import APIRouter
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

router = APIRouter(tags=["Metrics"])

@router.get("/metrics")
async def get_metrics():
    # Return the generated metrics in Prometheus text format.
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
