from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..dbs import SessionLocal
from ..models import User
from ..schemas import UserCreateModel, UserUpdateModel, UserResponseModel
from ..services import user_service
router = APIRouter(prefix="/users", tags=["Users"])
# Dependency - Get DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/", response_model=UserResponseModel, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreateModel, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    new_user = user_service.create_user(db, user)
    return new_user
@router.get("/", response_model=List[UserResponseModel], status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    """
    Retrieve all users.
    """
    users = user_service.get_all_users(db)
    return users
@router.get("/{user_id}", response_model=UserResponseModel, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single user by ID.
    """
    user = user_service.get_user_by_id(db, user_id)
    return user
@router.put("/{user_id}", response_model=UserResponseModel, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_update: UserUpdateModel, db: Session = Depends(get_db)):
    """
    Update an existing user.
    """
    updated_user = user_service.update_user(db, user_id, user_update)
    return updated_user
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user by ID.
    """
    user_service.delete_user(db, user_id)
    return
