from fastapi import APIRouter, HTTPException, Depends
import json
import os
from app.services.transform import load_transformation_rules
from app.services.security import get_current_user

router = APIRouter(
    prefix="/config",
    tags=["Configuration"],
    dependencies=[Depends(get_current_user)]
)

TRANSFORM_CONFIG_PATH = os.path.join("config", "transform_rules.json")

@router.get("/transform-rules")
async def get_transform_rules():
    rules = load_transformation_rules()
    return {"transformations": rules}

@router.put("/transform-rules")
async def update_transform_rules(new_rules: dict):
    try:
        os.makedirs("config", exist_ok=True)
        with open(TRANSFORM_CONFIG_PATH, "w") as f:
            json.dump({"transformations": new_rules}, f, indent=4)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating transformation rules: {str(e)}")
    return {"message": "Transformation rules updated successfully."}
