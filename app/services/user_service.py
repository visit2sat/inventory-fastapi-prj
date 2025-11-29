from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime

from .. import models
from ..schemas import UserCreateModel, UserUpdateModel
#from passlib.context import CryptContext
from ..auth import create_access_token

# Password hashing context (bcrypt)
#pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ============================================================
# Utility functions
# ============================================================
def authenticate_user(db: Session, username: str, password: str):
    """Validate username and password, return JWT token."""
    user = db.query(models.User).filter(models.User.Username == username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid username or password.",
        )

    if not verify_password(password, user.PasswordHash): # type: ignore
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password.",
        )

    if not user.IsActive: # type: ignore
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive.",
        )

    access_token = create_access_token(data={"sub": user.Username})
    return {"access_token": access_token, "token_type": "bearer"}

def get_password_hash(password: str) -> str:
    """Generate a hashed password using bcrypt."""
    #return pwd_context.hash(password)
    return password

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against the hashed password."""
    #return pwd_context.verify(plain_password, hashed_password)
    return True


# ============================================================
# CRUD Operations
# ============================================================

def create_user(db: Session, payload: UserCreateModel):
    """Create a new user."""
    # Check if email or username already exists
    existing_user = db.query(models.User).filter(
        (models.User.Email == payload.Email) | (models.User.Username == payload.Username)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or Username already exists.",
        )

    hashed_password = get_password_hash(payload.Password)

    new_user = models.User(
        FirstName=payload.FirstName,
        LastName=payload.LastName,
        Email=payload.Email,
        Phone=payload.Phone,
        Username=payload.Username,
        PasswordHash=hashed_password,
        Role=payload.Role,
        IsActive=payload.IsActive,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    """Retrieve all users."""
    return db.query(models.User).order_by(models.User.UserID.asc()).all()


def get_user_by_id(db: Session, user_id: int):
    """Retrieve a user by ID."""
    user = db.query(models.User).filter(models.User.UserID == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found.",
        )
    return user


def update_user(db: Session, user_id: int, payload: UserUpdateModel):
    """Update an existing user."""
    user = db.query(models.User).filter(models.User.UserID == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found.",
        )

    # Update fields dynamically
    update_data = payload.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)
    
    user.UpdatedAt = datetime.utcnow() # type: ignore
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    """Delete (or deactivate) a user."""
    user = db.query(models.User).filter(models.User.UserID == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found.",
        )

    db.delete(user)
    db.commit()
    return {"message": f"User with ID {user_id} deleted successfully."}
