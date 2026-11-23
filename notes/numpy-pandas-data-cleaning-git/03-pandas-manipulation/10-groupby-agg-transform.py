"""Grouped aggregation and row-preserving transformation.

Commit message: Add Week 3 Pandas groupby aggregation and transform notes

Aggregation answers group-level questions. Transformation calculates group
information while retaining one result for every original row.
"""

import pandas as pd


orders = pd.DataFrame(
    {
        "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
        "region": ["North", "South", "North", "West", "South", "North"],
        "product": ["Pen", "Bag", "Pen", "Book", "Bag", "Book"],
        "quantity": [2, 1, 4, 3, 2, 1],
        "revenue": [20.0, 80.0, 40.0, 75.0, 160.0, 30.0],
    }
)


# 1. Basic grouped aggregation
region_summary = (
    orders.groupby("region", as_index=False)
    .agg(
        total_revenue=("revenue", "sum"),
        average_order_value=("revenue", "mean"),
        order_count=("order_id", "nunique"),
        total_units=("quantity", "sum"),
    )
)
print("region summary:\n", region_summary)


# 2. Multiple grouping keys
product_region_summary = (
    orders.groupby(["region", "product"], as_index=False)
    .agg(
        revenue=("revenue", "sum"),
        units=("quantity", "sum"),
    )
    .sort_values(["region", "revenue"], ascending=[True, False])
)
print("product-region summary:\n", product_region_summary)


# 3. Named aggregation keeps output columns explicit
product_summary = orders.groupby("product", as_index=False).agg(
    revenue_total=("revenue", "sum"),
    revenue_median=("revenue", "median"),
    largest_order=("revenue", "max"),
)
print("product summary:\n", product_summary)


# 4. transform() preserves the original row count
orders = orders.assign(
    region_revenue=orders.groupby("region")["revenue"].transform("sum"),
    region_average=orders.groupby("region")["revenue"].transform("mean"),
)
orders["share_of_region_revenue"] = orders["revenue"] / orders["region_revenue"]
print("orders with group-level features:\n", orders)


# 5. Group-relative ranking
orders["rank_in_region"] = orders.groupby("region")["revenue"].rank(
    method="dense",
    ascending=False,
)
print("orders ranked within region:\n", orders.sort_values(["region", "rank_in_region"]))


# 6. Filtering groups by a group-level rule
large_regions = orders.groupby("region")["revenue"].sum()
large_region_names = large_regions[large_regions >= 100].index
large_region_orders = orders[orders["region"].isin(large_region_names)]
print("regions with revenue of at least 100:", large_region_names.tolist())
print("orders from large regions:\n", large_region_orders)


# Important notes
# - agg() reduces each group to one output row per group.
# - transform() returns a Series aligned with the original DataFrame index.
# - Named aggregation avoids ambiguous MultiIndex output columns.
# - Group-relative features are useful for ranking, normalization, and ML
#   feature preparation.
# - Check whether a group key is categorical, missing, or unexpectedly unique.
