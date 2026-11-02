"""Sorting and position-finding functions.

Commit message: Add Week 2 NumPy sorting and position notes

Sorting functions return ordered values or the indices needed to obtain that
order. Position functions identify where extreme or nonzero values occur.
"""

import numpy as np


# 1. Sorting values
values = np.array([45, 12, 78, 33, 56, 9])
ascending_values = np.sort(values)
descending_values = np.sort(values)[::-1]

print("original values:", values)
print("ascending values:", ascending_values)
print("descending values:", descending_values)


# 2. Sorting order with argsort()
sorting_order = np.argsort(values)
print("indices that sort values:", sorting_order)
print("values in sorting order:", values[sorting_order])


# 3. Sorting a matrix along each axis
matrix = np.array(
    [
        [9, 2, 7],
        [4, 8, 1],
        [6, 3, 5],
    ]
)

sorted_by_column = np.sort(matrix, axis=0)
sorted_by_row = np.sort(matrix, axis=1)

print("matrix:\n", matrix)
print("sorted down each column:\n", sorted_by_column)
print("sorted across each row:\n", sorted_by_row)


# 4. Finding extreme values and their positions
maximum_value = np.max(values)
minimum_value = np.min(values)
maximum_position = np.argmax(values)
minimum_position = np.argmin(values)

print("maximum value:", maximum_value)
print("maximum position:", maximum_position)
print("minimum value:", minimum_value)
print("minimum position:", minimum_position)


# 5. Axis-aware position functions
row_max_positions = np.argmax(matrix, axis=1)
column_min_positions = np.argmin(matrix, axis=0)

print("maximum position in each row:", row_max_positions)
print("minimum position in each column:", column_min_positions)


# 6. Nonzero positions
signals = np.array(
    [
        [0, 4, 0],
        [2, 0, 7],
        [0, 0, 3],
    ]
)
nonzero_positions = np.nonzero(signals)

print("signals:\n", signals)
print("row positions of nonzero values:", nonzero_positions[0])
print("column positions of nonzero values:", nonzero_positions[1])
print("nonzero values:", signals[nonzero_positions])


# 7. Convert a flattened position back to matrix coordinates
flat_position = np.argmax(matrix)
matrix_position = np.unravel_index(flat_position, matrix.shape)

print("flattened maximum position:", flat_position)
print("matrix maximum position:", matrix_position)


# Important notes
# - np.sort() returns sorted values and leaves the original array unchanged.
# - np.argsort() returns indices, which can reorder related arrays consistently.
# - Without axis, argmax() and argmin() use a flattened view of the array.
# - np.nonzero() returns one coordinate array for each dimension.
