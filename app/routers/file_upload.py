from fastapi import APIRouter, UploadFile, File, Depends
from app.services.file_processor import save_uploaded_file
from app.services.security import get_current_user

router = APIRouter(
    prefix="/upload",
    tags=["File Upload"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/input")
async def upload_input(file: UploadFile = File(...)):
    await save_uploaded_file(file, "input.csv")
    return {"message": "Input file uploaded successfully."}

@router.post("/reference")
async def upload_reference(file: UploadFile = File(...)):
    await save_uploaded_file(file, "reference.csv")
    return {"message": "Reference file uploaded successfully."}