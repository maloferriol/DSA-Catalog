---
title: "Bit Manipulation"
sidebar_label: "Bit Manipulation"
tags: [technique, math]
---

# Bit Manipulation

> Solve problems using bitwise AND/OR/XOR/shift tricks.

## Quick Facts

| | |
|---|---|
| **Kind** | Technique |
| **Category** | Math |
| **Time** | Usually O(1) per op |
| **Space** | O(1) |

## Key Techniques

- XOR pairing
- n & (n-1) lowest-bit
- Bitmasks
- Brian Kernighan's

## Notes & Interview Tips

Sean Prashad: 'If asked to count bits or use XOR → Bit manipulation.'

## How It Works

Bit manipulation uses bitwise operators (AND, OR, XOR, NOT, shifts) to solve problems efficiently. Key operations: check if bit is set (`n & (1 << i)`), set a bit (`n | (1 << i)`), clear a bit (`n & ~(1 << i)`), toggle (`n ^ (1 << i)`).

Essential tricks: `n & (n-1)` clears the lowest set bit (used to count set bits). `n & -n` isolates the lowest set bit. XOR of a number with itself is 0 — used to find the single non-duplicate element.

Common problems: single number (XOR all elements), counting bits, power of two check (`n & (n-1) == 0`), and subset enumeration with bitmasks.

## Implementation

```python
# Single number (find the non-duplicate)
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Count set bits (Brian Kernighan's)
def count_bits(n):
    count = 0
    while n:
        n &= n - 1  # clear lowest set bit
        count += 1
    return count

# Power of two
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# All subsets of a set
def all_subsets(n):
    return [mask for mask in range(1 << n)]
```

## Key Insight

> XOR is the Swiss Army knife of bit manipulation: a^a=0, a^0=a. This property finds the unique element in O(n) time O(1) space. Brian Kernighan's trick (n & (n-1)) counts bits in O(k) where k = number of set bits.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/bitmask)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Single Number](https://leetcode.com/problems/single-number/) | 🟢 Easy | NC150 |
|  | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | 🟢 Easy | B75, NC150 |
|  | [Counting Bits](https://leetcode.com/problems/counting-bits/) | 🟢 Easy | B75, NC150 |
|  | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | 🟢 Easy | B75, NC150 |
|  | [Single Number III](https://leetcode.com/problems/single-number-iii/) | 🟡 Medium | - |
|  | [Missing Number](https://leetcode.com/problems/missing-number/) | 🟢 Easy | B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Bit_manipulation)
- [leetcode.com](https://leetcode.com/discuss/general-discussion/1073221/all-about-bitwise-operations-beginner-intermediate)
