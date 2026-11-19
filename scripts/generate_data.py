import csv
import os
import random
from datetime import datetime, timedelta

random.seed(42)

# Output directory
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# 1. Dimension: Customers
customers = [
    ("CUST-1001", "Emma Watson", "Consumer", "New York", "New York", "USA", "10001"),
    ("CUST-1002", "Liam Smith", "Corporate", "Los Angeles", "California", "USA", "90001"),
    ("CUST-1003", "Olivia Johnson", "Home Office", "Chicago", "Illinois", "USA", "60601"),
    ("CUST-1004", "Noah Brown", "Consumer", "Houston", "Texas", "USA", "77001"),
    ("CUST-1005", "Ava Davis", "Corporate", "Phoenix", "Arizona", "USA", "85001"),
    ("CUST-1006", "William Miller", "Home Office", "Philadelphia", "Pennsylvania", "USA", "19101"),
    ("CUST-1007", "Sophia Wilson", "Consumer", "San Antonio", "Texas", "USA", "78201"),
    ("CUST-1008", "James Moore", "Corporate", "San Diego", "California", "USA", "92101"),
    ("CUST-1009", "Isabella Taylor", "Consumer", "Dallas", "Texas", "USA", "75201"),
    ("CUST-1010", "Benjamin Anderson", "Corporate", "Austin", "Texas", "USA", "73301"),
    ("CUST-1011", "Mia Thomas", "Home Office", "Jacksonville", "Florida", "USA", "32099"),
    ("CUST-1012", "Elijah Jackson", "Consumer", "San Francisco", "California", "USA", "94102"),
    ("CUST-1013", "Charlotte White", "Corporate", "Seattle", "Washington", "USA", "98101"),
    ("CUST-1014", "Lucas Harris", "Home Office", "Denver", "Colorado", "USA", "80201"),
    ("CUST-1015", "Amelia Martin", "Consumer", "Boston", "Massachusetts", "USA", "02108"),
    ("CUST-1016", "Mason Thompson", "Corporate", "Miami", "Florida", "USA", "33101"),
    ("CUST-1017", "Harper Garcia", "Consumer", "Atlanta", "Georgia", "USA", "30301"),
    ("CUST-1018", "Ethan Martinez", "Home Office", "Detroit", "Michigan", "USA", "48201"),
    ("CUST-1019", "Evelyn Robinson", "Corporate", "Minneapolis", "Minnesota", "USA", "55401"),
    ("CUST-1020", "Oliver Clark", "Consumer", "Portland", "Oregon", "USA", "97201")
]

cust_file = os.path.join(DATA_DIR, "dim_customers.csv")
with open(cust_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["CustomerID", "CustomerName", "Segment", "City", "State", "Country", "PostalCode"])
    writer.writerows(customers)

# 2. Dimension: Products
products = [
    # (ProductID, ProductName, Category, SubCategory, StandardCost, ListPrice)
    ("PROD-001", "UltraBook Pro 15", "Technology", "Laptops", 750.00, 1199.99),
    ("PROD-002", "Wireless Ergonomic Mouse", "Technology", "Accessories", 15.00, 39.99),
    ("PROD-003", "Mechanical Gaming Keyboard", "Technology", "Accessories", 40.00, 89.99),
    ("PROD-004", "4K Ultra HD 27\" Monitor", "Technology", "Monitors", 180.00, 329.99),
    ("PROD-005", "Noise-Cancelling Headphones", "Technology", "Audio", 90.00, 199.99),
    ("PROD-006", "Smart Laser Printer", "Technology", "Printers", 140.00, 249.99),
    ("PROD-007", "Ergonomic Office Chair", "Furniture", "Chairs", 110.00, 229.99),
    ("PROD-008", "Height-Adjustable Standing Desk", "Furniture", "Desks", 200.00, 449.99),
    ("PROD-009", "3-Drawer Mobile File Cabinet", "Furniture", "Storage", 65.00, 139.99),
    ("PROD-010", "LED Desk Lamp with USB Port", "Furniture", "Furnishings", 18.00, 44.99),
    ("PROD-011", "Conference Table (Seats 8)", "Furniture", "Tables", 350.00, 799.99),
    ("PROD-012", "Executive Bookcase 5-Shelf", "Furniture", "Bookcases", 120.00, 259.99),
    ("PROD-013", "Multi-Purpose Copy Paper (500ct)", "Office Supplies", "Paper", 4.50, 9.99),
    ("PROD-014", "Heavy-Duty Desktop Stapler", "Office Supplies", "Fasteners", 7.00, 18.99),
    ("PROD-015", "Gel Ink Pens (Pack of 12)", "Office Supplies", "Art & Pens", 3.00, 8.49),
    ("PROD-016", "Expanding Accordion File Folder", "Office Supplies", "Storage", 5.50, 14.99),
    ("PROD-017", "Dry Erase Whiteboard 36x24", "Office Supplies", "Supplies", 22.00, 54.99),
    ("PROD-018", "Sticky Notes Value Pack (12ct)", "Office Supplies", "Paper", 4.00, 11.49)
]

prod_file = os.path.join(DATA_DIR, "dim_products.csv")
with open(prod_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ProductID", "ProductName", "Category", "SubCategory", "StandardCost", "ListPrice"])
    writer.writerows(products)

# 3. Dimension: Regions
regions = [
    ("REG-01", "East", "United States", "Sarah Jenkins"),
    ("REG-02", "West", "United States", "Marcus Vance"),
    ("REG-03", "Central", "United States", "David Chen"),
    ("REG-04", "South", "United States", "Rachel Morales")
]

reg_file = os.path.join(DATA_DIR, "dim_regions.csv")
with open(reg_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["RegionID", "RegionName", "Country", "RegionalManager"])
    writer.writerows(regions)

# Customer to Region mapping for realism
cust_state_map = {c[0]: c[4] for c in customers}
state_to_region = {
    "New York": "REG-01", "Pennsylvania": "REG-01", "Massachusetts": "REG-01",
    "California": "REG-02", "Washington": "REG-02", "Oregon": "REG-02", "Colorado": "REG-02", "Arizona": "REG-02",
    "Illinois": "REG-03", "Michigan": "REG-03", "Minnesota": "REG-03",
    "Texas": "REG-04", "Florida": "REG-04", "Georgia": "REG-04"
}

# 4. Fact: Sales Orders
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
total_days = (end_date - start_date).days

fact_rows = []
flat_rows = []

prod_dict = {p[0]: p for p in products}
cust_dict = {c[0]: c for c in customers}
reg_dict = {r[0]: r for r in regions}

order_id_counter = 10001
num_orders = 750

for _ in range(num_orders):
    order_id = f"ORD-{order_id_counter}"
    order_id_counter += 1
    
    # Pick date with seasonal bump in Q4
    rand_day = random.randint(0, total_days)
    order_date = start_date + timedelta(days=rand_day)
    # Seasonal bump in Q4
    if random.random() < 0.25 and order_date.month not in [10, 11, 12]:
        new_month = random.choice([10, 11, 12])
        new_day = min(order_date.day, 28)
        order_date = order_date.replace(month=new_month, day=new_day)
    
    ship_delay = random.randint(1, 5)
    ship_date = order_date + timedelta(days=ship_delay)
    
    cust = random.choice(customers)
    cust_id = cust[0]
    cust_state = cust[4]
    reg_id = state_to_region.get(cust_state, "REG-01")
    
    # 1 to 3 items per order
    num_items = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]
    chosen_prods = random.sample(products, num_items)
    
    for item_idx, prod in enumerate(chosen_prods, start=1):
        line_item_id = f"{order_id}-{item_idx}"
        prod_id = prod[0]
        cost = prod[4]
        price = prod[5]
        
        # Quantity
        if prod[2] == "Office Supplies":
            qty = random.randint(1, 10)
        elif prod[2] == "Furniture":
            qty = random.randint(1, 4)
        else: # Technology
            qty = random.randint(1, 3)
            
        # Discount: 0%, 5%, 10%, 15%, 20%
        discount_rate = random.choices([0.0, 0.05, 0.10, 0.15, 0.20], weights=[0.45, 0.25, 0.15, 0.10, 0.05])[0]
        
        revenue = round(qty * price * (1.0 - discount_rate), 2)
        total_cost = round(qty * cost, 2)
        profit = round(revenue - total_cost, 2)
        
        fact_rows.append([
            line_item_id,
            order_id,
            order_date.strftime("%Y-%m-%d"),
            ship_date.strftime("%Y-%m-%d"),
            cust_id,
            prod_id,
            reg_id,
            qty,
            price,
            discount_rate,
            revenue,
            total_cost,
            profit
        ])
        
        # Flat row for single-table beginner mode
        flat_rows.append([
            line_item_id,
            order_id,
            order_date.strftime("%Y-%m-%d"),
            ship_date.strftime("%Y-%m-%d"),
            cust_id,
            cust[1], # CustomerName
            cust[2], # Segment
            cust[3], # City
            cust[4], # State
            cust[5], # Country
            prod_id,
            prod[1], # ProductName
            prod[2], # Category
            prod[3], # SubCategory
            reg_id,
            reg_dict[reg_id][1], # RegionName
            reg_dict[reg_id][3], # RegionalManager
            qty,
            price,
            discount_rate,
            revenue,
            total_cost,
            profit
        ])

# Write Fact Sales
fact_file = os.path.join(DATA_DIR, "fact_sales.csv")
with open(fact_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "LineItemID", "OrderID", "OrderDate", "ShipDate", "CustomerID", 
        "ProductID", "RegionID", "Quantity", "UnitPrice", "Discount", 
        "Revenue", "TotalCost", "Profit"
    ])
    writer.writerows(fact_rows)

# Write Flat Sales
flat_file = os.path.join(DATA_DIR, "sales_data_flat.csv")
with open(flat_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "LineItemID", "OrderID", "OrderDate", "ShipDate", "CustomerID", 
        "CustomerName", "Segment", "City", "State", "Country", 
        "ProductID", "ProductName", "Category", "SubCategory", 
        "RegionID", "RegionName", "RegionalManager", "Quantity", 
        "UnitPrice", "Discount", "Revenue", "TotalCost", "Profit"
    ])
    writer.writerows(flat_rows)

print(f"Generated {len(customers)} customers.")
print(f"Generated {len(products)} products.")
print(f"Generated {len(regions)} regions.")
print(f"Generated {len(fact_rows)} sales line items across {num_orders} orders.")
print("All CSV files successfully created in data/ folder!")
