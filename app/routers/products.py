from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..dbs import SessionLocal
from ..models import Product
from ..schemas import ProductCreateModel, ProductUpdateModel, ProductResponseModel
from ..services import product_service
router = APIRouter(prefix="/products", tags=["Products"])

# Dependency - Get DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[ProductResponseModel], status_code=status.HTTP_200_OK)
def get_all_products(db: Session = Depends(get_db)):
    """
    Retrieve all products with their category and supplier details.
    """
    products = product_service.get_all_products(db)
    return products

@router.get("/{product_id}", response_model=ProductResponseModel, status_code=status.HTTP_200_OK)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single product by its ID.
    """
    product = product_service.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product
@router.post("/", response_model=ProductResponseModel, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreateModel, db: Session = Depends(get_db)):
    """
    Create a new product.
    """
    new_product = product_service.create_product(db, product.dict())
    return new_product
@router.put("/{product_id}", response_model=ProductResponseModel, status_code=status.HTTP_200_OK)
def update_product(product_id: int, product_update: ProductUpdateModel, db: Session =
                     Depends(get_db)):
     """
     Update an existing product.
     """
     updated_product = product_service.update_product(db, product_id, product_update.dict(exclude_unset=True))
     if not updated_product:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
     return updated_product
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a product by its ID.
    """
    deleted_product = product_service.delete_product(db, product_id)
    if not deleted_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return None