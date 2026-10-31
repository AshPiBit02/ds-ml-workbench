"""Views, copies, and axis-based operations.

Commit message: Add Week 2 NumPy views copies and axis notes

Understanding whether an operation shares storage with an original array
prevents accidental mutation during data preparation.
"""

import numpy as np


# 1. A slice commonly creates a view
source = np.array([10, 20, 30, 40, 50])
slice_view = source[1:4]
slice_view[0] = 999

print("source after changing the slice:", source)
print("slice view:", slice_view)
print("slice shares memory:", np.shares_memory(source, slice_view))


# 2. Fancy indexing commonly creates a copy
source = np.array([10, 20, 30, 40, 50])
selected_copy = source[[1, 2, 3]]
selected_copy[0] = 999

print("source after changing fancy-indexed data:", source)
print("fancy-indexed data:", selected_copy)
print("fancy-indexed data shares memory:", np.shares_memory(source, selected_copy))


# 3. copy() creates independent storage
source = np.array([10, 20, 30, 40, 50])
independent_copy = source[1:4].copy()
independent_copy[0] = 999

print("source after changing an explicit copy:", source)
print("independent copy:", independent_copy)
print("explicit copy shares memory:", np.shares_memory(source, independent_copy))


# 4. Axis-based aggregation
measurements = np.array(
    [
        [12, 15, 18],
        [20, 22, 24],
        [30, 28, 26],
    ]
)

column_means = measurements.mean(axis=0)
row_means = measurements.mean(axis=1)
column_totals = measurements.sum(axis=0)
row_totals = measurements.sum(axis=1)

print("measurements:\n", measurements)
print("column means:", column_means)
print("row means:", row_means)
print("column totals:", column_totals)
print("row totals:", row_totals)


# 5. Axis-based sorting
sorted_rows = np.sort(measurements, axis=1)
sorted_columns = np.sort(measurements, axis=0)

print("each row sorted:\n", sorted_rows)
print("each column sorted:\n", sorted_columns)


# 6. Filtering rows and preserving two-dimensional structure
row_totals = measurements.sum(axis=1)
above_threshold = measurements[row_totals > 60]

print("row totals above 60:", row_totals[row_totals > 60])
print("rows with totals above 60:\n", above_threshold)


# Important notes
# - A view shares underlying data; changing it can change the source array.
# - copy() is appropriate when independent mutation is required.
# - axis=0 reduces rows and produces one result per column.
# - axis=1 reduces columns and produces one result per row.
# - Always check shape when combining masks, indexing, and reductions.
