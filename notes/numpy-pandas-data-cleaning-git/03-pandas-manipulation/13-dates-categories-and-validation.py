"""Datetime, categorical data, and analytical validation.

Commit message: Add Week 3 Pandas dates categories and validation notes

Dates and categories carry domain meaning that should be represented in the
DataFrame schema rather than handled as unstructured strings.
"""

import pandas as pd


events = pd.DataFrame(
    {
        "event_id": [1, 2, 3, 4, 5],
        "event_time": [
            "2026-01-03 09:15",
            "2026-01-10 14:30",
            "invalid-date",
            "2026-02-02 08:00",
            "2026-02-18 17:45",
        ],
        "priority": ["low", "high", "medium", "high", "low"],
        "status": ["open", "closed", "open", "pending", "closed"],
        "revenue": [20.0, 80.0, 35.0, 60.0, 45.0],
    }
)


# 1. Parse dates explicitly and inspect conversion failures
events["event_time"] = pd.to_datetime(events["event_time"], errors="coerce")
print("parsed event times:\n", events["event_time"])
print("invalid date count:", events["event_time"].isna().sum())


# 2. Extract time features
events = events.assign(
    event_date=events["event_time"].dt.date,
    event_month=events["event_time"].dt.to_period("M"),
    event_day_name=events["event_time"].dt.day_name(),
    event_hour=events["event_time"].dt.hour,
)
print("events with time features:\n", events)


# 3. Time-aware filtering
february_events = events.loc[
    events["event_time"].between("2026-02-01", "2026-02-28")
]
print("February events:\n", february_events)


# 4. Ordered categorical data
priority_dtype = pd.CategoricalDtype(
    categories=["low", "medium", "high"],
    ordered=True,
)
events["priority"] = events["priority"].astype(priority_dtype)
events["status"] = events["status"].astype("category")

print("priority dtype:", events["priority"].dtype)
print("status dtype:", events["status"].dtype)
print("events sorted by priority:\n", events.sort_values("priority"))


# 5. Category-aware grouping
priority_summary = (
    events.groupby("priority", observed=True, as_index=False)
    .agg(
        event_count=("event_id", "count"),
        revenue=("revenue", "sum"),
    )
)
print("priority summary:\n", priority_summary)


# 6. Schema and business-rule checks
assert events["event_id"].is_unique
assert events["revenue"].ge(0).all()
assert events["priority"].isin(["low", "medium", "high"]).all()
assert events["status"].notna().all()

required_columns = {
    "event_id",
    "event_time",
    "priority",
    "status",
    "revenue",
}
assert required_columns.issubset(events.columns)

print("schema and business-rule checks passed")


# Important notes
# - errors="coerce" makes invalid dates visible as NaT instead of hiding them.
# - Datetime accessors provide consistent time features for analysis.
# - Ordered categories support meaningful sorting and controlled values.
# - observed=True excludes unused categorical combinations from group results.
# - Assertions turn data assumptions into executable checks.
