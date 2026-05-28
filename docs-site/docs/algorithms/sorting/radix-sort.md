---
title: "Radix Sort"
sidebar_label: "Radix Sort"
tags: [algorithm, sorting]
---

# Radix Sort

> Non-comparison sort: process digits/bits from least to most significant using stable counting sort.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Sorting |
| **Time** | O(d·(n+b)) |
| **Space** | O(n+b) |

## Key Techniques

- Digit-by-digit
- Stable

## Notes & Interview Tips

Good for fixed-width integers and strings.

## How It Works

Radix sort sorts integers digit by digit, from least significant to most significant (LSD) or vice versa (MSD). Each digit is sorted using a stable subroutine like counting sort. For d digits with base b values, time is O(d × (n + b)).

LSD radix sort processes the least significant digit first using a stable sort. After all digits are processed, the array is sorted. This works because each pass preserves the relative order from previous passes (stability is essential).

Radix sort is practical for fixed-length integers, strings, and other data where "digits" can be extracted. For 32-bit integers, 4 passes of 8-bit counting sort gives O(4 × (n + 256)) = O(n). This is faster than O(n log n) comparison sorts for large n.

## Implementation

```python
def radix_sort(arr):
    if not arr: return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for x in arr:
        count[(x // exp) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for x in reversed(arr):  # reverse for stability
        digit = (x // exp) % 10
        output[count[digit] - 1] = x
        count[digit] -= 1
    arr[:] = output
```

## Key Insight

> Radix sort achieves O(n) for fixed-width integers by sorting one digit at a time with a stable sort. The stability of each pass is what makes the overall sort correct.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/sorting)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Maximum Gap](https://leetcode.com/problems/maximum-gap/) | 🟡 Medium | - |
|  | [Sort an Array](https://leetcode.com/problems/sort-an-array/) | 🟡 Medium | - |
|  | [Query Kth Smallest Trimmed Number](https://leetcode.com/problems/query-kth-smallest-trimmed-number/) | 🟡 Medium | - |
|  | [3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium | G75, B75, NC150 |
|  | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Radix_sort)
- [en.wikipedia.org](https://en.wikipedia.org/wiki/Radix_sort)
