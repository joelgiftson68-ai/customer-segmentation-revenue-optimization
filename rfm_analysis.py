"""
Customer Segmentation & Revenue Optimization Analysis
RFM segmentation pipeline for portfolio/demo use.

Run:
    python src/rfm_analysis.py
"""

from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
ANALYSIS_DATE = pd.Timestamp("2026-01-01")

def load_transactions(path=DATA_DIR / "customer_transactions.csv"):
    df = pd.read_csv(path, parse_dates=["OrderDate"])
    required = {
        "OrderID","CustomerID","OrderDate","Country","CustomerType","Channel",
        "ProductCategory","Quantity","UnitPrice","Discount","Revenue"
    }
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    return df

def build_rfm(df, analysis_date=ANALYSIS_DATE):
    orders = (
        df.groupby(["OrderID","CustomerID","OrderDate"], as_index=False)["Revenue"]
          .sum()
    )
    rfm = (
        orders.groupby("CustomerID")
        .agg(
            LastPurchaseDate=("OrderDate","max"),
            Frequency=("OrderID","nunique"),
            Monetary=("Revenue","sum"),
        )
        .reset_index()
    )
    rfm["Recency"] = (analysis_date - rfm["LastPurchaseDate"]).dt.days

    # Recency: lower days is better. Frequency/Monetary: higher is better.
    rfm["R_Score"] = pd.qcut(
        rfm["Recency"].rank(method="first", ascending=True),
        5, labels=[5,4,3,2,1]
    ).astype(int)
    rfm["F_Score"] = pd.qcut(
        rfm["Frequency"].rank(method="first"),
        5, labels=[1,2,3,4,5]
    ).astype(int)
    rfm["M_Score"] = pd.qcut(
        rfm["Monetary"].rank(method="first"),
        5, labels=[1,2,3,4,5]
    ).astype(int)
    rfm["RFM_Score"] = (
        rfm["R_Score"].astype(str)
        + rfm["F_Score"].astype(str)
        + rfm["M_Score"].astype(str)
    )

    def assign_segment(row):
        r, f, m = row["R_Score"], row["F_Score"], row["M_Score"]
        if r >= 4 and f >= 4 and m >= 4:
            return "Champions"
        if r >= 3 and f >= 4:
            return "Loyal Customers"
        if r >= 4 and f in [2,3]:
            return "Potential Loyalists"
        if r == 5 and f == 1:
            return "New Customers"
        if r in [2,3] and f >= 3 and m >= 3:
            return "Needs Attention"
        if r <= 2 and f >= 4 and m >= 4:
            return "Can't Lose Them"
        if r <= 2 and f >= 2:
            return "At Risk"
        return "Hibernating"

    rfm["Segment"] = rfm.apply(assign_segment, axis=1)
    rfm["Monetary"] = rfm["Monetary"].round(2)
    return rfm, orders

def build_segment_summary(rfm):
    summary = (
        rfm.groupby("Segment", as_index=False)
        .agg(
            Customers=("CustomerID","nunique"),
            AvgRecencyDays=("Recency","mean"),
            AvgFrequency=("Frequency","mean"),
            TotalRevenue=("Monetary","sum"),
            AvgCustomerValue=("Monetary","mean"),
        )
    )
    summary["CustomerSharePct"] = summary["Customers"] / rfm["CustomerID"].nunique() * 100
    summary["RevenueSharePct"] = summary["TotalRevenue"] / rfm["Monetary"].sum() * 100
    return summary.sort_values("TotalRevenue", ascending=False).round(2)

def main():
    df = load_transactions()
    rfm, orders = build_rfm(df)

    customer_dim = (
        df.sort_values("OrderDate")
          .groupby("CustomerID", as_index=False)
          .agg(Country=("Country","first"), CustomerType=("CustomerType","first"))
    )
    rfm = rfm.merge(customer_dim, on="CustomerID", how="left")
    rfm["RevenueSharePct"] = (rfm["Monetary"] / rfm["Monetary"].sum() * 100).round(4)

    summary = build_segment_summary(rfm)
    rfm.to_csv(DATA_DIR / "rfm_customer_segments.csv", index=False)
    summary.to_csv(DATA_DIR / "segment_summary.csv", index=False)

    total_revenue = orders["Revenue"].sum()
    total_orders = orders["OrderID"].nunique()
    total_customers = rfm["CustomerID"].nunique()
    aov = total_revenue / total_orders
    repeat_rate = (rfm["Frequency"] > 1).mean() * 100

    print(f"Customers: {total_customers:,}")
    print(f"Orders: {total_orders:,}")
    print(f"Revenue: {total_revenue:,.2f}")
    print(f"Average Order Value: {aov:,.2f}")
    print(f"Repeat Purchase Rate: {repeat_rate:.2f}%")
    print("\nSegment Summary")
    print(summary.to_string(index=False))

if __name__ == "__main__":
    main()
