# 📊 Sample Dataset Documentation

This directory contains clean, structured e-commerce retail data designed specifically for learning Power BI fundamentals, data modeling (Star Schema), DAX calculations, and report visualization.

---

## 📁 Files Overview

| File Name | Purpose | Type | Key Column(s) |
| :--- | :--- | :--- | :--- |
| `fact_sales.csv` | Transactional sales orders & line items | Fact Table | Primary: `LineItemID`<br>Foreign: `CustomerID`, `ProductID`, `RegionID` |
| `dim_customers.csv` | Customer demographics & segments | Dimension Table | Primary: `CustomerID` |
| `dim_products.csv` | Product catalog, costs & list prices | Dimension Table | Primary: `ProductID` |
| `dim_regions.csv` | Geographic sales territories & managers | Dimension Table | Primary: `RegionID` |
| `sales_data_flat.csv` | All 4 tables joined into a single table | Flat Table | Beginner mode (single table import) |

---

## 🗂️ Data Dictionary

### 1. `fact_sales.csv` (Fact Table)
Contains 1,131 order line items from **January 1, 2023** to **December 31, 2024**.

- `LineItemID` (Text) - Unique identifier for each line item (e.g. `ORD-10001-1`).
- `OrderID` (Text) - Order identifier; an order can contain 1 to 3 line items.
- `OrderDate` (Date) - Format `YYYY-MM-DD`.
- `ShipDate` (Date) - Format `YYYY-MM-DD` (typically 1-5 days after OrderDate).
- `CustomerID` (Text) - References `dim_customers.CustomerID`.
- `ProductID` (Text) - References `dim_products.ProductID`.
- `RegionID` (Text) - References `dim_regions.RegionID`.
- `Quantity` (Whole Number) - Number of units purchased.
- `UnitPrice` (Decimal/Currency) - Unit price at time of sale.
- `Discount` (Percentage/Decimal) - Applied discount rate (e.g., `0.05` for 5%).
- `Revenue` (Decimal/Currency) - Calculated as `Quantity * UnitPrice * (1 - Discount)`.
- `TotalCost` (Decimal/Currency) - Calculated as `Quantity * StandardCost`.
- `Profit` (Decimal/Currency) - Calculated as `Revenue - TotalCost`.

### 2. `dim_customers.csv` (Dimension Table)
- `CustomerID` (Text) - Unique customer identifier (e.g. `CUST-1001`).
- `CustomerName` (Text) - Full customer name.
- `Segment` (Text) - Market segment: `Consumer`, `Corporate`, or `Home Office`.
- `City` (Text) - Customer city.
- `State` (Text) - Customer state.
- `Country` (Text) - Customer country (`USA`).
- `PostalCode` (Text) - ZIP code.

### 3. `dim_products.csv` (Dimension Table)
- `ProductID` (Text) - Unique product SKU (e.g. `PROD-001`).
- `ProductName` (Text) - Product name.
- `Category` (Text) - High-level category: `Technology`, `Furniture`, `Office Supplies`.
- `SubCategory` (Text) - Specific grouping: `Laptops`, `Chairs`, `Paper`, `Accessories`, etc.
- `StandardCost` (Decimal/Currency) - Cost of production / acquisition.
- `ListPrice` (Decimal/Currency) - Standard retail price before discounts.

### 4. `dim_regions.csv` (Dimension Table)
- `RegionID` (Text) - Unique region code (`REG-01` to `REG-04`).
- `RegionName` (Text) - Region: `East`, `West`, `Central`, `South`.
- `Country` (Text) - Country (`United States`).
- `RegionalManager` (Text) - Territory sales leader.

---

## 💡 Recommended Path for Beginners
- **Option A (Best Practice)**: Import `fact_sales.csv`, `dim_customers.csv`, `dim_products.csv`, and `dim_regions.csv`. Build relationships in the **Model View** to create a classic **Star Schema**.
- **Option B (Fastest Start)**: Import only `sales_data_flat.csv` if you want to skip relationships and immediately build charts and visuals on a single table.
