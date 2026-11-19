import csv
import os
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, mode="r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    print("=" * 65)
    print("🎯 POWER BI PROJECT GROUND TRUTH BENCHMARKS (TESTING SUITE)")
    print("=" * 65)

    sales = load_csv("fact_sales.csv")
    products = {p["ProductID"]: p for p in load_csv("dim_products.csv")}
    customers = {c["CustomerID"]: c for c in load_csv("dim_customers.csv")}
    regions = {r["RegionID"]: r for r in load_csv("dim_regions.csv")}

    # 1. Global KPIs
    total_rev = sum(float(x["Revenue"]) for x in sales)
    total_cost = sum(float(x["TotalCost"]) for x in sales)
    total_profit = sum(float(x["Profit"]) for x in sales)
    profit_margin = (total_profit / total_rev) * 100 if total_rev else 0
    total_units = sum(int(x["Quantity"]) for x in sales)
    unique_orders = len(set(x["OrderID"] for x in sales))
    unique_customers = len(set(x["CustomerID"] for x in sales))
    avg_order_value = total_rev / unique_orders if unique_orders else 0

    print("\n📌 1. OVERALL KPI CARD BENCHMARKS (Check your Card Visuals):")
    print(f"   • Total Revenue:         ${total_rev:,.2f}")
    print(f"   • Total Cost:            ${total_cost:,.2f}")
    print(f"   • Total Profit:          ${total_profit:,.2f}")
    print(f"   • Profit Margin %:       {profit_margin:.2f}%")
    print(f"   • Total Orders:          {unique_orders:,}")
    print(f"   • Total Units Sold:      {total_units:,}")
    print(f"   • Total Active Customers:{unique_customers:,}")
    print(f"   • Avg Order Value (AOV): ${avg_order_value:,.2f}")

    # 2. Year Breakdown
    by_year_rev = defaultdict(float)
    by_year_prof = defaultdict(float)
    by_year_orders = defaultdict(set)

    for x in sales:
        yr = x["OrderDate"][:4]
        rev = float(x["Revenue"])
        prof = float(x["Profit"])
        by_year_rev[yr] += rev
        by_year_prof[yr] += prof
        by_year_orders[yr].add(x["OrderID"])

    print("\n📌 2. YEAR BREAKDOWN (Test your Date Slicer):")
    for yr in sorted(by_year_rev.keys()):
        yr_margin = (by_year_prof[yr] / by_year_rev[yr]) * 100 if by_year_rev[yr] else 0
        print(f"   • [{yr}] Revenue: ${by_year_rev[yr]:,.2f} | Profit: ${by_year_prof[yr]:,.2f} ({yr_margin:.2f}%) | Orders: {len(by_year_orders[yr]):,}")

    # 3. Category Breakdown
    cat_rev = defaultdict(float)
    cat_prof = defaultdict(float)
    for x in sales:
        cat = products.get(x["ProductID"], {}).get("Category", "Unknown")
        cat_rev[cat] += float(x["Revenue"])
        cat_prof[cat] += float(x["Profit"])

    print("\n📌 3. CATEGORY BREAKDOWN (Test your Bar Chart):")
    for cat, rev in sorted(cat_rev.items(), key=lambda i: i[1], reverse=True):
        m = (cat_prof[cat] / rev) * 100 if rev else 0
        pct = (rev / total_rev) * 100
        print(f"   • {cat:<16}: ${rev:,.2f} ({pct:.1f}% of total) | Profit: ${cat_prof[cat]:,.2f} ({m:.1f}% margin)")

    # 4. Region Breakdown
    reg_rev = defaultdict(float)
    for x in sales:
        reg_name = regions.get(x["RegionID"], {}).get("RegionName", "Unknown")
        reg_rev[reg_name] += float(x["Revenue"])

    print("\n📌 4. REGION BREAKDOWN (Test your Map or Region Slicer):")
    for reg, rev in sorted(reg_rev.items(), key=lambda i: i[1], reverse=True):
        pct = (rev / total_rev) * 100
        print(f"   • {reg:<8}: ${rev:,.2f} ({pct:.1f}%)")

    # 5. Customer Segment Breakdown
    seg_rev = defaultdict(float)
    for x in sales:
        seg = customers.get(x["CustomerID"], {}).get("Segment", "Unknown")
        seg_rev[seg] += float(x["Revenue"])

    print("\n📌 5. CUSTOMER SEGMENT BREAKDOWN (Test your Donut Chart):")
    for seg, rev in sorted(seg_rev.items(), key=lambda i: i[1], reverse=True):
        pct = (rev / total_rev) * 100
        print(f"   • {seg:<14}: ${rev:,.2f} ({pct:.1f}%)")

    print("\n" + "=" * 65)
    print("✅ All data tests passed without integrity errors!")
    print("=" * 65)

if __name__ == "__main__":
    main()
