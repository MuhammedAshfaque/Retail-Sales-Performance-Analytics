# 🎨 Dashboard Wireframe & Design Blueprint

A great Power BI report follows the **"F-Pattern" visual hierarchy**:
- **Top Bar**: Report title, logo, global slicers (Date range, Region).
- **Top Row**: High-level KPI Cards (The most important executive numbers).
- **Middle Section**: Trends over time and primary comparisons (Line chart & Bar chart).
- **Bottom Section**: Granular details, breakdowns, and tables (Matrix, Top N items).

---

## 📄 Page 1: Executive Sales & Profit Overview

### Visual Layout Grid

```text
+-----------------------------------------------------------------------------------+
| 🏢 EXECUTIVE SALES OVERVIEW                   [ Slicer: Year ] [ Slicer: Region ] |
+-----------------------------------------------------------------------------------+
| [ CARD ]           [ CARD ]           [ CARD ]           [ CARD ]                 |
| Total Revenue      Total Profit       Profit Margin %    Total Orders             |
| $1,248,500         $412,300           33.0%              750                      |
+------------------------------------+----------------------------------------------+
| 📈 LINE & CLUSTERED COLUMN CHART   | 📊 CLUSTERED BAR CHART                       |
| Monthly Revenue & Profit Trend     | Revenue by Product Category & Subcategory    |
| (X-Axis: Month Short, Y-Axis: $)   | (Y-Axis: Category, X-Axis: Total Revenue)    |
|                                    |                                              |
|                                    |                                              |
+------------------------------------+----------------------------------------------+
| 🍩 DONUT CHART                     | 📋 MATRIX / TABLE                            |
| Revenue by Customer Segment        | Top 5 Regional Breakdown                     |
| (Legend: Segment, Values: Revenue) | (Region, Manager, Orders, Revenue, Margin %) |
|                                    |                                              |
+------------------------------------+----------------------------------------------+
```

### Visual Configuration Details

1. **KPI Cards (New Card Visual or Card)**:
   - Card 1: `[Total Revenue]` -> Format as `$#,##0`
   - Card 2: `[Total Profit]` -> Format as `$#,##0`
   - Card 3: `[Profit Margin %]` -> Format as `0.0%`
   - Card 4: `[Total Orders]` -> Format as `#,##0`

2. **Monthly Trend Chart (Line Chart or Area Chart)**:
   - **X-Axis**: `Dim_Date[Month Short]` (Sorted by `Dim_Date[Month Number]`)
   - **Y-Axis**: `[Total Revenue]`
   - **Secondary Y-Axis**: `[Total Profit]`

3. **Category Breakdown (Clustered Bar Chart)**:
   - **Y-Axis**: `dim_products[Category]`
   - **X-Axis**: `[Total Revenue]`
   - **Tooltips**: `[Total Profit]`, `[Profit Margin %]`

4. **Customer Segment Breakdown (Donut Chart)**:
   - **Legend**: `dim_customers[Segment]`
   - **Values**: `[Total Revenue]`

---

## 📄 Page 2: Product & Customer Profitability Deep-Dive

### Layout Grid

```text
+-----------------------------------------------------------------------------------+
| 🔍 PRODUCT & CUSTOMER PROFITABILITY           [ Slicer: Category ] [ Search Box ] |
+---------------------------------------------------+-------------------------------+
| 📊 SCATTER PLOT                                   | 🏆 TOP 5 PRODUCTS            |
| Revenue vs. Profit Margin %                       | Horizontal Bar Chart          |
| (X-Axis: Revenue, Y-Axis: Margin %, Bubbles: SKU) | (Values: Profit)              |
+---------------------------------------------------+-------------------------------+
| 📑 DETAILED PERFORMANCE MATRIX (with Data Bars)                                   |
| Rows: Category > SubCategory > Product                                            |
| Values: Units Sold | Total Revenue | Total Cost | Total Profit | Profit Margin %  |
+-----------------------------------------------------------------------------------+
```

---

## 🎨 Recommended Professional Color Palette

Clean corporate styling prevents visual clutter:
- **Primary / Brand Navy**: `#1B365D` (Headers, Primary bars)
- **Accent Teal / Cyan**: `#00A3E0` (Line charts, Highlights)
- **Positive / Profit Green**: `#28A745` (Profitable indicators, positive variances)
- **Warning / Alert Coral**: `#E63946` (Negative profit, low margins)
- **Background Light Gray**: `#F8F9FA` (Clean canvas background)
- **Card Background**: `#FFFFFF` with slight shadow (Elevation effect)
