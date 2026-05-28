---
title: "String"
sidebar_label: "String"
tags: [data-structure, linear]
---

# String

> Immutable (in most languages) sequence of characters; an array of chars under the hood.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Linear |
| **Time** | Access O(1) · Concat O(n) · Substring O(n) |
| **Space** | O(n) |

## Key Techniques

- Two pointers
- Sliding window
- Hashing
- Trie
- KMP
- Rabin-Karp

## Notes & Interview Tips

Use StringBuilder/list-join in Python/Java to avoid O(n^2) concatenation.

## How It Works

Strings are sequences of characters — essentially character arrays with special semantics. In most languages (Python, Java, Go), strings are **immutable**: operations like concatenation create a new string rather than modifying the existing one. This means naive string concatenation in a loop is O(n²) — a critical performance trap.

The immutability has benefits: strings can be safely shared, hashed, and used as dictionary keys. For mutable string operations, use `list` of characters in Python (then `''.join()`), `StringBuilder` in Java, or `strings.Builder` in Go.

For interviews, string problems are extremely common. The key patterns are: **sliding window** (longest substring without repeating chars), **two pointers** (palindrome checking), **hashing** (anagram detection with frequency counts), and **trie** (prefix matching). Know your language's string API cold — `split`, `join`, `find`, `replace`, slicing.

## Implementation

```python
# Sliding window: longest substring without repeating characters
def length_of_longest_substring(s):
    seen = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# Anagram check with frequency counting
from collections import Counter
def is_anagram(s, t):
    return Counter(s) == Counter(t)
```

## Key Insight

> String concatenation in a loop is O(n²) because each concatenation copies the entire string. Always use `''.join(parts)` or `StringBuilder` for building strings incrementally.

## Visualization

- [Interactive Visualization](https://pythontutor.com/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟡 Medium | G75, B75, NC150 |
|  | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟡 Medium | G75, B75, NC150 |
|  | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 🔴 Hard | G75, B75, NC150 |
|  | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | 🟢 Easy | G75, B75, NC150 |
|  | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 🟡 Medium | B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/String_(computer_science))
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/string/)
