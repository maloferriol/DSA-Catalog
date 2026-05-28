---
title: "Heap (Binary Heap)"
sidebar_label: "Heap (Binary Heap)"
tags: [data-structure, trees]
---

# Heap (Binary Heap)

> Complete binary tree satisfying heap property (min or max at root); array-backed.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Trees |
| **Time** | Insert/Pop O(log n) · Peek O(1) |
| **Space** | O(n) |

## Key Techniques

- Sift up/down
- Heapify
- Top-K
- Heap sort

## Notes & Interview Tips

Sean Prashad: 'If asked for top/least K items → Heap, Quickselect, Bucket sort.'

## How It Works

A binary heap is a complete binary tree stored in an array where every parent satisfies the heap property: in a min-heap, parent ≤ children; in a max-heap, parent ≥ children. The array representation is key: for node at index i, left child = 2i+1, right child = 2i+2, parent = (i-1)//2.

Core operations: `insert` (add at end, bubble up) and `extract-min/max` (swap root with last, remove last, sift down), both O(log n). Building a heap from an array is O(n) using bottom-up heapify — a frequently tested fact.

Heaps are the backbone of priority queues, Dijkstra's algorithm, Huffman coding, and the **top K elements** pattern. In Python, `heapq` provides a min-heap; for a max-heap, negate values.

## Implementation

```python
import heapq

# Kth largest element
def kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)  # min-heap of size k
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]

# Merge K sorted lists
def merge_k_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    result = dummy = ListNode(0)
    while heap:
        val, i, node = heapq.heappop(heap)
        result.next = node
        result = result.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next

# Find median from data stream (two heaps)
class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap (negated)
        self.hi = []  # min-heap

    def add_num(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def find_median(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

## Key Insight

> Building a heap is O(n), not O(n log n). The bottom-up heapify works because most nodes are near the bottom and require very little sifting. For top-K problems, use a min-heap of size K.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/heap)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 Medium | NC150 |
|  | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | 🟡 Medium | B75, NC150 |
|  | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | 🔴 Hard | G75, B75, NC150 |
|  | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | 🔴 Hard | G75, B75, NC150 |
|  | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | 🟢 Easy | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Heap_(data_structure))
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/heap/)
- [visualgo.net](https://visualgo.net/en/heap)
