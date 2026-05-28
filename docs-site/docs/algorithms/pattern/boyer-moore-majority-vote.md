---
title: "Boyer-Moore Majority Vote"
sidebar_label: "Boyer-Moore Majority Vote"
tags: [algorithm, pattern]
---

# Boyer-Moore Majority Vote

> Find majority element (>n/2) in O(n) time and O(1) space.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Pattern |
| **Time** | O(n) |
| **Space** | O(1) |

## Key Techniques

- Counter cancellation

## Notes & Interview Tips

Generalizes to k candidates for >n/k threshold.

## How It Works

Boyer-Moore majority vote finds the element that appears more than n/2 times (the majority element) in O(n) time and O(1) space. It maintains a candidate and a count: when the count drops to 0, pick the current element as the new candidate.

The algorithm works because the majority element has more occurrences than all other elements combined. Every time a non-majority element cancels a majority element, there are still enough majority elements left.

To verify, make a second pass to confirm the candidate actually appears > n/2 times (the algorithm can return a wrong answer if no majority exists).

## Implementation

```python
def majority_element(nums):
    candidate = count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate  # verify with a second pass if majority not guaranteed
```

## Key Insight

> Think of it as a voting war: the majority element has more 'soldiers' than all others combined. Even if every non-majority element cancels one majority element, the majority survives.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Majority Element](https://leetcode.com/problems/majority-element/) | 🟢 Easy | G75 |
|  | [Majority Element II](https://leetcode.com/problems/majority-element-ii/) | 🟡 Medium | - |
|  | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | G75, B75, NC150 |
|  | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard | NC150 |
|  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
- [leetcode.com](https://leetcode.com/problems/majority-element/)
