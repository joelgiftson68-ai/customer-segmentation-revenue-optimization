# customer-segmentation-revenue-optimization
RFM-based Customer Segmentation &amp; Revenue Optimization Analysis using Python, SQL, Pandas and Excel.

Customer Segmentation & Revenue Optimization Analysis

Python
Pandas
SQL
Excel
Status

Project Overview

This portfolio project demonstrates an end-to-end customer analytics and revenue optimization workflow using RFM (Recency, Frequency, Monetary) segmentation.

The analysis converts raw retail transaction data into actionable customer segments so a business can answer questions such as:

• Who are the highest-value customers?
• Which customers are most likely to need retention attention?
• Which customers should receive loyalty or win-back campaigns?
• How concentrated is revenue among the highest-value customers?
• Which customer segments contribute the most revenue?
• What actions could improve repeat purchases and average order value?

> **Dataset note:** This repository uses a synthetic retail dataset created specifically for portfolio demonstration. It contains no real customer or company information. Business recommendations demonstrate the analytical method and do not claim a measured real-world revenue uplift.

────────

Business Objective

Build a repeatable customer segmentation framework that helps marketing, CRM, sales, and management teams prioritize customers based on purchasing behavior.

The project focuses on four business outcomes:

1. Customer targeting — identify the right audience for each campaign.
2. Retention — detect high-value customers who may be becoming inactive.
3. Revenue optimization — identify cross-sell, loyalty, and reactivation opportunities.
4. Decision support — communicate customer behavior through KPIs, charts, SQL queries, and an Excel dashboard.

────────

Dataset

The synthetic transaction dataset contains:

|Metric            |Value                   |
|------------------|-----------------------:|
|Transaction lines |22,787                  |
|Distinct orders   |9,073                   |
|Customers         |1,000                   |
|Countries         |8                       |
|Product categories|6                       |
|Date range        |2024-01-01 to 2025-12-31|

Main Fields

OrderID, CustomerID, OrderDate, Country, CustomerType, Channel, ProductCategory, Quantity, UnitPrice, Discount, and Revenue.

────────

Tech Stack

• Python — data preparation, RFM scoring, segmentation and analysis
• Pandas / NumPy — data manipulation and feature engineering
• Matplotlib — analytical visualizations
• SQL — KPI, customer, country, category and retention analysis
• Excel — management-style dashboard workbook and analytical tables
• Jupyter Notebook — documented end-to-end analysis
• Git / GitHub — portfolio project version control

────────

RFM Methodology

RFM is a behavioral segmentation framework based on three dimensions:

• Recency (R): How recently did the customer purchase?
• Frequency (F): How often did the customer purchase?
• Monetary (M): How much revenue did the customer generate?

Each customer receives a score from 1 to 5 for each dimension. For recency, a smaller number of days since the last purchase is better; for frequency and monetary value, higher values are better.

The scores are translated into practical segments:

• Champions
• Loyal Customers
• Potential Loyalists
• New Customers
• Needs Attention
• Can’t Lose Them
• At Risk
• Hibernating

────────

Key Results

|KPI                                     |Result      |
|----------------------------------------|-----------:|
|Total Revenue                           |5,303,349.32|
|Total Orders                            |9,073       |
|Total Customers                         |1,000       |
|Average Order Value                     |584.52      |
|Repeat Purchase Rate                    |94.30%      |
|Revenue from Top 20% of Customers       |52.26%      |
|Champion Revenue                        |2,240,602.73|
|Revenue associated with At-Risk segments|554,946.34  |

Segment Performance

|Segment            |Customers|Revenue     |Revenue Share|
|-------------------|--------:|-----------:|------------:|
|Champions          |189      |2,240,602.73|42.25%       |
|Loyal Customers    |123      |1,085,954.50|20.48%       |
|Needs Attention    |172      |893,573.21  |16.85%       |
|At Risk            |185      |461,422.75  |8.70%        |
|Potential Loyalists|90       |270,542.00  |5.10%        |
|Hibernating        |177      |206,979.51  |3.90%        |
|Can’t Lose Them    |14       |93,523.59   |1.76%        |
|New Customers      |50       |50,751.03   |0.96%        |

Major Analytical Findings

1. Champions are the most important segment.
The 189 Champion customers contribute 42.25% of total revenue. This supports VIP treatment, referral programs, early product access and premium retention activity.

2. Revenue is meaningfully concentrated.
The top 20% of customers generate approximately 52.26% of revenue. Retention activity should therefore prioritize customer value rather than treating every customer identically.

3. Revenue at risk is commercially important.
Customers classified as At Risk or Can’t Lose Them account for approximately 554,946.34 in historical customer value. These groups are strong candidates for targeted win-back campaigns.

4. Potential Loyalists are an expansion opportunity.
This group is relatively recent but has not yet reached the purchase frequency of Loyal or Champion customers. Personalized cross-sell, bundles, second/third-purchase incentives, and loyalty onboarding can help move them upward.

5. New and Hibernating customers need different treatment.
New customers should receive onboarding and repeat-purchase journeys, while Hibernating customers are better suited to lower-cost re-engagement to avoid overspending on low-probability conversions.

────────

Recommended Campaign Strategy

|Segment            |Recommended Action                                             |
|-------------------|---------------------------------------------------------------|
|Champions          |VIP rewards, early access, referral campaigns                  |
|Loyal Customers    |Loyalty points, bundles, subscription or reorder offers        |
|Potential Loyalists|Cross-sell and repeat-purchase incentives                      |
|New Customers      |Welcome journey, onboarding offers, product education          |
|Needs Attention    |Personalized reminders and category-based promotions           |
|Can’t Lose Them    |Priority win-back outreach and high-value retention offers     |
|At Risk            |Time-bound reactivation campaigns                              |
|Hibernating        |Low-cost re-engagement and suppression rules for non-responders|

────────

Dashboard

The Excel workbook contains a management-style dashboard, transaction-level data, RFM customer output, segment summaries, monthly trends, category performance and country performance.

Excel Dashboard

────────

Visualizations

Customer Count by Segment

Customer Segments

Revenue by Segment

Revenue by Segment

RFM Distribution

RFM Distribution

Top Customers

Top Customers

────────

Repository Structure

```text
customer-segmentation-revenue-optimization/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── data/
│   ├── customer_transactions.csv
│   ├── rfm_customer_segments.csv
│   ├── segment_summary.csv
│   ├── monthly_revenue.csv
│   ├── category_summary.csv
│   ├── country_summary.csv
│   └── DATA_DICTIONARY.md
│
├── notebooks/
│   └── customer_segmentation_analysis.ipynb
│
├── sql/
│   └── customer_analysis.sql
│
├── src/
│   └── rfm_analysis.py
│
├── dashboard/
│   └── customer_segmentation_dashboard.xlsx
│
└── images/
    ├── excel_dashboard_preview.png
    ├── customer_segments.png
    ├── revenue_by_segment.png
    ├── rfm_distribution.png
    └── top_customers.png
```

────────

How to Run

1. Clone the repository

```bash
git clone <your-github-repository-url>
cd customer-segmentation-revenue-optimization
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the Python pipeline

```bash
python src/rfm_analysis.py
```

5. Open the notebook

```bash
jupyter notebook notebooks/customer_segmentation_analysis.ipynb
```

────────

SQL Analysis

sql/customer_analysis.sql includes queries for:

• Core customer and revenue KPIs
• Revenue by country
• Product-category performance
• Monthly revenue trends
• Customer-level RFM aggregation
• Segment performance
• Revenue-at-risk analysis
• Top customer identification
• Segment-by-country opportunity analysis
• Average order value by channel

────────

Skills Demonstrated

Relevant to Data Analyst, Business Analyst, Junior Data Scientist, MIS/Reporting Analyst and analytics-oriented IT roles:

• Data cleaning and validation
• Exploratory data analysis
• Customer analytics
• RFM feature engineering
• Quantile-based scoring
• Business segmentation
• KPI development
• SQL analytics
• Data visualization
• Excel dashboarding
• Translating analysis into business recommendations
• GitHub project documentation
