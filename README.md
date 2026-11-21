# Real Estate Procurement & Supply Chain Analytics

In real estate construction, keeping track of raw material purchases, vendor payments, and pending deliveries is what keeps sites running on schedule and within budget. This project analyzes **₹96.39 Crores** in historical purchase data across five project sheets (Daivi, Purchase, Skyrise, Fiora, and Aikyam), turning raw multi-sheet Excel exports into a clean dataset, automated Python analysis, SQL queries, and an interactive Power BI dashboard.

## What This Project Covers
- Consolidating 7,629 purchase order records from multiple project sheets into one standardized dataset.
- Cleaning common ERP export issues like trailing spaces, inconsistent casing, missing due dates, blank indent numbers, and negative pending balances.
- Tracking total procurement spend vs. outstanding liabilities across active residential sites.
- Identifying vendor concentration and the material groups driving the bulk of project costs.

## Tools Used
- **Power BI** — Data modeling, DAX measures, and interactive reporting (`PURCHASE DASHBOARD.pbix`)
- **SQL** — Data cleaning, deduplication (CTEs), and business aggregations (Window Functions)
- **Python** — Multi-sheet Excel preprocessing (`pandas`) and exploratory charts (`matplotlib`, `seaborn`)
- **Excel** — Source procurement dataset (`purchase.xlsx`)

## Dashboard Preview
![Dashboard Main View](Images/dashboard_main.png)

*(Download `PURCHASE DASHBOARD.pbix` and open it in Power BI Desktop to explore the interactive filters and visuals.)*

## Key Findings
- **Overall Spend & Liability:** Total procurement value is **₹96.39 Cr**, with **₹4.18 Cr** in pending delivery/payment liability.
- **Top Material Categories:**
  - **Steel:** ₹25.04 Cr
  - **Ready Mix Concrete (RMC):** ₹19.09 Cr
  - **Tiles:** ₹9.08 Cr
  - **Cement:** ₹8.44 Cr
  - **Cables & Wires:** ₹5.82 Cr
- **Site-Wise Spend:** `Shreeji Ganesh-SRA` (₹30.55 Cr) and `Daivi Eterneety` (₹27.27 Cr) account for over half of total material spend, followed by `Shreeji SkyRise` (₹23.88 Cr) and `Shreeji Fiora` (₹14.70 Cr).
- **Supplier Concentration:** The top two vendors (`OM SAI JP ENTERPRISE` at ₹7.78 Cr and `ADR ENTERPRISES` at ₹7.71 Cr) represent over ₹15.49 Cr in combined spend—clear candidates for volume-based rate negotiation.

## Repository Structure
- `PURCHASE DASHBOARD.pbix` — Interactive Power BI dashboard
- `purchase.xlsx` — Raw multi-sheet procurement dataset
- `SQL_Scripts/Data_Cleaning_and_Analysis.sql` — SQL cleaning pipeline and business queries
- `Python_Scripts/01_data_preprocessing.py` — Combines all Excel sheets, cleans text/dates/anomalies, and exports a clean CSV
- `Python_Scripts/02_exploratory_analysis.py` — Generates spend summaries by business unit and plots the top suppliers chart
- `Images/` — Dashboard screenshots and Python-generated charts

## How to Run the Scripts
```bash
cd Python_Scripts
python 01_data_preprocessing.py
python 02_exploratory_analysis.py
```
