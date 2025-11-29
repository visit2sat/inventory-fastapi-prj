from sqlalchemy.orm import Session
from datetime import datetime
from .. import models

# ============================================================
# CRUD Operations  
# ============================================================
def get_all_suppliers(db: Session):
    """Fetch all active suppliers."""
    return db.query(models.Supplier).all()
def get_supplier_by_id(db: Session, supplier_id: int):
    """Fetch a single supplier by its ID."""
    return db.query(models.Supplier).filter(models.Supplier.SupplierID == supplier_id).first()
def create_supplier(db: Session, supplier_data: dict):
    """Create a new supplier."""
    new_supplier = models.Supplier(**supplier_data)
    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)
    return new_supplier
def update_supplier(db: Session, supplier_id: int, update_data: dict):
    """Update an existing supplier."""
    supplier = db.query(models.Supplier).filter(models.Supplier.SupplierID == supplier_id).first()
    if not supplier:
        return None
    for key, value in update_data.items():
        setattr(supplier, key, value)
    supplier.UpdatedAt = datetime.utcnow() # type: ignore
    db.commit()
    db.refresh(supplier)
    return supplier
def delete_supplier(db: Session, supplier_id: int):
    """Delete a supplier by its ID."""
    supplier = db.query(models.Supplier).filter(models.Supplier.SupplierID == supplier_id).first()
    if not supplier:
        return None
    db.delete(supplier)
    db.commit()
    return supplier
# ============================================================