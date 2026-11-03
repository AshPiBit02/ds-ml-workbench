# Pandas Week 3 Notes

## Purpose

This folder covers practical Pandas manipulation for tabular data: Series and
DataFrames, reliable selection, method chaining, grouped analysis, joins,
concatenation, reshaping, dates, categorical data, and validation of results.

The basic API is introduced briefly, while the examples emphasize patterns
used in exploratory analysis, reporting, feature preparation, and production
data workflows.

## Learning goals

- Choose between `Series` and `DataFrame` representations.
- Select rows and columns safely with `.loc[]` and `.iloc[]`.
- Build readable filtering pipelines with vectorized expressions and
  method chaining.
- Distinguish grouped aggregation from row-preserving transformation.
- Join tables deliberately and verify join cardinality and row counts.
- Reshape data between wide and long forms with `pivot`, `pivot_table`, and
  `melt`.
- Parse dates, extract time features, and use time-aware filtering.
- Use categorical data intentionally for consistency and memory efficiency.
- Validate assumptions about keys, duplicates, missing values, and output
  shape after each important operation.

## Recommended order

1. `09-series-dataframes-selection.py`
2. `10-groupby-agg-transform.py`
3. `11-merge-joins-and-cardinality.py`
4. `12-concat-reshape-and-tidy-data.py`
5. `13-dates-categories-and-validation.py`

## Core workflow

```text
inspect
  -> select
  -> filter
  -> transform
  -> aggregate
  -> join or reshape
  -> validate
  -> communicate
```

## Important distinctions

- `.loc[]` uses labels; `.iloc[]` uses integer positions.
- `agg()` reduces rows within groups; `transform()` returns one value per
  original row.
- `merge()` combines columns using keys; `concat()` appends or stacks objects.
- `pivot()` requires unique index-column combinations; `pivot_table()` can
  aggregate duplicates.
- A left join preserves the left table's rows, but duplicate keys can still
  multiply rows.
- Datetime and categorical columns should be represented with meaningful
  dtypes instead of remaining as generic strings or objects.

## Commit message

Add Week 3 Pandas manipulation overview and roadmap notes
