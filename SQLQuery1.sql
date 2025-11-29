use inventroy

CREATE TABLE Product (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,          -- Unique product ID
    ProductName VARCHAR(100) NOT NULL,                -- Product name
    CategoryID INT NULL,                              -- Foreign key to category table
    SupplierID INT NULL,                              -- Foreign key to supplier table
    SKU VARCHAR(50) UNIQUE NOT NULL,                  -- Stock Keeping Unit (unique)
    Description VARCHAR(255),                         -- Optional description
    QuantityInStock INT DEFAULT 0 CHECK (QuantityInStock >= 0),  -- Stock quantity
    UnitPrice DECIMAL(10,2) NOT NULL CHECK (UnitPrice >= 0),     -- Price per unit
    ReorderLevel INT DEFAULT 0 CHECK (ReorderLevel >= 0),        -- Reorder threshold
    IsActive BIT DEFAULT 1,                           -- Active status
    CreatedAt DATETIME DEFAULT GETDATE(),             -- Record creation timestamp
    UpdatedAt DATETIME DEFAULT GETDATE()              -- Record update timestamp
);

