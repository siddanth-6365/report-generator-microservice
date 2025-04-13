from fastapi import APIRouter, HTTPException, Depends
from app.services.scheduler_service import add_schedule, list_schedules, delete_schedule
from app.services.security import get_current_user

router = APIRouter(
    prefix="/schedule",
    tags=["Scheduler"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/add")
async def add_schedule_endpoint(cron_expr: str):
    try:
        job = add_schedule(cron_expr)
        return {"message": "Job scheduled successfully.", "job_id": job.id}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error scheduling job: {str(e)}")

@router.get("/list")
async def list_schedule_endpoint():
    jobs = list_schedules()
    return {"jobs": jobs}

@router.delete("/delete/{job_id}")
async def delete_schedule_endpoint(job_id: str):
    try:
        delete_schedule(job_id)
        return {"message": f"Job '{job_id}' deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting job: {str(e)}")
