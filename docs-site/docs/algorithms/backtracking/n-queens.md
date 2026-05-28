---
title: "N-Queens"
sidebar_label: "N-Queens"
tags: [algorithm, backtracking]
---

# N-Queens

> Place N non-attacking queens on an N×N board via backtracking with column/diagonal pruning.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Backtracking |
| **Time** | O(N!) |
| **Space** | O(N) |

## Key Techniques

- Backtracking
- Bit masks for diagonals

## Notes & Interview Tips

Canonical backtracking exercise.

## How It Works

The N-Queens problem places N queens on an N×N chessboard so no two queens attack each other (no same row, column, or diagonal). It's the classic backtracking problem.

The approach: place queens one row at a time. For each row, try each column. Check if the position is safe (no conflict with previously placed queens). If safe, place the queen and recurse to the next row. If stuck, backtrack.

Optimize with sets: track occupied columns, diagonals (row-col), and anti-diagonals (row+col). This makes the safety check O(1) instead of scanning all placed queens.

## Implementation

```python
def solve_n_queens(n):
    results = []
    cols, diags, anti_diags = set(), set(), set()

    def backtrack(row, queens):
        if row == n:
            results.append(queens[:])
            return
        for col in range(n):
            if col in cols or (row-col) in diags or (row+col) in anti_diags:
                continue
            cols.add(col); diags.add(row-col); anti_diags.add(row+col)
            queens.append(col)
            backtrack(row + 1, queens)
            queens.pop()
            cols.remove(col); diags.remove(row-col); anti_diags.remove(row+col)

    backtrack(0, [])
    return results
```

## Key Insight

> Use three sets (columns, diagonals, anti-diagonals) for O(1) conflict checking. Diagonals share the same row-col value; anti-diagonals share the same row+col value.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [N-Queens](https://leetcode.com/problems/n-queens/) | 🔴 Hard | NC150 |
|  | [N-Queens II](https://leetcode.com/problems/n-queens-ii/) | 🔴 Hard | - |
|  | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | 🟡 Medium | G75, NC150 |
|  | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | 🟡 Medium | NC150 |
|  | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | 🔴 Hard | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
- [leetcode.com](https://leetcode.com/problems/n-queens/)
