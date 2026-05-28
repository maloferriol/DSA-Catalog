---
title: "Greedy Algorithm"
sidebar_label: "Greedy Algorithm"
tags: [paradigm, greedy]
---

# Greedy Algorithm

> Build a solution by always taking the locally optimal choice; works when the problem has the greedy-choice property.

## Quick Facts

| | |
|---|---|
| **Kind** | Paradigm |
| **Category** | Greedy |
| **Time** | Problem-specific |
| **Space** | Problem-specific |

## Key Techniques

- Exchange argument
- Sort then scan

## Notes & Interview Tips

Sean Prashad: 'If need to count/divide optimally → Greedy, DP.'

## How It Works

Greedy algorithms make the locally optimal choice at each step, hoping to reach the global optimum. They work when the problem has the **greedy choice property** (a locally optimal choice leads to a globally optimal solution) and **optimal substructure**.

Greedy algorithms are typically faster and simpler than DP. The challenge is proving correctness — the exchange argument is the standard proof technique: show that swapping any non-greedy choice for the greedy one doesn't make things worse.

Common greedy problems: interval scheduling (sort by end time), Huffman coding (merge least frequent), fractional knapsack (best value/weight ratio), and minimum spanning tree (cheapest edge).

## Implementation

```python
# Fractional Knapsack
def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)  # sort by value/weight
    total = 0
    for weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total += value
        else:
            total += value * (capacity / weight)
            break
    return total
```

## Key Insight

> Greedy works when you can prove the greedy choice is safe — taking it never prevents you from reaching the optimal solution. If you can't prove it, consider DP instead.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Jump Game](https://leetcode.com/problems/jump-game/) | 🟡 Medium | B75, NC150 |
|  | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | 🟡 Medium | NC150 |
|  | [Partition Labels](https://leetcode.com/problems/partition-labels/) | 🟡 Medium | NC150 |
|  | [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | 🟡 Medium | - |
|  | [Gas Station](https://leetcode.com/problems/gas-station/) | 🟡 Medium | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm)
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/greedy/)
