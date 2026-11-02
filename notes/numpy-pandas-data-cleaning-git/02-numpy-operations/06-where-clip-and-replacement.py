"""Conditional replacement and value clipping.

Commit message: Add Week 2 NumPy conditional replacement notes

NumPy can replace values according to conditions without writing explicit
element-by-element Python loops.
"""

import numpy as np


# 1. Binary replacement with np.where()
temperatures = np.array([12, 19, 24, 31, 8, 27])
temperature_labels = np.where(temperatures >= 20, "warm", "cool")

print("temperatures:", temperatures)
print("temperature labels:", temperature_labels)


# 2. Numeric replacement
scores = np.array([35, 48, 72, 91, 24, 66])
adjusted_scores = np.where(scores < 40, 40, scores)

print("original scores:", scores)
print("scores with a floor of 40:", adjusted_scores)


# 3. Replacing invalid values
measurements = np.array([10.5, -2.0, 7.3, np.nan, 12.1, -1.0])
valid_measurements = np.where(
    np.isnan(measurements) | (measurements < 0),
    0.0,
    measurements,
)

print("measurements:", measurements)
print("invalid measurements replaced with zero:", valid_measurements)


# 4. Multiple conditions with np.select()
ages = np.array([7, 16, 25, 42, 68])
age_categories = np.select(
    [
        ages < 13,
        ages < 18,
        ages < 65,
    ],
    [
        "child",
        "teenager",
        "adult",
    ],
    default="senior",
)

print("ages:", ages)
print("age categories:", age_categories)


# 5. Clipping values to lower and upper limits
raw_percentages = np.array([-10, 0, 42, 87, 105, 130])
bounded_percentages = np.clip(raw_percentages, 0, 100)

print("raw percentages:", raw_percentages)
print("bounded percentages:", bounded_percentages)


# 6. Clipping a matrix
matrix = np.array(
    [
        [4, 12, 28],
        [35, 7, 19],
    ]
)
limited_matrix = np.clip(matrix, 10, 25)

print("original matrix:\n", matrix)
print("matrix clipped to 10 through 25:\n", limited_matrix)


# Important notes
# - np.where(condition, value_if_true, value_if_false) preserves array shape.
# - np.select() handles ordered multiple conditions.
# - np.clip() changes extreme values but does not remove elements.
# - NaN values require explicit handling; comparisons alone do not classify NaN.
