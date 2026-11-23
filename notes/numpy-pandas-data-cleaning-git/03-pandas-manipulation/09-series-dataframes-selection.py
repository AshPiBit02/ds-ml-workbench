"""Series, DataFrames, selection, and method chaining.

Commit message: Add Week 3 Pandas structures and selection notes

The examples use a small order table to demonstrate patterns that transfer to
larger analytical datasets.
"""

import pandas as pd


orders = pd.DataFrame(
    {
        "order_id": [1001, 1002, 1003, 1004, 1005],
        "customer": ["Asha", "Ravi", "Asha", "Mina", "Ravi"],
        "region": ["North", "South", "North", "West", "South"],
        "quantity": [2, 1, 4, 3, 2],
        "unit_price": [25.0, 80.0, 15.0, 40.0, 55.0],
        "status": ["shipped", "pending", "shipped", "cancelled", "shipped"],
    }
)


# 1. Series and DataFrame basics
quantity_series = orders["quantity"]
selected_columns = orders[["order_id", "customer", "quantity"]]

print("Series:\n", quantity_series)
print("Series dtype:", quantity_series.dtype)
print("DataFrame shape:", orders.shape)
print("selected columns:\n", selected_columns)


# 2. Label-based and position-based selection
print("row with label 2:\n", orders.loc[2])
print("rows 1 through 3:\n", orders.loc[1:3])
print("first two rows:\n", orders.iloc[:2])
print("rows 0 and 3, selected columns:\n", orders.loc[[0, 3], ["order_id", "status"]])
print("first row, first three columns:\n", orders.iloc[0, :3])


# 3. Vectorized calculated columns
orders = orders.assign(
    revenue=orders["quantity"] * orders["unit_price"],
    is_complete=orders["status"].eq("shipped"),
)
print("orders with calculated columns:\n", orders)


# 4. Boolean filtering with explicit conditions
completed_orders = orders.loc[
    orders["status"].eq("shipped") & orders["revenue"].ge(50)
]
print("completed orders with revenue at least 50:\n", completed_orders)


# 5. Method chaining for a readable analysis pipeline
regional_revenue = (
    orders.loc[orders["status"].ne("cancelled")]
    .assign(revenue=lambda frame: frame["quantity"] * frame["unit_price"])
    .groupby("region", as_index=False)
    .agg(total_revenue=("revenue", "sum"), order_count=("order_id", "nunique"))
    .sort_values("total_revenue", ascending=False)
)
print("regional revenue:\n", regional_revenue)


# 6. Index management
indexed_orders = orders.set_index("order_id")
print("order 1003:\n", indexed_orders.loc[1003])
restored_orders = indexed_orders.reset_index()
print("restored columns:", restored_orders.columns.tolist())


# Important notes
# - Use a Series for one labeled column and a DataFrame for tabular data.
# - .loc[] selects labels; .iloc[] selects integer positions.
# - Use .loc[mask] rather than chained indexing for predictable assignment.
# - assign() and method chaining make derived-column pipelines easier to audit.
# - Index values are labels, not automatically row numbers after transformations.
