# ⚠️ Top 10 Power BI Mistakes Beginners Make (And How to Fix Them)

Learning Power BI is straightforward once you know the common traps. Here is your reference guide to avoid the most frequent mistakes.

---

### 1. ❌ Using Implicit Measures instead of Explicit Measures
- **Mistake**: Dragging a numeric column (e.g. `Revenue`) directly into a visual and letting Power BI calculate "Sum of Revenue".
- **Problem**: You cannot format it globally, reference it in other DAX formulas, or control its aggregation context.
- **Fix**: Always write an explicit DAX measure: `Total Revenue = SUM(fact_sales[Revenue])`.

### 2. ❌ Letting Months Sort Alphabetically (April, August, December...)
- **Mistake**: Adding `Month Name` to an axis and having "April" appear before "January".
- **Fix**: Select `Month Short` or `Month Name` column -> click **Column Tools** tab -> **Sort by Column** -> choose `Month Number`.

### 3. ❌ Keeping Everything in One Giant Flat Table
- **Mistake**: Merging all tables into 1 giant table with 50 columns.
- **Problem**: Slows down performance, bloats memory, and creates DAX calculation anomalies when counting customers or products.
- **Fix**: Use a Star Schema with 1 Fact table connected to 1-to-many Dimension tables.

### 4. ❌ Using "Both" (Bi-directional) Cross-Filter Direction
- **Mistake**: Changing relationship direction from "Single" to "Both" when numbers don't filter as expected.
- **Problem**: Causes ambiguous filter paths, slow queries, and unpredictable DAX calculation results.
- **Fix**: Keep relationships set to "Single". If a specific measure requires bi-directional filtering, use `CROSSFILTER()` inside that specific DAX measure.

### 5. ❌ Using the Division Slash (`/`) instead of `DIVIDE()`
- **Mistake**: Writing `[Total Profit] / [Total Revenue]`.
- **Problem**: When `[Total Revenue]` is `0` or null, your visual will display `NaN` or `Infinity` errors.
- **Fix**: Use `DIVIDE([Total Profit], [Total Revenue], 0)`.

### 6. ❌ Not Creating a Dedicated Date/Calendar Table
- **Mistake**: Relying on Power BI's automatic date hierarchy (`OrderDate.Month`, `OrderDate.Year`).
- **Problem**: Auto date/time creates hidden tables for every date column, bloating file size, and breaks advanced DAX time intelligence (`SAMEPERIODLASTYEAR`, `TOTALYTD`).
- **Fix**: Create `Dim_Date` with DAX or Power Query, mark it as a Date Table, and turn off Auto Date/Time in File -> Options -> Data Load.

### 7. ❌ Hardcoding File Paths in Power Query
- **Mistake**: Moving project files to another folder or computer and breaking all queries.
- **Fix**: Keep all data files inside the project's `data/` folder. If paths change, go to **Home -> Data Source Settings** -> **Change Source** and select the new location.

### 8. ❌ Visual Clutter & "Chart Jumble"
- **Mistake**: Putting 15 different pie charts, gauges, and tables with conflicting bright colors on one page.
- **Fix**: Limit each report page to 4-6 focused visuals. Stick to a 3-color palette (Primary, Accent, Neutral).

### 9. ❌ Forgetting to Check Data Types in Power Query
- **Mistake**: Numeric columns loaded as "Text" or date columns loaded as "Text".
- **Problem**: Power BI won't let you sum, average, or drill down by date.
- **Fix**: Inspect every column header icon in Power Query (`123` = Integer, `$ / 1.2` = Decimal/Currency, `📅` = Date, `ABC` = Text).

### 10. ❌ Not Renaming Measures and Columns for Business Users
- **Mistake**: Leaving columns named `fact_sales.rev_usd_amt` or `Sum of TotalRevenue`.
- **Fix**: Rename measures to clean business terms: `Total Revenue`, `Gross Profit`, `Order Count`.
