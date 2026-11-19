# 📐 DAX (Data Analysis Expressions) Reference Guide

This folder contains organized DAX measures ranging from introductory sums to intermediate time intelligence calculations.

---

## 🏗️ Best Practice: Create a Dedicated `_Measures` Table

Rather than scattering your calculated measures inside different data tables, professionals always keep them in a centralized measures table.

### How to create it in Power BI Desktop:
1. In the **Home** tab ribbon, click **Enter Data**.
2. Name the table `_Measures` (the leading underscore keeps it at the top of the Fields pane).
3. Leave Column 1 blank and click **Load**.
4. In the Fields pane on the right, right-click `_Measures` and select **New Measure**.
5. Paste your DAX code and hit **Enter**.
6. (Optional) Right-click and delete the original empty `Column1` from `_Measures`. The icon for `_Measures` will turn into a calculator icon!

---

## 🗂️ DAX File Index

| File | Level | Focus | Key Functions Used |
| :--- | :--- | :--- | :--- |
| [`00_calendar_date_table.dax`](00_calendar_date_table.dax) | Essential | Full Calendar Table generation | `CALENDAR`, `ADDCOLUMNS`, `FORMAT`, `QUARTER`, `WEEKDAY` |
| [`01_core_kpi_measures.dax`](01_core_kpi_measures.dax) | Beginner | High-level metrics | `SUM`, `DISTINCTCOUNT`, `DIVIDE` |
| [`02_margin_and_ratios.dax`](02_margin_and_ratios.dax) | Beginner | Financial ratios & percentages | `DIVIDE`, `AVERAGE` |
| [`03_time_intelligence.dax`](03_time_intelligence.dax) | Intermediate | Period comparisons | `TOTALYTD`, `SAMEPERIODLASTYEAR`, `DATEADD` |
| [`04_ranking_and_categorization.dax`](04_ranking_and_categorization.dax) | Intermediate | Filtering & contextual ranks | `CALCULATE`, `ALL`, `ALLSELECTED`, `RANKX`, `SELECTEDVALUE` |

---

## 🏷️ Measure Formatting Checklist

After adding any measure, always set its display format in the **Measure Tools** ribbon:

- **Revenue / Cost / Profit**: Currency (`$`) with `0` or `2` decimal places.
- **Profit Margin % / Discount % / YoY Growth %**: Percentage (`%`) with `1` or `2` decimal places.
- **Units / Orders / Customers**: Whole Number with thousands separator (`,`).
