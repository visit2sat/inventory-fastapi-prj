from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional


# ============================================================
# Category and Supplier Response Models (for nested response)
# ============================================================
class CategoryResponseModel(BaseModel):
    CategoryID: int
    CategoryName: str
    Description: Optional[str] = None

    class Config:
         model_config = ConfigDict(from_attributes=True)

class CreateCategoryModel(BaseModel):
    CategoryName: str
    Description: Optional[str] = None
    class Config:
         model_config = ConfigDict(from_attributes=True)

class UpdateCategoryModel(BaseModel):
    CategoryName: Optional[str] = None
    Description: Optional[str] = None
    class Config:
         model_config = ConfigDict(from_attributes=True)

class DeleteCategoryModel(BaseModel):
    CategoryID: int
    class Config:
         model_config = ConfigDict(from_attributes=True)
class CreateSupplierModel(BaseModel):
    SupplierName: str
    ContactName: Optional[str] = None
    Phone: Optional[str] = None
    Email: Optional[str] = None
    Address: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None
    class Config:
         model_config = ConfigDict(from_attributes=True)

class UpdateSupplierModel(BaseModel):
    SupplierName: Optional[str] = None
    ContactName: Optional[str] = None
    Phone: Optional[str] = None
    Email: Optional[str] = None
    Address: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None
    class Config:
         model_config = ConfigDict(from_attributes=True)
         
class DeleteSupplierModel(BaseModel):
    SupplierID: int
    class Config:
         model_config = ConfigDict(from_attributes=True)
    
# ============================================================
# Supplier Response Model
# ============================================================
class SupplierResponseModel(BaseModel):
    SupplierID: int
    SupplierName: str
    ContactName: Optional[str] = None
    Phone: Optional[str] = None
    Email: Optional[str] = None
    Address: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None

    class Config:
         model_config = ConfigDict(from_attributes=True)


# ============================================================
# Product Create Model
# ============================================================
class ProductCreateModel(BaseModel):
    ProductName: str = Field(..., max_length=100, description="Name of the product")
    CategoryID: int = Field(..., description="Foreign key reference to Category table")
    SupplierID: int = Field(..., description="Foreign key reference to Supplier table")
    SKU: str = Field(..., max_length=50, description="Unique SKU code")
    Description: Optional[str] = Field(None, max_length=255, description="Product description")
    QuantityInStock: int = Field(..., ge=0, description="Available stock quantity")
    UnitPrice: float = Field(..., gt=0, description="Price per unit")
    ReorderLevel: Optional[int] = Field(10, ge=0, description="Minimum quantity before reorder")
    IsActive: Optional[bool] = Field(True, description="Whether the product is active")

    class Config:
         model_config = ConfigDict(from_attributes=True)


# ============================================================
# Product Update Model
# ============================================================
class ProductUpdateModel(BaseModel):
    ProductName: Optional[str] = Field(None, max_length=100)
    CategoryID: Optional[int]
    SupplierID: Optional[int]
    SKU: Optional[str] = Field(None, max_length=50)
    Description: Optional[str] = Field(None, max_length=255)
    QuantityInStock: Optional[int] = Field(None, ge=0)
    UnitPrice: Optional[float] = Field(None, gt=0)
    ReorderLevel: Optional[int] = Field(None, ge=0)
    IsActive: Optional[bool] = None
    UpdatedAt: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
         model_config = ConfigDict(from_attributes=True)


# ============================================================
# Product Response Model
# ============================================================
class ProductResponseModel(BaseModel):
    ProductID: int
    ProductName: str
    SKU: str
    Description: Optional[str] = None
    QuantityInStock: int
    UnitPrice: float
    ReorderLevel: int
    IsActive: bool
    CreatedAt: datetime
    UpdatedAt: datetime

    Category: Optional[CategoryResponseModel] = None
    Supplier: Optional[SupplierResponseModel] = None

    class Config:
        model_config = ConfigDict(from_attributes=True)

    # id: int
    # qty_before: Optional[int]
    # qty_after: Optional[int]
    # timestamp: Optional[datetime]
# ============================================================
# User Create Model
# ============================================================
class UserCreateModel(BaseModel):
    FirstName: str = Field(..., max_length=100)
    LastName: str = Field(..., max_length=100)
    Email: str
    Phone: Optional[str] = Field(None, max_length=20)
    Username: str = Field(..., max_length=100)
    Password: str = Field(..., min_length=6, description="Plain password to be hashed before saving")
    Role: Optional[str] = Field("User", description="User role (Admin, Manager, User)")
    IsActive: Optional[bool] = True

    class Config:
        model_config = ConfigDict(from_attributes=True)


# ============================================================
# User Update Model
# ============================================================
class UserUpdateModel(BaseModel):
    FirstName: Optional[str] = Field(None, max_length=100)
    LastName: Optional[str] = Field(None, max_length=100)
    Phone: Optional[str] = Field(None, max_length=20)
    Role: Optional[str] = Field(None, description="User role (Admin, Manager, User)")
    IsActive: Optional[bool] = None
    UpdatedAt: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        model_config = ConfigDict(from_attributes=True)


# ============================================================
# User Response Model
# ============================================================
class UserResponseModel(BaseModel):
    UserID: int
    FirstName: str
    LastName: str
    Email: str
    Phone: Optional[str]
    Username: str
    Role: str
    IsActive: bool
    CreatedAt: datetime
    UpdatedAt: datetime

    class Config:
        model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    
class transactionModel(BaseModel):
    id: int
    qty_before: Optional[int]
    qty_after: Optional[int]
    timestamp: Optional[datetime]
    class Config:
        model_config = ConfigDict(from_attributes=True)
class auditlogModel(BaseModel):
    id: int
    action: Optional[str]
    entity: Optional[str]
    entity_id: Optional[int]
    timestamp: Optional[datetime]
    user_id: Optional[int]
    class Config:
        model_config = ConfigDict(from_attributes=True)
# ============================================================