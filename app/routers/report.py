from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
import os
from app.services.report_generator import generate_report
from app.services.security import get_current_user

router = APIRouter(
    prefix="/report",
    tags=["Report"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/generate")
async def report_generate():
    output_file = generate_report()
    return {"message": "Report generated successfully.", "output_file": output_file}

@router.get("/download")
async def report_download():
    output_file = "uploads/output.csv"
    if not os.path.exists(output_file):
        raise HTTPException(status_code=404, detail="Output report not found. Please generate it first.")
    return FileResponse(path=output_file, filename="output.csv", media_type="text/csv")
