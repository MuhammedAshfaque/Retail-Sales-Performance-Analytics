# ⚡ Power Query ETL & Data Cleansing

Power Query is the data preparation engine in Power BI (often called the "Kitchen" where raw ingredients are washed and chopped before cooking).

---

## 🛠️ Essential Power Query Rules for Beginners

1. **Fix Data Types Early**: Always ensure Date columns are set to `Date`, financial metrics to `Currency` or `Decimal Number`, quantities to `Whole Number`, and IDs/Codes to `Text`.
2. **Remove Unnecessary Columns**: If a column won't be used in filtering, slicing, or calculations, remove it. This speeds up Power BI and saves memory.
3. **Avoid Merging Fact Tables**: Do not merge dimensional tables directly into your fact table inside Power Query. Instead, keep them separate and connect them in the **Model View** using relationships (Star Schema).
4. **Rename Applied Steps**: In the right-hand panel (**Applied Steps**), right-click and give descriptive names to complex steps so future teammates can understand your logic.

---

## 🚀 How to Open Power Query in Power BI Desktop
1. In the **Home** tab ribbon, click **Transform Data**.
2. The Power Query Editor window will open.
3. Click **Close & Apply** in the top left when finished with transformations.
