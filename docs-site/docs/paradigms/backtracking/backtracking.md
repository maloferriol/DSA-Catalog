---
title: "Backtracking"
sidebar_label: "Backtracking"
tags: [paradigm, backtracking]
---

# Backtracking

> Build a solution incrementally and undo choices that lead to dead ends.

## Quick Facts

| | |
|---|---|
| **Kind** | Paradigm |
| **Category** | Backtracking |
| **Time** | Often O(b^d) where b=branches, d=depth |
| **Space** | O(d) |

## Key Techniques

- DFS with undo
- Pruning

## Notes & Interview Tips

Sean Prashad: 'If asked for all permutations/subsets → Backtracking.'

## How It Works

Backtracking systematically explores all possible solutions by making choices, and when a choice leads to a dead end, undoing it (backtracking) and trying the next option. It's DFS on the decision tree.

The template: (1) make a choice, (2) recurse, (3) undo the choice. The key optimization is **pruning**: detect dead ends early and skip entire branches of the search tree.

Backtracking problems: N-Queens, Sudoku solver, permutations/combinations/subsets, word search, palindrome partitioning, and constraint satisfaction problems.

## Implementation

```python
# Sudoku solver
def solve_sudoku(board):
    def is_valid(r, c, num):
        for i in range(9):
            if board[r][i] == num or board[i][c] == num:
                return False
        br, bc = 3*(r//3), 3*(c//3)
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if board[i][j] == num:
                    return False
        return True

    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for num in '123456789':
                        if is_valid(r, c, num):
                            board[r][c] = num
                            if solve(): return True
                            board[r][c] = '.'  # backtrack
                    return False
        return True

    solve()
```

## Key Insight

> Backtracking = DFS + pruning. The power comes from cutting off branches early. The more constraints you can check before recursing, the faster the algorithm runs.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Permutations](https://leetcode.com/problems/permutations/) | 🟡 Medium | G75, NC150 |
|  | [Subsets](https://leetcode.com/problems/subsets/) | 🟡 Medium | G75, NC150 |
|  | [Combination Sum](https://leetcode.com/problems/combination-sum/) | 🟡 Medium | G75, B75, NC150 |
|  | [N-Queens](https://leetcode.com/problems/n-queens/) | 🔴 Hard | NC150 |
|  | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | 🟡 Medium | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Backtracking)
- [leetcode.com](https://leetcode.com/discuss/general-discussion/680706/backtracking-cheat-sheet)
