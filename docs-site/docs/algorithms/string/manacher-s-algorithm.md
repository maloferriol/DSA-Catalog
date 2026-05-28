---
title: "Manacher's Algorithm"
sidebar_label: "Manacher's Algorithm"
tags: [algorithm, string]
---

# Manacher's Algorithm

> Find all palindromic substrings in linear time.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | String |
| **Time** | O(n) |
| **Space** | O(n) |

## Key Techniques

- Center expansion with reuse

## Notes & Interview Tips

Longest palindromic substring in O(n).

## How It Works

Manacher's algorithm finds all palindromic substrings (or the longest one) in O(n) time. It exploits the mirror property of palindromes: if you know palindromes centered at positions left of center c, you can use that information for positions to the right of c.

The trick: insert a special character (like '#') between every character and at both ends. This converts the problem to only consider odd-length palindromes. `P[i]` = radius of the longest palindrome centered at position i in the modified string.

For interviews, knowing that Manacher's exists and runs in O(n) is usually sufficient. The expand-from-center approach (O(n²)) is often acceptable and much simpler to implement.

## Implementation

```python
def longest_palindrome(s):
    # O(n^2) expand from center (simpler, usually sufficient)
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
    best = ""
    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i + 1)
        best = max(best, odd, even, key=len)
    return best

# Manacher's O(n) (for reference)
def manacher(s):
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    c = r = 0
    for i in range(n):
        if i < r:
            p[i] = min(r - i, p[2*c - i])
        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i+p[i]+1] == t[i-p[i]-1]:
            p[i] += 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    return max(p)  # length of longest palindrome = max(p)
```

## Key Insight

> Manacher's uses the mirror property: palindromes are symmetric, so knowing one side gives you the other. The O(n²) expand-from-center approach is usually sufficient for interviews.

## Visualization

- [Interactive Visualization](https://cp-algorithms.com/string/manacher.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟡 Medium | G75, B75, NC150 |
|  | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟡 Medium | G75, B75, NC150 |
|  | [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/) | 🟡 Medium | - |
|  | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | 🟡 Medium | G75 |
|  | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🔴 Hard | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Longest_palindromic_substring)
- [cp-algorithms.com](https://cp-algorithms.com/string/manacher.html)
