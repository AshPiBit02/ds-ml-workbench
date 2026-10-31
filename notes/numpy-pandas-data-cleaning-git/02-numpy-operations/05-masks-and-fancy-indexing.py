"""Boolean masks and fancy indexing.

Commit message: Add Week 2 NumPy masks and fancy indexing notes

Boolean masks select values that satisfy conditions. Fancy indexing selects
explicit positions through arrays of integer indices.
"""

import numpy as np


# 1. Boolean masks on a one-dimensional array
scores = np.array([42, 18, 75, 63, 29, 90])
passing_mask = scores >= 50

print("scores:", scores)
print("passing mask:", passing_mask)
print("passing scores:", scores[passing_mask])


# 2. Combining conditions
in_target_range = (scores >= 30) & (scores <= 80)
outside_target_range = (scores < 30) | (scores > 80)

print("scores from 30 through 80:", scores[in_target_range])
print("scores outside the target range:", scores[outside_target_range])


# 3. Boolean masks on rows
records = np.array(
    [
        [101, 24, 72],
        [102, 31, 88],
        [103, 19, 61],
        [104, 27, 45],
    ]
)

# Columns represent record ID, age, and score.
high_score_rows = records[:, 2] >= 70
adult_rows = records[:, 1] >= 21

print("records with high scores:\n", records[high_score_rows])
print("adult records with high scores:\n", records[adult_rows & high_score_rows])


# 4. Fancy indexing with explicit integer positions
positions = np.array([0, 2, 4])
selected_scores = scores[positions]

print("selected positions:", positions)
print("selected scores:", selected_scores)


# 5. Selecting explicit rows and columns
selected_rows = records[[0, 3]]
selected_columns = records[:, [0, 2]]
selected_cells = records[[0, 1, 3], [2, 2, 1]]

print("selected rows:\n", selected_rows)
print("selected columns:\n", selected_columns)
print("selected cells:", selected_cells)


# 6. Boolean masks and fancy indexing can be combined
high_score_positions = np.nonzero(high_score_rows)[0]
print("positions of high-score records:", high_score_positions)
print("high-score record IDs:", records[high_score_positions, 0])


# Important notes
# - A mask has the same selection length as the dimension being filtered.
# - Parentheses are required around individual conditions.
# - Fancy indexing accepts integer arrays or lists of positions.
# - Multiple index arrays select paired coordinates rather than a submatrix.
