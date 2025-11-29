from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .dbs import Base  # your SQLAlchemy base object


class Category(Base):
    __tablename__ = "Category"

    CategoryID = Column(Integer, primary_key=True, index=True)
    CategoryName = Column(String(100), nullable=False)
    Description = Column(String(255))
    CreatedAt = Column(DateTime, default=datetime.utcnow)
    UpdatedAt = Column(DateTime, default=datetime.utcnow)


class Supplier(Base):
    __tablename__ = "Supplier"

    SupplierID = Column(Integer, primary_key=True, index=True)
    SupplierName = Column(String(150), nullable=False)
    ContactName = Column(String(100))
    Phone = Column(String(20))
    Email = Column(String(150))
    Address = Column(String(255))
    City = Column(String(100))
    Country = Column(String(100))
    CreatedAt = Column(DateTime, default=datetime.utcnow)
    UpdatedAt = Column(DateTime, default=datetime.utcnow)


class Product(Base):
    __tablename__ = "Product"

    ProductID = Column(Integer, primary_key=True, index=True)
    ProductName = Column(String(100), nullable=False)
    CategoryID = Column(Integer, ForeignKey("Category.CategoryID"), nullable=False)
    SupplierID = Column(Integer, ForeignKey("Supplier.SupplierID"), nullable=False)
    SKU = Column(String(50), unique=True, nullable=False)
    Description = Column(String(255))
    QuantityInStock = Column(Integer, default=0)
    UnitPrice = Column(DECIMAL(10, 2), nullable=False)
    ReorderLevel = Column(Integer, default=10)
    IsActive = Column(Boolean, default=True)
    CreatedAt = Column(DateTime, default=datetime.utcnow)
    UpdatedAt = Column(DateTime, default=datetime.utcnow)

    # Relationships
    Category = relationship("Category")
    Supplier = relationship("Supplier")

class User(Base):
    __tablename__ = "Users"

    UserID = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String(100), nullable=False)
    LastName = Column(String(100), nullable=False)
    Email = Column(String(150), unique=True, nullable=False)
    Phone = Column(String(20))
    Username = Column(String(100), unique=True, nullable=False)
    PasswordHash = Column(String(255), nullable=False)
    Role = Column(String(50), default="User")
    IsActive = Column(Boolean, default=True)
    CreatedAt = Column(DateTime, default=datetime.utcnow)
    UpdatedAt = Column(DateTime, default=datetime.utcnow)

class InventoryTransaction(Base):
    __tablename__ = "InventoryTransaction"

    TransactionID = Column(Integer, primary_key=True, index=True)
    ProductID = Column(Integer, ForeignKey("Product.ProductID"), nullable=False)
    QuantityChanged = Column(Integer, nullable=False)
    TransactionType = Column(String(50), nullable=False)  # e.g., "Addition", "Removal", "Adjustment"
    TransactionDate = Column(DateTime, default=datetime.utcnow)
    Notes = Column(Text)

    # Relationships
    Product = relationship("Product")
class AuditLog(Base):
    __tablename__ = "AuditLog"

    LogID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("Users.UserID"), nullable=False)
    Action = Column(String(255), nullable=False)
    Timestamp = Column(DateTime, default=datetime.utcnow)
    Details = Column(Text)

    # Relationships
    User = relationship("User") 