from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..dbs import get_db
from ..services import user_service
from ..auth import verify_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Authenticate user and return JWT token.
    """
    return user_service.authenticate_user(db, form_data.username, form_data.password)


@router.get("/verify")
def verify_token_route(token: str = Depends(oauth2_scheme)):
    """
    Verify a token (for testing).
    """
    username = verify_token(token)
    return {"username": username, "message": "Token is valid."}
