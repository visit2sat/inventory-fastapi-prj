from sqlalchemy.orm import Session
from .. import models

def get_all_products(db: Session):
    """Fetch all active products along with Category and Supplier."""
    return db.query(models.Product).join(models.Category).join(models.Supplier).all()

def get_product_by_id(db: Session, product_id: int):
    """Fetch a single product by its ID."""
    return db.query(models.Product).filter(models.Product.ProductID == product_id).first()

def create_product(db: Session, product_data: dict):
    """Create a new product."""
    new_product = models.Product(**product_data)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def update_product(db: Session, product_id: int, update_data: dict):
    """Update an existing product."""
    product = db.query(models.Product).filter(models.Product.ProductID == product_id).first()
    if not product:
        return None
    for key, value in update_data.items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    """Delete a product by its ID."""
    product = db.query(models.Product).filter(models.Product.ProductID == product_id).first()
    if not product:
        return None
    db.delete(product)
    db.commit()
    return product