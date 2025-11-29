from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..dbs import SessionLocal
from ..services import supplier_service
from ..schemas import SupplierResponseModel, CreateSupplierModel, UpdateSupplierModel
router = APIRouter(prefix="/suppliers", tags=["Suppliers"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/", response_model=List[SupplierResponseModel])
def read_suppliers(db: Session = Depends(get_db)):
    """Fetch all suppliers."""
    suppliers = supplier_service.get_all_suppliers(db)
    return suppliers
@router.get("/{supplier_id}", response_model=SupplierResponseModel)
def read_supplier(supplier_id: int, db: Session = Depends(get_db)):
    """Fetch a single supplier by its ID."""
    supplier = supplier_service.get_supplier_by_id(db, supplier_id)
    if not supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    return supplier
@router.post("/", response_model=SupplierResponseModel, status_code=status.HTTP_201_CREATED)
def create_supplier(supplier_data: CreateSupplierModel, db: Session = Depends(get_db)):
    """Create a new supplier."""
    new_supplier = supplier_service.create_supplier(db, supplier_data.dict())
    return new_supplier
@router.put("/{supplier_id}", response_model=SupplierResponseModel)
def update_supplier(supplier_id: int, update_data: UpdateSupplierModel, db: Session = Depends(get_db)):
    """Update an existing supplier."""
    updated_supplier = supplier_service.update_supplier(db, supplier_id, update_data.dict())
    if not updated_supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    return updated_supplier 
@router.delete("/{supplier_id}", response_model=SupplierResponseModel)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    """Delete a supplier by its ID."""
    deleted_supplier = supplier_service.delete_supplier(db, supplier_id)
    if not deleted_supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    return deleted_supplier
# ============================================================