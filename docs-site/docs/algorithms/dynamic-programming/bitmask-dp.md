---
title: "Bitmask DP"
sidebar_label: "Bitmask DP"
tags: [algorithm, dynamic-programming]
---

# Bitmask DP

> DP where state encodes a subset as bits in an integer; common for TSP-like problems on small n.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Dynamic Programming |
| **Time** | O(2^n · n) |
| **Space** | O(2^n) |

## Key Techniques

- Subset enumeration via bits

## Notes & Interview Tips

n ≤ ~20.

## How It Works

Bitmask DP uses a bitmask (integer) to represent a subset of elements as the DP state. Each bit position corresponds to an element: 1 = included, 0 = excluded. This allows iterating over all 2^n subsets as integer states.

Common operations: check if element i is in mask (`mask & (1 << i)`), add element i (`mask | (1 << i)`), remove element i (`mask & ~(1 << i)`), count set bits (`bin(mask).count('1')`).

Applications: Traveling Salesman Problem (TSP), assignment problems, Hamiltonian path, and any problem involving choosing subsets with constraints. Time: O(2^n × n) — practical for n ≤ 20.

## Implementation

```python
# Traveling Salesman Problem (TSP)
def tsp(dist):
    n = len(dist)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # start at city 0, only city 0 visited

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == float('inf'): continue
            if not (mask & (1 << u)): continue
            for v in range(n):
                if mask & (1 << v): continue  # already visited
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])

    full_mask = (1 << n) - 1
    return min(dp[full_mask][u] + dist[u][0] for u in range(n))
```

## Key Insight

> A bitmask of n bits encodes which elements are 'used'. Iterate over all 2^n masks as DP states. Only practical for n ≤ 20 (2^20 = ~1M states).

## Visualization

- [Interactive Visualization](https://cp-algorithms.com/algebra/all-submasks.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Subsets](https://leetcode.com/problems/subsets/) | 🟡 Medium | G75, NC150 |
|  | [Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/) | 🟡 Medium | - |
|  | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | 🔴 Hard | - |
|  | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/) | 🟡 Medium | - |
|  | [Add Binary](https://leetcode.com/problems/add-binary/) | 🟢 Easy | G75 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Bitmask)
- [cp-algorithms.com](https://cp-algorithms.com/dynamic_programming/profile-dynamics.html)
