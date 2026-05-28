---
title: "Hash Set"
sidebar_label: "Hash Set"
tags: [data-structure, hash-based]
---

# Hash Set

> Unordered set of unique keys backed by a hash function.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Hash-based |
| **Time** | Insert/Lookup/Delete avg O(1) |
| **Space** | O(n) |

## Key Techniques

- Duplicate detection
- Set intersection
- Visited tracking

## Notes & Interview Tips

Default visited-tracker in DFS/BFS.

## How It Works

A hash set is a hash table that stores only keys (no values), supporting O(1) average-time `add`, `remove`, and `contains`. It's the go-to structure when you need to track **unique elements** or check membership efficiently.

Common uses: deduplication, checking if an element exists in a collection, finding intersections/unions of collections, and cycle detection (store visited states). In Python, `set()` is built on the same hash table mechanism as `dict`.

For interviews, sets are often used alongside hash maps. The "seen" set pattern is ubiquitous: maintain a set of visited elements/states as you traverse. This appears in linked list cycle detection, graph traversal (visited set), and duplicate detection.

## Implementation

```python
# Longest consecutive sequence: O(n) using set
def longest_consecutive(nums):
    num_set = set(nums)
    best = 0
    for n in num_set:
        if n - 1 not in num_set:  # start of a sequence
            length = 1
            while n + length in num_set:
                length += 1
            best = max(best, length)
    return best

# Contains duplicate
def contains_duplicate(nums):
    return len(nums) != len(set(nums))
```

## Key Insight

> The trick in longest consecutive sequence: only start counting from numbers that are the START of a sequence (n-1 not in set). This ensures each element is visited at most twice, giving O(n).

## Visualization

- [Interactive Visualization](https://visualgo.net/en/hashtable)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | 🟢 Easy | G75, B75, NC150 |
|  | [Happy Number](https://leetcode.com/problems/happy-number/) | 🟢 Easy | NC150 |
|  | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | 🟡 Medium | B75, NC150 |
|  | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | G75, B75, NC150 |
|  | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟡 Medium | G75, B75, NC150 |
|  | [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | 🟡 Medium | - |
|  | [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Set_(abstract_data_type))
- [geeksforgeeks.org](https://www.geeksforgeeks.org/hash-set-in-java/)
