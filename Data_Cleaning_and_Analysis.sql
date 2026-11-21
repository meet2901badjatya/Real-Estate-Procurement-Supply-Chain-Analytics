-- Data Cleaning
UPDATE purchases
SET 
    Supplier = UPPER(TRIM(Supplier)),
    "Item  Group" = UPPER(TRIM("Item  Group")),
    "Business Unit" = TRIM("Business Unit"),
    "Item Name" = TRIM("Item Name");

UPDATE purchases
SET "Due Date" = DATE_ADD("Document Date", INTERVAL 15 DAY)
WHERE "Due Date" IS NULL;

UPDATE purchases
SET "Indent No" = 'NO_INDENT'
WHERE "Indent No" IS NULL;

UPDATE purchases
SET 
    "Pending Qty" = 0, 
    "Pending Amount" = 0
WHERE "Pending Qty" < 0 OR "Pending Amount" < 0;

WITH DuplicateRecords AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY "Document No", "Item Code", "Supplier", "Amount" 
               ORDER BY "Document Date"
           ) AS row_num
    FROM purchases
)
DELETE FROM purchases
WHERE "Document No" IN (SELECT "Document No" FROM DuplicateRecords WHERE row_num > 1);

-- Top 5 Suppliers by Spend
WITH SupplierSpend AS (
    SELECT 
        Supplier, 
        SUM(Amount) AS Total_Amount
    FROM purchases
    GROUP BY Supplier
)
SELECT 
    Supplier, 
    Total_Amount,
    DENSE_RANK() OVER (ORDER BY Total_Amount DESC) AS Spend_Rank
FROM SupplierSpend
LIMIT 5;

-- Spend and Liability by Item Group
SELECT 
    "Item  Group",
    COUNT(DISTINCT "Document No") AS Total_Orders,
    SUM(Amount) AS Total_Spend,
    SUM("Pending Amount") AS Total_Liability
FROM purchases
GROUP BY "Item  Group"
ORDER BY Total_Spend DESC;

-- Pending Liability by Business Unit
SELECT 
    "Business Unit",
    SUM(Amount) AS Total_Ordered_Value,
    SUM("Pending Amount") AS Total_Liability,
    ROUND((SUM("Pending Amount") / SUM(Amount)) * 100, 2) AS Liability_Percentage
FROM purchases
WHERE "Pending Amount" > 0
GROUP BY "Business Unit"
ORDER BY Total_Liability DESC;

-- GRN Fulfillment Rate
SELECT 
    "Document No",
    Supplier,
    "PO Qty",
    "GRN Qty",
    CASE 
        WHEN "PO Qty" = 0 THEN 0 
        ELSE ROUND(("GRN Qty" * 100.0) / "PO Qty", 2) 
    END AS Fulfillment_Percentage
FROM purchases
WHERE "PO Qty" > 0;
