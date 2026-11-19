// ==============================================================================
// POWER QUERY (M) RECIPES & TRANSFORMATIONS
// ==============================================================================
// These code snippets show how Power Query cleans, transforms, and types
// your dataset automatically. You can review them in the "Advanced Editor"
// in Power Query.
// ==============================================================================

// ------------------------------------------------------------------------------
// 1. FACT SALES: Load, Promote Headers, Set Data Types, Add Shipping Days
// ------------------------------------------------------------------------------
let
    // Load CSV from file path (replace path with your actual local file path if needed)
    Source = Csv.Document(File.Contents("c:\Users\ashfa\Desktop\My_Project\Retail-Sales-Performance-Analytics\data\fact_sales.csv"), [Delimiter=",", Columns=13, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    
    // Promote first row to column headers
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    
    // Set appropriate data types for accurate calculations
    ChangedType = Table.TransformColumnTypes(PromotedHeaders, {
        {"LineItemID", type text},
        {"OrderID", type text},
        {"OrderDate", type date},
        {"ShipDate", type date},
        {"CustomerID", type text},
        {"ProductID", type text},
        {"RegionID", type text},
        {"Quantity", Int64.Type},
        {"UnitPrice", Currency.Type},
        {"Discount", type number},
        {"Revenue", Currency.Type},
        {"TotalCost", Currency.Type},
        {"Profit", Currency.Type}
    }),
    
    // Add custom column: Delivery Lead Time (Days between Order and Shipment)
    AddedShippingDays = Table.AddColumn(ChangedType, "ShippingDays", each Duration.Days([ShipDate] - [OrderDate]), Int64.Type)
in
    AddedShippingDays


// ------------------------------------------------------------------------------
// 2. DIM CUSTOMERS: Data Cleansing & Text Trimming
// ------------------------------------------------------------------------------
let
    Source = Csv.Document(File.Contents("c:\Users\ashfa\Desktop\My_Project\Retail-Sales-Performance-Analytics\data\dim_customers.csv"), [Delimiter=",", Columns=7, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedType = Table.TransformColumnTypes(PromotedHeaders, {
        {"CustomerID", type text},
        {"CustomerName", type text},
        {"Segment", type text},
        {"City", type text},
        {"State", type text},
        {"Country", type text},
        {"PostalCode", type text}
    }),
    // Trim extra spaces from customer names
    TrimmedNames = Table.TransformColumns(ChangedType, {{"CustomerName", Text.Trim, type text}})
in
    TrimmedNames


// ------------------------------------------------------------------------------
// 3. DIM PRODUCTS: Categorization and Price Typing
// ------------------------------------------------------------------------------
let
    Source = Csv.Document(File.Contents("c:\Users\ashfa\Desktop\My_Project\Retail-Sales-Performance-Analytics\data\dim_products.csv"), [Delimiter=",", Columns=6, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedType = Table.TransformColumnTypes(PromotedHeaders, {
        {"ProductID", type text},
        {"ProductName", type text},
        {"Category", type text},
        {"SubCategory", type text},
        {"StandardCost", Currency.Type},
        {"ListPrice", Currency.Type}
    })
in
    ChangedType
