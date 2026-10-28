"""NumPy vectorization and broadcasting.

Commit message: Add Week 1 NumPy vectorization and broadcasting notes

Vectorization means applying operations to whole arrays instead of manual loops.
Broadcasting allows compatible shapes to work together without explicit reuse.
"""

import numpy as np

# Vectorized operations
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])
print("Element-wise addition:", x + y)
print("Element-wise multiplication:", x * y)
print("Square root:", np.sqrt(x))

# Compare with explicit loop logic
values = np.array([2, 4, 6, 8])
print("Vectorized square:", values ** 2)

# Broadcasting examples
A = np.array([[1, 2, 3]])
B = np.array([[10], [20], [30]])
print("A shape:", A.shape)
print("B shape:", B.shape)
print("Broadcasted sum:\n", A + B)

# Row vector + scalar
print("Row + scalar:", np.array([[1, 2, 3]]) + 5)

# 2D array + 1D array
C = np.array([[1, 2, 3], [4, 5, 6]])
print("C + [10, 20, 30]:\n", C + np.array([10, 20, 30]))

# incompatible shapes
try:
    np.array([[1, 2, 3]]) + np.array([1, 2])
except ValueError as e:
    print("Broadcasting error:", e)

# Important notes
# - vectorized operations are faster than Python loops for array math
# - broadcasting aligns dimensions from the right
# - compatibility requires matching dimensions or a dimension of size 1
# - incompatible shapes trigger a ValueError
