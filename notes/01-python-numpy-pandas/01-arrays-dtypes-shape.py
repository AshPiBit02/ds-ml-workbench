"""NumPy arrays, dtypes, and shape basics.

Commit message: Add Week 1 NumPy arrays, dtypes, and shape notes

This file explains the foundations of NumPy arrays and their role in high-speed
numeric work.
"""

import numpy as np

# 1. Creating arrays
arr_1d = np.array([1, 2, 3, 4])
arr_2d = np.array([[1, 2], [3, 4]])
arr_float = np.array([1, 2, 3], dtype=np.float64)

print("1D array:", arr_1d)
print("2D array:\n", arr_2d)
print("dtype:", arr_1d.dtype)
print("float dtype:", arr_float.dtype)

# 2. Shape, ndim, size
print("shape:", arr_2d.shape)
print("ndim:", arr_2d.ndim)
print("size:", arr_2d.size)

# 3. Reshaping
arr = np.arange(12)
print("original:", arr)
print("reshaped 3x4:\n", arr.reshape(3, 4))

# 4. Scalar vs vector operations
print("arr + 5:", arr + 5)
print("arr * 2:", arr * 2)

# 5. Broadcasting overview
row = np.array([[1, 2, 3]])
col = np.array([[1], [2], [3]])
print("row shape:", row.shape)
print("col shape:", col.shape)
print("broadcasted sum:\n", row + col)

# 6. Dtype significance
int_arr = np.array([1, 2, 3], dtype=np.int32)
float_arr = int_arr.astype(np.float32)
print("int array:", int_arr.dtype)
print("float array:", float_arr.dtype)

# Important notes
# - shape stores the size of each dimension
# - ndim indicates the number of dimensions
# - dtype defines the stored data type
# - NumPy arrays support fast vectorized calculations
# - shape compatibility is essential before arithmetic between arrays
