"""NumPy indexing, slicing, and boolean masks.

Commit message: Add Week 1 NumPy indexing and slicing notes

This file focuses on selecting values from arrays and filtering data efficiently.
"""

import numpy as np

# 1D indexing
arr = np.array([10, 20, 30, 40, 50])
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice:", arr[1:4])

# 2D indexing
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Entire matrix:\n", matrix)
print("Row 1:", matrix[1])
print("Column 2:", matrix[:, 1])
print("Top-right 2x2:\n", matrix[:2, 1:])

# Boolean masking
mask = arr > 20
print("Boolean mask:", mask)
print("Filtered values:", arr[mask])

# Fancy indexing
indices = np.array([0, 2, 4])
print("Fancy indexing:", arr[indices])

# Boolean indexing on 2D arrays
matrix_mask = matrix > 5
print("Values greater than 5:\n", matrix[matrix_mask])

# np.where example
print("np.where result:", np.where(arr > 25, arr, 0))

# Important notes
# - index selection uses square brackets
# - slicing keeps start and excludes stop
# - boolean masks filter values based on a condition
# - fancy indexing selects explicit positions
# - np.where is useful when values need conditional replacement
