"""NumPy aggregation, reduction, and numerical precision.

Commit message: Add Week 1 NumPy aggregation and precision notes

This file covers summary statistics and the reason small floating-point
differences matter in numerical work.
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("sum:", arr.sum())
print("mean:", arr.mean())
print("std:", arr.std())
print("min:", arr.min())
print("max:", arr.max())

# 2D reduction across axes
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Column sums:", matrix.sum(axis=0))
print("Row sums:", matrix.sum(axis=1))

# np.argmax / np.argmin
print("argmax:", np.argmax(matrix))
print("argmin:", np.argmin(matrix))

# Floating-point precision
x = np.array([0.1, 0.2, 0.3])
print("x:", x)
print("sum(x):", x.sum())
print("Difference from expected:", x.sum() - 0.6)

# Safe float comparison
print("Is x.sum() == 0.6?", np.isclose(x.sum(), 0.6))

# Example of rounding behavior
print("Rounded to 3 decimals:", np.round(x.sum(), 3))

# Important notes
# - reductions summarize data across rows or columns
# - axis=0 reduces across rows and axis=1 reduces across columns
# - np.argmax and np.argmin return positions of max and min values
# - floating-point values do not always represent decimal fractions exactly
# - np.isclose is more reliable than direct equality for float comparisons
