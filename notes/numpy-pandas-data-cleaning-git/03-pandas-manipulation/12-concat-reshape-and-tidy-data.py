"""Concatenation, reshaping, and tidy-data transformations.

Commit message: Add Week 3 Pandas concatenation and reshaping notes

Real datasets frequently move between event-level long form and report-level
wide form. Reshaping choices should preserve identifiers and totals.
"""

import pandas as pd


first_batch = pd.DataFrame(
    {
        "order_id": [1001, 1002],
        "region": ["North", "South"],
        "revenue": [20.0, 80.0],
    }
)
second_batch = pd.DataFrame(
    {
        "order_id": [1003, 1004],
        "region": ["North", "West"],
        "revenue": [40.0, 75.0],
    }
)


# 1. Row-wise concatenation
all_orders = pd.concat([first_batch, second_batch], ignore_index=True)
print("row-wise concatenation:\n", all_orders)


# 2. Column-wise concatenation by index
customer_details = pd.DataFrame(
    {
        "customer": ["Asha", "Ravi", "Mina", "Noah"],
    },
    index=[1001, 1002, 1003, 1004],
)
orders_with_customers = pd.concat(
    [all_orders.set_index("order_id"), customer_details],
    axis=1,
)
print("column-wise concatenation:\n", orders_with_customers)


# 3. Long-form data
monthly_sales = pd.DataFrame(
    {
        "region": ["North", "North", "South", "South"],
        "month": ["Jan", "Feb", "Jan", "Feb"],
        "revenue": [100.0, 120.0, 80.0, 95.0],
    }
)


# 4. pivot() requires unique index-column combinations
wide_sales = monthly_sales.pivot(
    index="region",
    columns="month",
    values="revenue",
)
print("wide sales:\n", wide_sales)


# 5. pivot_table() aggregates duplicate combinations
sales_with_duplicate = pd.concat(
    [
        monthly_sales,
        pd.DataFrame({"region": ["North"], "month": ["Jan"], "revenue": [30.0]}),
    ],
    ignore_index=True,
)
wide_sales_aggregated = sales_with_duplicate.pivot_table(
    index="region",
    columns="month",
    values="revenue",
    aggfunc="sum",
    fill_value=0,
)
print("aggregated wide sales:\n", wide_sales_aggregated)


# 6. Wide-to-long conversion with melt()
wide_metrics = pd.DataFrame(
    {
        "region": ["North", "South"],
        "revenue": [220.0, 175.0],
        "orders": [12, 9],
    }
)
long_metrics = wide_metrics.melt(
    id_vars="region",
    var_name="metric",
    value_name="value",
)
print("long metrics:\n", long_metrics)


# 7. Validate totals after reshaping
long_revenue_total = monthly_sales["revenue"].sum()
wide_revenue_total = wide_sales.to_numpy().sum()
print("long-form total:", long_revenue_total)
print("wide-form total:", wide_revenue_total)
assert long_revenue_total == wide_revenue_total


# Important notes
# - concat(axis=0) appends rows; concat(axis=1) aligns columns by index.
# - ignore_index=True creates a fresh sequential index after row appends.
# - pivot() fails when one cell represents multiple source rows.
# - pivot_table() resolves duplicate combinations through aggregation.
# - melt() produces tidy long form: one observation per row.
# - Preserve identifiers and reconcile totals after every reshape.
