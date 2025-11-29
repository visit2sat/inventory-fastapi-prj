from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..dbs import SessionLocal
from ..services import category_service
from ..schemas import CategoryResponseModel, CreateCategoryModel, UpdateCategoryModel
router = APIRouter(prefix="/categories", tags=["Categories"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/", response_model=List[CategoryResponseModel])
def read_categories(db: Session = Depends(get_db)):
    """Fetch all categories along with their Products."""
    categories = category_service.get_all_categories(db)
    return categories
@router.get("/{category_id}", response_model=CategoryResponseModel)
def read_category(category_id: int, db: Session = Depends(get_db)):
    """Fetch a single category by its ID."""
    category = category_service.get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category
@router.post("/", response_model=CategoryResponseModel, status_code=status.HTTP_201_CREATED)
def create_category(category_data: CreateCategoryModel, db: Session = Depends(get_db)):
    """Create a new category."""
    new_category = category_service.create_category(db, category_data.dict())
    return new_category
@router.put("/{category_id}", response_model=CategoryResponseModel)
def update_category(category_id: int, update_data: UpdateCategoryModel, db: Session = 
Depends(get_db)):
    """Update an existing category."""
    updated_category = category_service.update_category(db, category_id, update_data.dict())
    if not updated_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return updated_category
@router.delete("/{category_id}", response_model=CategoryResponseModel)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    """Delete a category by its ID."""
    deleted_category = category_service.delete_category(db, category_id)
    if not deleted_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return deleted_category 
# ============================================================