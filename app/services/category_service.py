from sqlalchemy.orm import Session
from datetime import datetime
from .. import models

# ============================================================
# CRUD Operations
# ============================================================
def get_all_categories(db: Session):
    """Fetch all active categories along with their Products."""
    return db.query(models.Category).join(models.Product).all()
def get_category_by_id(db: Session, category_id: int):
    """Fetch a single category by its ID."""
    return db.query(models.Category).filter(models.Category.CategoryID == category_id).first()
def create_category(db: Session, category_data: dict):
    """Create a new category."""
    new_category = models.Category(**category_data)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
def update_category(db: Session, category_id: int, update_data: dict):
    """Update an existing category."""
    category = db.query(models.Category).filter(models.Category.CategoryID == category_id).first()
    if not category:
        return None
    for key, value in update_data.items():
        setattr(category, key, value)
    category.UpdatedAt = datetime.utcnow() # type: ignore
    db.commit()
    db.refresh(category)
    return category
def delete_category(db: Session, category_id: int):
    """Delete a category by its ID."""
    category = db.query(models.Category).filter(models.Category.CategoryID == category_id).first()
    if not category:
        return None
    db.delete(category)
    db.commit()
    return category
