from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User

user_router = APIRouter()


@user_router.post("/login", tags=["sesion"], response_model = dict, status_code = 200)
def login(user: User):
    if user.email == "admin@salle.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content={"token": token})
