from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.services.security import create_access_token

router = APIRouter(tags=["Authentication"])

# A simple fake user database for demonstration.
fake_users_db = {
    "siddanth": {"username": "siddanth", "password": "password", "full_name": "Siddanth reddy"},
    "test": {"username": "test", "password": "test123", "full_name": "test user"}
}

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user:
        return False
    if password != user["password"]:
        return False
    return user

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
