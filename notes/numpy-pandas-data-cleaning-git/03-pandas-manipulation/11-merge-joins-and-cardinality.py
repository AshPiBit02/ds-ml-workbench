"""Merging tables, join cardinality, and post-join validation.

Commit message: Add Week 3 Pandas joins and cardinality notes

Joins are a common source of silent row multiplication. Key uniqueness and
row-count checks should be explicit parts of an analytical workflow.
"""

import pandas as pd


orders = pd.DataFrame(
    {
        "order_id": [1001, 1002, 1003, 1004],
        "customer_id": ["C01", "C02", "C01", "C03"],
        "revenue": [20.0, 80.0, 40.0, 75.0],
    }
)

customers = pd.DataFrame(
    {
        "customer_id": ["C01", "C02", "C03", "C04"],
        "customer_name": ["Asha", "Ravi", "Mina", "Noah"],
        "segment": ["retail", "business", "retail", "business"],
    }
)


# 1. Validate key uniqueness before a many-to-one merge
print("order IDs unique:", orders["order_id"].is_unique)
print("customer IDs unique in customer table:", customers["customer_id"].is_unique)

enriched_orders = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one",
    indicator=True,
)
print("enriched orders:\n", enriched_orders)
print("join indicators:\n", enriched_orders["_merge"].value_counts())


# 2. Compare row counts before and after the join
print("orders before merge:", len(orders))
print("orders after merge:", len(enriched_orders))
assert len(enriched_orders) == len(orders)


# 3. Inner and outer joins answer different questions
inner_join = orders.merge(customers, on="customer_id", how="inner")
outer_join = orders.merge(customers, on="customer_id", how="outer", indicator=True)

print("inner join:\n", inner_join)
print("outer join:\n", outer_join)


# 4. Joining on different key names
customer_targets = pd.DataFrame(
    {
        "customer_code": ["C01", "C02", "C03"],
        "target_revenue": [50.0, 100.0, 60.0],
    }
)
orders_with_targets = orders.merge(
    customer_targets,
    left_on="customer_id",
    right_on="customer_code",
    how="left",
    validate="many_to_one",
)
print("orders with targets:\n", orders_with_targets)


# 5. Detecting duplicate keys that would multiply rows
duplicate_customer_rows = pd.DataFrame(
    {
        "customer_id": ["C01", "C01", "C02"],
        "region": ["North", "Central", "South"],
    }
)

try:
    orders.merge(
        duplicate_customer_rows,
        on="customer_id",
        how="left",
        validate="many_to_one",
    )
except pd.errors.MergeError as error:
    print("expected cardinality validation error:", error)

duplicated_keys = duplicate_customer_rows.loc[
    duplicate_customer_rows["customer_id"].duplicated(keep=False),
    "customer_id",
]
print("duplicate customer keys:", duplicated_keys.unique().tolist())


# Important notes
# - many_to_one means many left rows may match one right row.
# - validate= prevents accidental many-to-many joins from going unnoticed.
# - indicator=True exposes unmatched keys and supports reconciliation.
# - A left join preserves left rows only when the right key is unique.
# - Compare business totals before and after merging, not only row counts.
