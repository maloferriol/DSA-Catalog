---
title: "Bucket Sort"
sidebar_label: "Bucket Sort"
tags: [algorithm, sorting]
---

# Bucket Sort

> Distribute elements into buckets, sort each, then concatenate.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Sorting |
| **Time** | Avg O(n+k) |
| **Space** | O(n+k) |

## Key Techniques

- Bucket distribution

## Notes & Interview Tips

Sean Prashad: 'If asked for top/least K → Heap, Quickselect, Bucket sort.' Used in Top-K Frequent.

## How It Works

Bucket sort distributes elements into buckets (ranges), sorts each bucket individually, then concatenates the results. Expected time is O(n + k) when elements are uniformly distributed across k buckets.

The algorithm: (1) create k empty buckets, (2) place each element in the bucket corresponding to its value range, (3) sort each bucket (with insertion sort for small buckets), (4) concatenate all buckets in order.

Bucket sort is ideal for uniformly distributed floating-point numbers in [0, 1). For n elements, use n buckets; each bucket gets ~1 element on average, making the per-bucket sort O(1). Real-world use: sorting by score ranges, histogram-based sorting.

## Implementation

```python
def bucket_sort(arr, num_buckets=10):
    if not arr: return arr
    min_val, max_val = min(arr), max(arr)
    if min_val == max_val: return arr
    bucket_range = (max_val - min_val) / num_buckets
    buckets = [[] for _ in range(num_buckets)]
    for x in arr:
        idx = min(int((x - min_val) / bucket_range), num_buckets - 1)
        buckets[idx].append(x)
    result = []
    for bucket in buckets:
        bucket.sort()  # insertion sort for small buckets
        result.extend(bucket)
    return result
```

## Key Insight

> Bucket sort achieves O(n) when elements are uniformly distributed. The trick is choosing the right number of buckets and bucket boundaries for the data distribution.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/sorting)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | 🟡 Medium | B75, NC150 |
|  | [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | 🟡 Medium | - |
|  | [Maximum Gap](https://leetcode.com/problems/maximum-gap/) | 🟡 Medium | - |
|  | [Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) | 🔴 Hard | - |
|  | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Bucket_sort)
- [en.wikipedia.org](https://en.wikipedia.org/wiki/Bucket_sort)
