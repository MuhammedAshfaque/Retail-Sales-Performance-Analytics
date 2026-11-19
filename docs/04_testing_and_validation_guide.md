# 🧪 Power BI Testing & Validation Guide

When building Power BI solutions, testing ensures your data is accurate, relationships are properly configured, and DAX calculations return correct business results.

---

## 📋 4-Step Testing Checklist

| Step | Test Objective | What to Verify |
| :--- | :--- | :--- |
| **Test 1: Data Integrity** | Power Query ETL | No errors, correct data types (Dates as Date, Sales as Currency) |
| **Test 2: Model Relationships** | Model View | 1-to-many (`1:*`) relationships active, Single direction filter |
| **Test 3: DAX Calculations** | Card Visuals | Numbers match the ground truth benchmarks exactly |
| **Test 4: Interactivity** | Canvas Slicers | Cross-filtering updates all visuals dynamically |

---

## 🎯 Ground Truth Benchmark Numbers

You can run the included Python test suite anytime in PowerShell:
```powershell
python scripts\verify_benchmarks.py
```

### 1. Overall KPI Verification (Cards)
When you add your KPI card visuals to a blank canvas, they **must** match these exact totals:

| Metric | DAX Measure | Expected Value | Display Format |
| :--- | :--- | :--- | :--- |
| **Total Revenue** | `[Total Revenue]` | **$550,169.14** | Currency (`$#,##0`) |
| **Total Cost** | `[Total Cost]` | **$286,004.50** | Currency (`$#,##0`) |
| **Total Profit** | `[Total Profit]` | **$264,164.64** | Currency (`$#,##0`) |
| **Profit Margin %**| `[Profit Margin %]` | **48.02%** | Percentage (`0.0%`) |
| **Total Orders** | `[Total Orders]` | **750** | Whole Number |
| **Total Units Sold**| `[Total Units Sold]` | **3,801** | Whole Number |
| **Avg Order Value**| `[Average Order Value]`| **$733.56** | Currency (`$#,##0.00`) |

---

### 2. Slicer Verification (Year Filter Test)
Add a Slicer visual for `Dim_Date[Year]`. Click each year to verify filter propagation:

- **When `2023` is selected:**
  - Revenue: **$254,649.06**
  - Profit: **$123,369.06**
  - Profit Margin: **48.45%**
  - Orders: **368**
- **When `2024` is selected:**
  - Revenue: **$295,520.08**
  - Profit: **$140,795.58**
  - Profit Margin: **47.64%**
  - Orders: **382**

---

### 3. Category Breakdown Verification (Bar Chart Test)
Add a Clustered Bar Chart with `Category` on the Y-Axis and `[Total Revenue]` on the X-Axis:

- **Furniture**: **$292,612.93** (53.2% of total | 53.0% margin)
- **Technology**: **$221,719.84** (40.3% of total | 39.6% margin)
- **Office Supplies**: **$35,836.37** (6.5% of total | 59.5% margin)

---

### 4. Regional Breakdown Verification (Map / Slicer Test)
- **South**: **$215,657.68** (39.2%)
- **West**: **$183,772.99** (33.4%)
- **Central**: **$77,904.61** (14.2%)
- **East**: **$72,833.86** (13.2%)

---

## 🔍 How to Debug Common Failures

### Symptom A: Every row or card shows the exact same number ($550,169.14)
- **Cause**: The relationship between your dimension table and `fact_sales` is missing or inactive.
- **Fix**: Open **Model View**. Ensure there is an active link connecting the dimension's key to `fact_sales`.

### Symptom B: A card displays `(Blank)` or `NaN`
- **Cause**: Division by zero or missing records.
- **Fix**: Use `DIVIDE(Numerator, Denominator, 0)` instead of `/`.

### Symptom C: Months sort alphabetically ("April", "August", "December")
- **Cause**: Default text column sorting.
- **Fix**: Select `Month Short` ➡️ click **Column Tools** ➡️ **Sort by Column** ➡️ select `Month Number`.
