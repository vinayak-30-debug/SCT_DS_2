# Supermarket Sales Analysis with AI

## AICTE Internship Project

**Program:** IBM SkillsBuild Data Analytics with AI Academic Internship Program  
**Conducted by:** BharatCares in association with AICTE  
**Student:** Dasarla Vinayak

## Project Overview

This project analyzes 500 supermarket transactions to identify sales trends, product and category performance, branch performance, customer behavior, payment preferences, and ratings. It also includes an AI component using K-Means clustering to segment transactions into lower-, mid-, and higher-value groups based on Quantity, Unit Price, Rating, and Sales.

## Dataset

The project uses the provided `supermarket_sales_500_rows.csv` dataset. It contains 500 transaction records and 13 original columns, covering transactions dated from 1 January 2026 to 1 July 2026.

**Dataset:** `supermarket_sales_500_rows.csv` (provided as part of the internship project materials)

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- Microsoft Word

## Analysis Performed

1. Dataset loading and inspection
2. Data type validation and date conversion
3. Missing-value and duplicate checks
4. Sales formula validation
5. Descriptive statistics
6. Branch and city analysis
7. Product and category analysis
8. Payment method analysis
9. Customer type and gender analysis
10. Monthly sales trend analysis
11. Customer rating analysis
12. K-Means transaction segmentation

## Key Results

- **Total sales:** ₹244,411.08
- **Average transaction:** ₹488.82
- **Highest-sales branch:** Branch C — Mumbai (₹72,469.45)
- **Highest-sales category:** Beverages (₹56,108.24)
- **Highest-sales product:** Cheese (₹27,906.30)
- **Most-used payment method:** UPI (127 transactions)
- **Average rating:** 3.99/5
- **Missing values:** 0
- **Duplicate invoice IDs:** 0

## Project Structure

```text
AICTE_Supermarket_Sales_Analysis/
├── Vinayak_Dasarla_SupermarketSalesAnalysis.ipynb
├── Vinayak_Dasarla_ProjectReport.docx
├── requirements.txt
└── README.md
```

## How to Run

1. Place `supermarket_sales_500_rows.csv` in the same folder as the notebook.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Open the notebook:

```bash
jupyter notebook Vinayak_Dasarla_SupermarketSalesAnalysis.ipynb
```

4. Run all cells from top to bottom.

## AI Component

The dataset does not contain a persistent customer identifier. Therefore, K-Means is applied to **transactions**, rather than claiming to segment individual customers. The model uses Quantity, Unit Price, Rating, and Sales after feature standardization.

## Author

**Dasarla Vinayak**  
GitHub: https://github.com/vinayak-30-debug
