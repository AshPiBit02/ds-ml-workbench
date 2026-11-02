# NumPy Week 2 Notes

## Purpose

This folder covers the second week of the study roadmap: boolean masks,
fancy indexing, conditional replacement, sorting, position functions,
clipping, axis-based operations, and views versus copies.

## Learning goals

- Filter one-dimensional and multidimensional arrays with boolean masks.
- Select specific elements, rows, and columns with fancy indexing.
- Replace values conditionally with `np.where()` and `np.select()`.
- Sort values and obtain sorting order with `np.sort()` and `np.argsort()`.
- Locate minimum and maximum positions with `argmin()`, `argmax()`, and
  `nonzero()`.
- Limit values to a valid range with `np.clip()`.
- Distinguish array views from independent copies.
- Apply operations along the correct axis and verify output shapes.

## Recommended order

1. `05-masks-and-fancy-indexing.py`
2. `06-where-clip-and-replacement.py`
3. `07-sorting-and-position-functions.py`
4. `08-views-copies-and-axis-operations.py`

## Weekly objective

A strong understanding of NumPy selection and transformation operations is
required before handling tabular data with Pandas. Each operation should be
interpreted through its input shape, output shape, selected positions, and
effect on the original array.

## Core reminders

- Use `&` and `|` for combined NumPy conditions, with parentheses around each
  condition.
- `np.argsort()` returns indices, while `np.sort()` returns sorted values.
- A slice often produces a view, while fancy indexing produces a copy.
- `axis=0` operates down rows and produces column-wise results; `axis=1`
  operates across columns and produces row-wise results.
- `np.clip()` limits values without removing elements.

## Commit message

Add Week 2 NumPy operations overview and roadmap notes
