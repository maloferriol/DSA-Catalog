#!/usr/bin/env python3
"""Enrich all DSA doc pages with detailed explanations, code examples, and visualizations."""

import json
import re
from pathlib import Path

PROJ = Path(__file__).parent.parent
DATA = PROJ / "data" / "dsa_enriched.json"
DOCS = PROJ / "docs-site" / "docs"

# ─── CONTENT DATABASE ───────────────────────────────────────────────────────
# Each entry: explanation (2-3 paragraphs), code (Python), key_insight, visualization_url

CONTENT = {

# ══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES — LINEAR
# ══════════════════════════════════════════════════════════════════════════════

"Array": {
    "explanation": """An array is the most fundamental data structure: a contiguous block of memory where elements are stored at fixed-size intervals. Because the memory is contiguous and elements are uniformly sized, accessing any element by index is O(1) — the address is simply `base + index × element_size`. This makes arrays the fastest structure for random access.

The trade-off is rigidity. Inserting or deleting in the middle requires shifting all subsequent elements, costing O(n). Arrays also have a fixed size at allocation time (in languages like C/Java). Despite these limitations, arrays underpin nearly every other data structure — hash tables, heaps, and even graphs are often implemented with arrays.

For interviews, arrays are the most common structure you'll encounter. Master the core patterns: **two pointers** (converging from both ends), **sliding window** (fixed or variable-size subarray), and **prefix sum** (precompute cumulative sums for O(1) range queries).""",
    "code": """```python
# Two Pointers: check if sorted array has pair summing to target
def two_sum_sorted(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            return [lo, hi]
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return []

# Prefix Sum: O(1) range sum queries after O(n) preprocessing
def build_prefix(nums):
    prefix = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x
    return prefix  # range_sum(l, r) = prefix[r+1] - prefix[l]
```""",
    "key_insight": "Arrays give O(1) random access because memory addresses are computed arithmetically. This is why array-based structures (heaps, hash tables) are so fast — they reduce to index arithmetic.",
    "visualization": "https://visualgo.net/en/array"
},

"Dynamic Array (ArrayList / Vector)": {
    "explanation": """A dynamic array solves the fixed-size problem of regular arrays by automatically resizing when full. When the internal array runs out of space, a new array (typically 2× the size) is allocated, and all elements are copied over. This gives **amortized O(1)** append — most appends are O(1), but occasionally one triggers an O(n) copy.

The amortized analysis works because the expensive copies are exponentially rare. If you double the size each time, the total cost of n appends is O(n), giving O(1) per operation on average. This is the strategy used by Python's `list`, Java's `ArrayList`, C++'s `vector`, and Go's `slice`.

The key gotcha: if you know the final size in advance, pre-allocate to avoid unnecessary copies. In Python, use list comprehensions instead of repeated `.append()` when possible. Also be aware that deleting from the middle is still O(n) due to shifting.""",
    "code": """```python
# Dynamic array from scratch (simplified)
class DynamicArray:
    def __init__(self):
        self._data = [None] * 2
        self._size = 0
        self._capacity = 2

    def append(self, val):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = val
        self._size += 1

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_cap

    def __getitem__(self, i):
        if i < 0 or i >= self._size:
            raise IndexError
        return self._data[i]
```""",
    "key_insight": "Doubling the capacity on resize gives amortized O(1) append. The total cost of n insertions is O(n) because the copy costs form a geometric series: 1 + 2 + 4 + ... + n = 2n - 1.",
    "visualization": "https://www.cs.usfca.edu/~galles/visualization/ArrayList.html"
},

"String": {
    "explanation": """Strings are sequences of characters — essentially character arrays with special semantics. In most languages (Python, Java, Go), strings are **immutable**: operations like concatenation create a new string rather than modifying the existing one. This means naive string concatenation in a loop is O(n²) — a critical performance trap.

The immutability has benefits: strings can be safely shared, hashed, and used as dictionary keys. For mutable string operations, use `list` of characters in Python (then `''.join()`), `StringBuilder` in Java, or `strings.Builder` in Go.

For interviews, string problems are extremely common. The key patterns are: **sliding window** (longest substring without repeating chars), **two pointers** (palindrome checking), **hashing** (anagram detection with frequency counts), and **trie** (prefix matching). Know your language's string API cold — `split`, `join`, `find`, `replace`, slicing.""",
    "code": """```python
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
```""",
    "key_insight": "String concatenation in a loop is O(n²) because each concatenation copies the entire string. Always use `''.join(parts)` or `StringBuilder` for building strings incrementally.",
    "visualization": "https://pythontutor.com/"
},

"Linked List (Singly)": {
    "explanation": """A singly linked list is a chain of nodes where each node contains a value and a pointer to the next node. Unlike arrays, linked lists don't require contiguous memory, so insertion and deletion at a known position are O(1) — you just redirect pointers. The trade-off: there's no random access. To reach the nth element, you must traverse from the head, taking O(n).

The most important technique is using a **dummy head** (sentinel node). This eliminates edge cases for operations at the head of the list. Without a dummy head, inserting/deleting the first element requires special handling; with it, all positions are treated uniformly.

For interviews, linked list problems are fundamentally about pointer manipulation. The critical patterns are: **fast & slow pointers** (cycle detection, finding the middle), **reversing** (iterative with three pointers: prev, curr, next), and **merge** (combining two sorted lists). Always draw the pointers on paper before coding.""",
    "code": """```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reverse a linked list (iterative)
def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Detect cycle (Floyd's algorithm)
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```""",
    "key_insight": "Always use a dummy head node to avoid special-casing operations on the first element. Return `dummy.next` as the result.",
    "visualization": "https://visualgo.net/en/list"
},

"Doubly Linked List": {
    "explanation": """A doubly linked list extends the singly linked list by adding a `prev` pointer to each node, allowing traversal in both directions. This makes deletion O(1) when you have a reference to the node (no need to find the predecessor), and enables backward traversal.

The main practical use is in implementing **LRU caches** and **deques**. An LRU cache combines a hash map (for O(1) lookup) with a doubly linked list (for O(1) insertion/removal at both ends). When a key is accessed, its node is moved to the front; when the cache is full, the tail node is evicted.

The trade-off vs singly linked lists is memory: each node needs an extra pointer. In practice, doubly linked lists are used more often than singly linked lists because the bidirectional traversal eliminates many edge cases and simplifies algorithms.""",
    "code": """```python
class DLLNode:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = DLLNode(), DLLNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_front(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache: return -1
        node = self.cache[key]
        self._remove(node)
        self._add_front(node)
        return node.val

    def put(self, key, val):
        if key in self.cache:
            self._remove(self.cache[key])
        node = DLLNode(key, val)
        self.cache[key] = node
        self._add_front(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```""",
    "key_insight": "Doubly linked lists with sentinel head/tail nodes make LRU Cache operations (move-to-front, remove-from-tail) clean O(1) with no edge cases.",
    "visualization": "https://visualgo.net/en/list"
},

"Stack": {
    "explanation": """A stack is a Last-In-First-Out (LIFO) collection with two primary operations: `push` (add to top) and `pop` (remove from top), both O(1). Think of a stack of plates — you can only add or remove from the top.

Stacks are used implicitly every time you call a function (the call stack), and explicitly for problems involving **nesting** (matching parentheses), **backtracking** (DFS, undo operations), and **monotonic patterns** (next greater element). The stack is also used to convert recursive algorithms to iterative ones.

The **monotonic stack** is a powerful interview pattern: maintain a stack where elements are always in increasing (or decreasing) order. When pushing a new element, pop all elements that violate the order. This efficiently solves "next greater element," "largest rectangle in histogram," and similar problems in O(n).""",
    "code": """```python
# Valid parentheses
def is_valid(s):
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in match:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack

# Next greater element using monotonic stack
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # indices of elements waiting for their next greater
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(i)
    return result
```""",
    "key_insight": "Whenever you see nesting, matching, or 'nearest greater/smaller' in a problem, think stack. The monotonic stack pattern solves many O(n²) brute-force problems in O(n).",
    "visualization": "https://visualgo.net/en/list"
},

"Queue": {
    "explanation": """A queue is a First-In-First-Out (FIFO) collection with `enqueue` (add to back) and `dequeue` (remove from front), both O(1). Think of a line at a store — first come, first served.

Queues are the backbone of **BFS** (breadth-first search), which explores nodes level by level. They're also used in scheduling (task queues, message queues), buffering (I/O buffers, print spooling), and rate limiting. In Python, use `collections.deque` for an efficient queue — `list` has O(n) `pop(0)`.

A common interview pattern is **BFS with level tracking**: use the queue size at the start of each iteration to process exactly one level. This is used for level-order traversal, shortest path in unweighted graphs, and rotting oranges-style problems.""",
    "code": """```python
from collections import deque

# BFS level-order traversal of a binary tree
def level_order(root):
    if not root: return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):  # process one level
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result

# BFS shortest path in unweighted graph
def shortest_path(graph, start, end):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        if node == end: return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1
```""",
    "key_insight": "BFS = queue. DFS = stack (or recursion). When a problem asks for the shortest path in an unweighted graph or minimum steps, BFS with a queue is almost always the answer.",
    "visualization": "https://visualgo.net/en/list"
},

"Deque (Double-ended queue)": {
    "explanation": """A deque (double-ended queue) supports O(1) insertion and removal at both ends. It combines the capabilities of both stacks and queues. In Python, `collections.deque` is implemented as a doubly-linked list of fixed-size blocks, giving O(1) operations at both ends.

The most important interview application is the **sliding window maximum/minimum** problem. A monotonic deque maintains indices of elements in decreasing order of value. As the window slides, you remove elements from the back that are smaller than the new element (they can never be the max), and remove elements from the front that have fallen outside the window. This gives O(n) for the entire array.

Deques are also used to implement BFS variants like **0-1 BFS** (edges with weight 0 or 1), where 0-weight neighbors go to the front of the deque and 1-weight neighbors go to the back.""",
    "code": """```python
from collections import deque

# Sliding window maximum (monotonic deque)
def max_sliding_window(nums, k):
    dq = deque()  # indices, front = index of current max
    result = []
    for i, num in enumerate(nums):
        # Remove elements outside the window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller elements from the back
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```""",
    "key_insight": "The monotonic deque pattern solves sliding window min/max in O(n). Each element is pushed and popped at most once, so the total work across all iterations is linear.",
    "visualization": "https://visualgo.net/en/list"
},

# ══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES — HASH-BASED
# ══════════════════════════════════════════════════════════════════════════════

"Hash Table / Hash Map": {
    "explanation": """A hash table maps keys to values using a hash function that converts keys into array indices. On average, insertion, deletion, and lookup are all O(1). The hash function computes an index, and if two keys hash to the same index (a collision), the table resolves it — typically via **chaining** (linked list at each bucket) or **open addressing** (probing for the next empty slot).

The load factor (n/capacity) determines performance. When it exceeds a threshold (typically 0.75), the table resizes (usually doubling) and rehashes all entries. This keeps the average chain length short. Python's `dict` uses open addressing with a sophisticated probing scheme; Java's `HashMap` uses chaining with tree-ification for long chains.

For interviews, hash maps are your Swiss Army knife. They convert O(n) lookups into O(1) lookups. The classic pattern: "have I seen this before?" — store elements as you iterate, check existence in O(1). This underlies Two Sum, group anagrams, subarray sum equals K, and dozens more.""",
    "code": """```python
# Two Sum: O(n) using hash map
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Group Anagrams: sort each word as the key
from collections import defaultdict
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return list(groups.values())
```""",
    "key_insight": "When a problem requires checking existence or counting frequencies, a hash map almost always gives you the O(n) solution. The pattern: iterate once, store in map, check in map.",
    "visualization": "https://visualgo.net/en/hashtable"
},

"Hash Set": {
    "explanation": """A hash set is a hash table that stores only keys (no values), supporting O(1) average-time `add`, `remove`, and `contains`. It's the go-to structure when you need to track **unique elements** or check membership efficiently.

Common uses: deduplication, checking if an element exists in a collection, finding intersections/unions of collections, and cycle detection (store visited states). In Python, `set()` is built on the same hash table mechanism as `dict`.

For interviews, sets are often used alongside hash maps. The "seen" set pattern is ubiquitous: maintain a set of visited elements/states as you traverse. This appears in linked list cycle detection, graph traversal (visited set), and duplicate detection.""",
    "code": """```python
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
```""",
    "key_insight": "The trick in longest consecutive sequence: only start counting from numbers that are the START of a sequence (n-1 not in set). This ensures each element is visited at most twice, giving O(n).",
    "visualization": "https://visualgo.net/en/hashtable"
},

"Bloom Filter": {
    "explanation": """A Bloom filter is a space-efficient probabilistic data structure that tests whether an element is a member of a set. It can have **false positives** (says "maybe in set" when it's not) but **never false negatives** (if it says "definitely not in set," it's correct). This trade-off makes it ideal for pre-filtering expensive lookups.

It works using k hash functions and a bit array of m bits. To insert: hash the element k times, set those k bit positions to 1. To query: hash the element k times, check if all k positions are 1. If any is 0, the element is definitely not in the set. If all are 1, it's probably in the set (but other elements might have set those bits).

Real-world uses: databases (check if a key exists before disk lookup), web crawlers (avoid revisiting URLs), CDNs (cache membership), and spell checkers. The false positive rate depends on m/n (bits per element) and k (number of hash functions). With 10 bits per element and 7 hash functions, the false positive rate is about 1%.""",
    "code": """```python
import hashlib

class BloomFilter:
    def __init__(self, size=1000, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bits = [False] * size

    def _hashes(self, item):
        for i in range(self.num_hashes):
            h = hashlib.md5(f\"{item}{i}\".encode()).hexdigest()
            yield int(h, 16) % self.size

    def add(self, item):
        for pos in self._hashes(item):
            self.bits[pos] = True

    def might_contain(self, item):
        return all(self.bits[pos] for pos in self._hashes(item))
```""",
    "key_insight": "Bloom filters trade accuracy for extreme space efficiency. A hash set storing 1M URLs might use 50MB; a Bloom filter with 1% false positive rate uses only 1.2MB.",
    "visualization": "https://www.jasondavies.com/bloomfilter/"
},

# ══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES — TREES
# ══════════════════════════════════════════════════════════════════════════════

"Binary Tree": {
    "explanation": """A binary tree is a hierarchical data structure where each node has at most two children (left and right). It's the foundation for BSTs, heaps, segment trees, and more. Binary trees can be complete (every level filled except possibly the last, filled left to right), full (every node has 0 or 2 children), or perfect (all leaves at the same depth).

Traversal is the most critical operation. There are four main traversals: **inorder** (left-root-right), **preorder** (root-left-right), **postorder** (left-right-root), and **level-order** (BFS). Understanding these recursively and iteratively is essential. Interviewers frequently ask for iterative implementations using an explicit stack.

Most tree problems reduce to a single pattern: solve for left subtree, solve for right subtree, combine at root. This is bottom-up recursion. Master this pattern and you can solve maximum depth, diameter, path sum, subtree validation, and dozens of other problems.""",
    "code": """```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Maximum depth (bottom-up recursion)
def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Inorder traversal (iterative)
def inorder(root):
    result, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result

# Diameter of binary tree
def diameter(root):
    best = 0
    def height(node):
        nonlocal best
        if not node: return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)
    height(root)
    return best
```""",
    "key_insight": "The pattern for most tree problems: (1) base case: null node returns identity value, (2) recurse on left and right, (3) combine results at current node. This bottom-up approach naturally handles the tree structure.",
    "visualization": "https://visualgo.net/en/bst"
},

"Binary Search Tree (BST)": {
    "explanation": """A BST is a binary tree where for every node, all values in the left subtree are strictly less, and all values in the right subtree are strictly greater. This invariant enables O(log n) search, insertion, and deletion on average — but O(n) worst-case when the tree degenerates into a linked list.

The key insight is that an **inorder traversal of a BST produces elements in sorted order**. This property is exploited constantly: validating a BST, finding the kth smallest element, or finding the closest value. Deletion is the trickiest operation — when removing a node with two children, replace it with either its inorder successor (smallest in right subtree) or predecessor (largest in left subtree).

To validate a BST, pass min/max bounds recursively: `isValid(node, min, max)`. Do NOT simply check `left < root < right` at each node — that only checks immediate children and misses violations deeper in the subtree.""",
    "code": """```python
# Validate BST with range bounds
def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    if not root: return True
    if root.val <= lo or root.val >= hi:
        return False
    return (is_valid_bst(root.left, lo, root.val) and
            is_valid_bst(root.right, root.val, hi))

# Kth smallest element (inorder traversal)
def kth_smallest(root, k):
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0: return curr.val
        curr = curr.right

# LCA in BST (exploit BST property)
def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
```""",
    "key_insight": "Inorder traversal of a BST = sorted order. For LCA in a BST, exploit the ordering: if both values are less than root, go left; both greater, go right; otherwise root is the LCA.",
    "visualization": "https://visualgo.net/en/bst"
},

"AVL Tree": {
    "explanation": """An AVL tree is a self-balancing BST where the heights of the left and right subtrees of every node differ by at most 1. After every insertion or deletion, the tree checks balance factors along the path to the root and performs rotations to restore balance. This guarantees O(log n) worst-case for all operations.

There are four rotation cases: **LL** (single right rotation), **RR** (single left rotation), **LR** (left then right rotation), and **RL** (right then left rotation). Identify the case by examining the balance factor of the unbalanced node and its child.

AVL trees are stricter than Red-Black trees (max height ~1.44 log n vs ~2 log n), making lookups slightly faster but insertions/deletions slightly slower due to more frequent rotations. They're preferred when reads dominate writes.""",
    "code": """```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.height = 1

def height(node):
    return node.height if node else 0

def balance_factor(node):
    return height(node.left) - height(node.right) if node else 0

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def insert(node, val):
    if not node: return AVLNode(val)
    if val < node.val:    node.left = insert(node.left, val)
    elif val > node.val:  node.right = insert(node.right, val)
    else: return node
    node.height = 1 + max(height(node.left), height(node.right))
    bf = balance_factor(node)
    if bf > 1 and val < node.left.val:   return rotate_right(node)       # LL
    if bf < -1 and val > node.right.val: return rotate_left(node)        # RR
    if bf > 1 and val > node.left.val:                                   # LR
        node.left = rotate_left(node.left)
        return rotate_right(node)
    if bf < -1 and val < node.right.val:                                 # RL
        node.right = rotate_right(node.right)
        return rotate_left(node)
    return node
```""",
    "key_insight": "After each insert/delete, update heights bottom-up and check balance factors. The rotation case is determined by the signs of the balance factors of the unbalanced node and its child.",
    "visualization": "https://www.cs.usfca.edu/~galles/visualization/AVLtree.html"
},

"Red-Black Tree": {
    "explanation": """A Red-Black tree is a self-balancing BST that uses node coloring (red or black) and five invariants to maintain approximate balance. The rules guarantee the longest path is at most twice the shortest, yielding O(log n) operations.

The five properties: (1) every node is red or black, (2) root is black, (3) null leaves are black, (4) red nodes can't have red children, (5) every path from a node to its leaves has the same number of black nodes (black-height).

Red-Black trees perform fewer rotations than AVL trees on insert/delete, making them better for write-heavy workloads. This is why they're used in Java's `TreeMap`, C++ `std::map`, and Linux's CFS scheduler. Understanding the concept is more important than memorizing every case for interviews.""",
    "code": """```python
# Red-Black tree conceptual overview (not full implementation)
# The mental model: a 2-3-4 tree mapped to a binary tree
# - A black node alone = 2-node
# - A black node with one red child = 3-node
# - A black node with two red children = 4-node

# Key operations:
# Insert: always add as RED, then fix violations
# Fix-up cases:
#   Case 1: Uncle is RED -> recolor parent, uncle to black, grandparent to red
#   Case 2: Uncle is BLACK, node is "inside" child -> rotate to make it Case 3
#   Case 3: Uncle is BLACK, node is "outside" child -> rotate grandparent, recolor

# In practice, use your language's built-in:
# Python: sortedcontainers.SortedDict (not RB but same interface)
# Java: TreeMap, TreeSet
# C++: std::map, std::set
```""",
    "key_insight": "Red-Black trees are 2-3-4 trees in disguise. A red node is 'glued' to its black parent to form a multi-node. This mental model makes the rotations and recoloring intuitive.",
    "visualization": "https://www.cs.usfca.edu/~galles/visualization/RedBlack.html"
},

"B-Tree / B+ Tree": {
    "explanation": """A B-Tree of order m allows each node to have up to m children and m-1 keys. Unlike binary trees, B-Trees are wide and shallow, minimizing disk I/O by keeping the height very low (typically 3-4 levels for millions of keys). Each node is designed to fit within a single disk page.

A B+ Tree is the variant used by virtually every database index (MySQL, PostgreSQL, SQLite). The key difference: all data is stored only in leaf nodes, and leaves are linked together for efficient range scans. Internal nodes contain only routing keys.

For interviews, the important thing is understanding **why** databases use B+ Trees: (1) low height = few disk reads, (2) leaf links = fast range queries, (3) high fanout = better cache utilization.""",
    "code": """```python
# B-Tree conceptual overview
# Not typically implemented in interviews, but understand the operations:

# INSERT:
# 1. Find the correct leaf node
# 2. Insert the key in sorted order
# 3. If the node overflows (> m-1 keys):
#    - Split into two nodes
#    - Push the median key up to the parent
#    - Recursively split the parent if needed
# Tree grows in height ONLY when the root splits

# WHY B+ Trees for databases:
# - Height of 3-4 for billions of rows (each node = 1 disk page = 4-16 KB)
# - Range query: find start leaf, then follow leaf pointers
# - All leaves at same depth = predictable performance
```""",
    "key_insight": "B+ Trees minimize disk I/O by maximizing fanout. A B+ Tree with 4KB pages and 100-byte keys has a fanout of ~40, meaning 3 levels can index 40³ = 64,000 keys with just 3 disk reads.",
    "visualization": "https://www.cs.usfca.edu/~galles/visualization/BPlusTree.html"
},

"Trie (Prefix Tree)": {
    "explanation": """A trie stores strings character by character, with each node representing a single character and paths from root representing stored strings. Lookup, insertion, and deletion are all O(L) where L is the string length, independent of how many strings are stored.

Tries excel at **prefix-based operations**: autocomplete, spell checking, IP routing (longest prefix match), and word games. The TrieNode typically contains a children map/array and an `is_end` flag marking complete words.

For interviews, the most important problems are: **Word Search II** (build trie from word list, DFS on board with trie pruning), **Design Autocomplete** (trie + DFS from prefix node), and **Implement Trie** (insert, search, startsWith).""",
    "code": """```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def _find(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```""",
    "key_insight": "A trie trades space for time: it uses more memory than a hash set of strings but enables prefix queries that hash-based structures cannot do efficiently.",
    "visualization": "https://www.cs.usfca.edu/~galles/visualization/Trie.html"
},

"Heap (Binary Heap)": {
    "explanation": """A binary heap is a complete binary tree stored in an array where every parent satisfies the heap property: in a min-heap, parent ≤ children; in a max-heap, parent ≥ children. The array representation is key: for node at index i, left child = 2i+1, right child = 2i+2, parent = (i-1)//2.

Core operations: `insert` (add at end, bubble up) and `extract-min/max` (swap root with last, remove last, sift down), both O(log n). Building a heap from an array is O(n) using bottom-up heapify — a frequently tested fact.

Heaps are the backbone of priority queues, Dijkstra's algorithm, Huffman coding, and the **top K elements** pattern. In Python, `heapq` provides a min-heap; for a max-heap, negate values.""",
    "code": """```python
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
```""",
    "key_insight": "Building a heap is O(n), not O(n log n). The bottom-up heapify works because most nodes are near the bottom and require very little sifting. For top-K problems, use a min-heap of size K.",
    "visualization": "https://visualgo.net/en/heap"
},

"Priority Queue": {
    "explanation": """A priority queue is an abstract data type supporting `insert` and `extract-min/max`. The most common implementation is a binary heap, but the interface is what matters: elements come out in priority order, not insertion order.

In Python, `heapq` is a min-heap. For max-heap, negate values. For custom objects, use tuples: `(priority, tie_breaker, item)` where the tie_breaker (e.g., insertion counter) prevents comparison errors when priorities are equal.

Priority queues appear in Dijkstra's algorithm, task scheduling, event-driven simulation, and the "K closest/largest" family of problems. The **two-heap** pattern (max-heap for lower half + min-heap for upper half) elegantly solves the median-finding problem.""",
    "code": """```python
import heapq

# Task scheduler with cooldown
def least_interval(tasks, n):
    freq = [0] * 26
    for t in tasks:
        freq[ord(t) - ord('A')] += 1
    max_freq = max(freq)
    max_count = freq.count(max_freq)
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)

# K closest points to origin
def k_closest(points, k):
    return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
```""",
    "key_insight": "In Python, always use heapq with tuples for custom priority: (priority, counter, object). The counter breaks ties and avoids comparing incomparable objects.",
    "visualization": "https://visualgo.net/en/heap"
},

"Segment Tree": {
    "explanation": """A segment tree answers range queries (sum, min, max, GCD) over an array while supporting point or range updates, both in O(log n). Each leaf represents a single element, and each internal node stores the aggregate of its children's ranges.

Building takes O(n). For a range query [L, R], traverse the tree and at each node whose range is completely inside [L, R], take its value directly instead of recursing further. This decomposes the query into O(log n) nodes.

**Lazy propagation** extends segment trees to handle range updates in O(log n). Instead of updating every leaf, store a pending update at internal nodes and push it down only when needed.""",
    "code": """```python
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self._build(nums, 1, 0, self.n - 1)

    def _build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
            return
        mid = (start + end) // 2
        self._build(nums, 2 * node, start, mid)
        self._build(nums, 2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update(self, idx, val, node=1, start=0, end=None):
        if end is None: end = self.n - 1
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid: self.update(idx, val, 2*node, start, mid)
        else:          self.update(idx, val, 2*node+1, mid+1, end)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

    def query(self, l, r, node=1, start=0, end=None):
        if end is None: end = self.n - 1
        if r < start or end < l: return 0
        if l <= start and end <= r: return self.tree[node]
        mid = (start + end) // 2
        return (self.query(l, r, 2*node, start, mid) +
                self.query(l, r, 2*node+1, mid+1, end))
```""",
    "key_insight": "Segment trees decompose any range [L,R] into O(log n) pre-computed segments. Lazy propagation defers range updates by storing pending operations at internal nodes.",
    "visualization": "https://visualgo.net/en/segmenttree"
},

"Fenwick Tree (Binary Indexed Tree)": {
    "explanation": """A Fenwick tree (BIT) supports prefix sum queries and point updates in O(log n) with just a 1D array. It achieves the same as a segment tree for prefix sums but with simpler code, lower memory, and smaller constants.

The magic is bit manipulation: the lowest set bit (`i & -i`) determines which range of elements each position covers. To query prefix sum: accumulate and remove LSB. To update: add delta and add LSB. Use 1-based indexing.

For range sum [L, R], compute `prefix(R) - prefix(L-1)`. Fenwick trees are a competitive programming staple — under 15 lines of code.""",
    "code": """```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)
```""",
    "key_insight": "The operation `i & (-i)` extracts the lowest set bit, which elegantly partitions responsibilities among array positions. Fenwick trees are the simplest way to solve 'range sum with updates'.",
    "visualization": "https://visualgo.net/en/fenwicktree"
},

"Disjoint Set Union (Union-Find)": {
    "explanation": """Union-Find tracks disjoint sets with two operations: `find(x)` returns which set x belongs to, and `union(x, y)` merges two sets. With path compression and union by rank, both operations are nearly O(1) amortized.

Path compression flattens the tree during `find`: `parent[x] = find(parent[x])`. Union by rank attaches the shorter tree under the taller one. Together, these give inverse Ackermann time — effectively constant.

Union-Find is the go-to for dynamic connectivity: detecting cycles in undirected graphs, Kruskal's MST, connected components, and problems like "number of islands" or "accounts merge".""",
    "code": """```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        self.components -= 1
        return True
```""",
    "key_insight": "Path compression (`parent[x] = find(parent[x])`) is the single most important line — it flattens the tree on every find, keeping future operations near O(1).",
    "visualization": "https://visualgo.net/en/ufds"
},

"Suffix Array / Suffix Tree": {
    "explanation": """A suffix array is a sorted array of all suffixes of a string, represented by their starting indices. Combined with an LCP (Longest Common Prefix) array, it can solve virtually any substring problem efficiently.

A suffix tree is the compressed trie of all suffixes, built in O(n) with Ukkonen's algorithm. Suffix arrays use less memory (4-8 bytes vs 20+ bytes per character) and have largely replaced suffix trees in practice.

These are advanced structures used in bioinformatics, text compression (BWT), and competitive programming. For interviews, knowing when to use them matters more than implementation details.""",
    "code": """```python
# Simple suffix array construction (O(n log^2 n))
def build_suffix_array(s):
    n = len(s)
    suffixes = sorted(range(n), key=lambda i: s[i:])
    return suffixes

# Longest repeated substring using suffix array + LCP
def longest_repeated_substring(s):
    sa = build_suffix_array(s)
    best = ""
    for i in range(1, len(sa)):
        # Compare adjacent suffixes in sorted order
        a, b = s[sa[i-1]:], s[sa[i]:]
        lcp = 0
        while lcp < len(a) and lcp < len(b) and a[lcp] == b[lcp]:
            lcp += 1
        if lcp > len(best):
            best = s[sa[i]:sa[i]+lcp]
    return best
```""",
    "key_insight": "The suffix array + LCP array together solve most substring problems. The longest repeated substring is just the maximum value in the LCP array.",
    "visualization": "https://visualgo.net/en/suffixarray"
},

# ══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES — GRAPH & SPECIALIZED
# ══════════════════════════════════════════════════════════════════════════════

"Graph": {
    "explanation": """A graph consists of vertices (nodes) and edges connecting them. Graphs can be directed or undirected, weighted or unweighted, cyclic or acyclic. The two main representations are **adjacency list** (list of neighbors per vertex, space-efficient for sparse graphs) and **adjacency matrix** (2D array, fast edge lookup for dense graphs).

Most graph problems reduce to traversal (BFS/DFS), shortest path (Dijkstra/Bellman-Ford), or connectivity (Union-Find/DFS). The choice of representation matters: adjacency lists use O(V + E) space and are preferred for most problems; adjacency matrices use O(V²) but allow O(1) edge existence checks.

For interviews, always clarify: directed or undirected? weighted? can there be cycles? self-loops? disconnected components? These details determine the algorithm.""",
    "code": """```python
from collections import defaultdict, deque

# Adjacency list representation
graph = defaultdict(list)
edges = [(0,1), (0,2), (1,3), (2,3)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # undirected

# DFS: detect cycle in undirected graph
def has_cycle(graph, n):
    visited = [False] * n
    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node): return True
            elif neighbor != parent:
                return True
        return False
    return any(dfs(i, -1) for i in range(n) if not visited[i])

# Count connected components
def count_components(graph, n):
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            queue = deque([i])
            visited[i] = True
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    return count
```""",
    "key_insight": "For sparse graphs (E << V²), use adjacency lists. For dense graphs or when you need O(1) edge lookup, use an adjacency matrix. Most interview problems use adjacency lists.",
    "visualization": "https://visualgo.net/en/graphds"
},

"Matrix (Grid)": {
    "explanation": """A matrix or grid is a 2D array commonly used to represent maps, game boards, and images. Grid problems are essentially graph problems where each cell is a node connected to its 4 (or 8) neighbors.

The most common pattern is **BFS/DFS on a grid**: iterate through cells, when you find a starting condition (like '1' in Number of Islands), explore all connected cells using BFS or DFS. Use a visited set or modify the grid in-place to mark visited cells.

Direction arrays (`dx = [-1,0,1,0], dy = [0,1,0,-1]`) are the standard way to iterate over 4 neighbors. Always check bounds before accessing a neighbor.""",
    "code": """```python
from collections import deque

# Number of Islands (BFS)
def num_islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                queue = deque([(r, c)])
                grid[r][c] = '0'  # mark visited
                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = cr+dr, cc+dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'
                            queue.append((nr, nc))
    return count

# Shortest path in binary matrix (BFS)
def shortest_path(grid):
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]: return -1
    queue = deque([(0, 0, 1)])
    grid[0][0] = 1
    for r, c, dist in queue:
        if r == n-1 and c == n-1: return dist
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and not grid[nr][nc]:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))
    return -1
```""",
    "key_insight": "Grid problems are graph problems in disguise. The standard template: iterate cells, BFS/DFS from each starting point, mark visited. Direction arrays `[(-1,0),(1,0),(0,-1),(0,1)]` iterate 4-connected neighbors.",
    "visualization": "https://visualgo.net/en/dfsbfs"
},

"Monotonic Stack": {
    "explanation": """A monotonic stack maintains elements in strictly increasing (or decreasing) order. When pushing a new element, pop all elements that violate the monotonic property. This efficiently finds the "next greater element," "next smaller element," or "previous greater/smaller element" for every position in O(n) total.

The key insight: each element is pushed and popped at most once, so the total work across all iterations is O(n), not O(n²). The stack stores indices (not values) so you can compute distances.

Applications: next greater element, largest rectangle in histogram, trapping rain water, stock span, and daily temperatures.""",
    "code": """```python
# Daily temperatures: days until a warmer day
def daily_temperatures(temps):
    n = len(temps)
    result = [0] * n
    stack = []  # indices, decreasing temps
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result

# Largest rectangle in histogram
def largest_rectangle(heights):
    stack = []  # indices, increasing heights
    max_area = 0
    heights.append(0)  # sentinel
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()
    return max_area
```""",
    "key_insight": "Each element is pushed and popped at most once → O(n) total. When you pop an element, you've found its 'answer' (next greater/smaller). The stack stores candidates still waiting for their answer.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Monotonic Queue / Deque": {
    "explanation": """A monotonic queue (implemented as a deque) maintains elements in non-increasing or non-decreasing order, enabling O(1) access to the min or max of a sliding window. Elements are removed from both ends: from the back when a new element makes them obsolete, and from the front when they leave the window.

This solves the sliding window maximum/minimum problem in O(n) total. The classic approach: maintain a deque of indices in decreasing order of values. For each new element, pop from the back all elements smaller than it (they'll never be the max), then append. Pop from the front if it's outside the window.

Also used in DP optimization (convex hull trick, sliding window DP) and 0-1 BFS.""",
    "code": """```python
from collections import deque

# Sliding window maximum
def max_sliding_window(nums, k):
    dq = deque()  # indices, decreasing values
    result = []
    for i, num in enumerate(nums):
        while dq and dq[0] < i - k + 1: dq.popleft()
        while dq and nums[dq[-1]] <= num: dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```""",
    "key_insight": "The monotonic deque gives O(1) sliding window min/max by maintaining a deque where the front is always the current answer. Each element enters and leaves the deque at most once → O(n) total.",
    "visualization": "https://algorithm-visualizer.org/"
},

"LRU Cache": {
    "explanation": """An LRU (Least Recently Used) cache combines a hash map with a doubly linked list to provide O(1) `get` and `put`. The hash map gives O(1) key lookup; the doubly linked list maintains access order with O(1) move-to-front and remove-from-tail.

On `get`: if key exists, move its node to the front (most recently used) and return the value. On `put`: if key exists, update and move to front. If new, add to front. If over capacity, evict the tail (least recently used).

This is one of the most common system design interview questions and also appears as LeetCode 146. The implementation uses sentinel head/tail nodes to avoid edge cases.""",
    "code": """```python
# See Doubly Linked List section for full implementation
# Key insight: HashMap<key, DLLNode> + Doubly Linked List
# - get(key): O(1) lookup + O(1) move to front
# - put(key, val): O(1) insert at front + O(1) evict from tail if full
```""",
    "key_insight": "LRU Cache = HashMap + Doubly Linked List. The hash map gives O(1) access to any node; the linked list maintains the access order with O(1) restructuring.",
    "visualization": "https://www.cs.usfca.edu/~galles/visualization/LRUCache.html"
},

"Skip List": {
    "explanation": """A skip list is a probabilistic data structure that provides O(log n) average-case search, insertion, and deletion — similar to a balanced BST but simpler to implement. It consists of multiple levels of sorted linked lists, where each higher level is a "fast lane" that skips over multiple elements.

Each element is promoted to higher levels with probability 1/2. Searching starts at the top level and moves right until the next element is too large, then drops down a level. On average, the height is O(log n) and each level has half the elements of the level below.

Skip lists are used in Redis (sorted sets), LevelDB, and MemSQL. They're an alternative to balanced BSTs with the advantage of simpler concurrent implementations (lock-free skip lists are easier than lock-free RB trees).""",
    "code": """```python
import random

class SkipNode:
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level=16):
        self.max_level = max_level
        self.head = SkipNode(float('-inf'), max_level)
        self.level = 0

    def _random_level(self):
        lvl = 0
        while random.random() < 0.5 and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, target):
        curr = self.head
        for i in range(self.level, -1, -1):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        curr = curr.next[0]
        return curr and curr.val == target
```""",
    "key_insight": "Skip lists achieve O(log n) by creating 'express lanes' — higher levels skip over more elements. Probabilistic promotion (coin flip) provides balance without rotations.",
    "visualization": "https://www.cs.usfca.edu/~galles/visualization/SkipList.html"
},

"Sparse Table": {
    "explanation": """A sparse table answers static range minimum (or maximum, GCD) queries in O(1) after O(n log n) preprocessing. It precomputes answers for all ranges of power-of-2 lengths. Any range [L, R] can be covered by at most two overlapping power-of-2 ranges.

The table `st[i][j]` stores the minimum of the range starting at index j with length 2^i. Building: `st[0][j] = arr[j]`, then `st[i][j] = min(st[i-1][j], st[i-1][j + 2^(i-1)])`. Querying: find k = floor(log2(R-L+1)), return min(st[k][L], st[k][R-2^k+1]).

Sparse tables work for idempotent operations (min, max, GCD, OR) where overlapping ranges don't cause problems. For sum, use a prefix sum array or Fenwick tree instead.""",
    "code": """```python
import math

class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        k = int(math.log2(n)) + 1
        self.st = [[0] * n for _ in range(k)]
        self.st[0] = arr[:]
        for i in range(1, k):
            for j in range(n - (1 << i) + 1):
                self.st[i][j] = min(self.st[i-1][j],
                                    self.st[i-1][j + (1 << (i-1))])

    def query(self, l, r):
        k = int(math.log2(r - l + 1))
        return min(self.st[k][l], self.st[k][r - (1 << k) + 1])
```""",
    "key_insight": "Any range [L,R] can be covered by two overlapping power-of-2 ranges. For idempotent operations like min/max/GCD, overlapping doesn't matter, giving O(1) queries.",
    "visualization": "https://cp-algorithms.com/data_structures/sparse-table.html"
},

# ══════════════════════════════════════════════════════════════════════════════
# ALGORITHMS — SORTING
# ══════════════════════════════════════════════════════════════════════════════

"Bubble Sort": {
    "explanation": """Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order. The largest unsorted element "bubbles" to its correct position each pass. After n-1 passes, the array is sorted.

Time: O(n²) average and worst case, O(n) best case (already sorted, with early termination). Space: O(1). Stable: yes. It's the simplest sorting algorithm to understand but one of the slowest in practice.

Useful only for educational purposes and tiny arrays. The only practical advantage: it can detect if the array is already sorted in O(n) by checking if any swap occurred during a pass.""",
    "code": """```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # already sorted
    return arr
```""",
    "key_insight": "The early termination optimization (if no swaps in a pass, the array is sorted) makes bubble sort O(n) on already-sorted input. Without it, it always runs O(n²).",
    "visualization": "https://visualgo.net/en/sorting"
},

"Insertion Sort": {
    "explanation": """Insertion sort builds the sorted array one element at a time by inserting each element into its correct position among the already-sorted elements. It shifts larger elements right to make room.

Time: O(n²) worst/average, O(n) best (nearly sorted). Space: O(1). Stable: yes. Insertion sort excels on small arrays (n < 20-50) and nearly-sorted data. This is why `timsort` (Python/Java's built-in sort) uses insertion sort for small runs.

It's also the sort to use when new elements arrive one at a time (online sorting) — each insertion takes O(n) in the worst case but O(1) if the element is already roughly in place.""",
    "code": """```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```""",
    "key_insight": "Insertion sort is the fastest simple sort for nearly-sorted data and small arrays. Python's timsort uses insertion sort for runs shorter than 32-64 elements.",
    "visualization": "https://visualgo.net/en/sorting"
},

"Selection Sort": {
    "explanation": """Selection sort finds the minimum element in the unsorted portion and swaps it with the first unsorted element. It makes exactly n-1 swaps, which is optimal when swaps are expensive (e.g., large records with small keys).

Time: O(n²) always (no best-case optimization). Space: O(1). Stable: no (the swap can change relative order of equal elements). Selection sort is rarely used in practice except when minimizing writes is critical.

The key property: after k iterations, the first k elements are the k smallest in sorted order. This makes selection sort useful as a mental model for understanding partial sorting.""",
    "code": """```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```""",
    "key_insight": "Selection sort makes the minimum number of swaps (n-1). Use it when writing to memory is expensive but comparisons are cheap.",
    "visualization": "https://visualgo.net/en/sorting"
},

"Merge Sort": {
    "explanation": """Merge sort divides the array in half, recursively sorts each half, then merges the two sorted halves. It's a classic divide-and-conquer algorithm with guaranteed O(n log n) time regardless of input.

The merge step is the key operation: use two pointers to walk through both halves, always picking the smaller element. This produces a sorted result in O(n). The recursion depth is O(log n), and each level does O(n) work, giving O(n log n) total.

Merge sort is stable, predictable (no worst-case degradation), and naturally parallelizable. Its main disadvantage is O(n) extra space. It's the algorithm of choice for sorting linked lists (no random access needed) and external sorting (sorting data that doesn't fit in memory).""",
    "code": """```python
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```""",
    "key_insight": "Merge sort is the only comparison-based O(n log n) sort that is stable AND has guaranteed worst-case O(n log n). Use it for linked lists and when stability matters.",
    "visualization": "https://visualgo.net/en/sorting"
},

"Quick Sort": {
    "explanation": """Quick sort picks a pivot, partitions the array so all elements less than the pivot come before it and all greater come after, then recursively sorts the partitions. Average case is O(n log n), but worst case is O(n²) when the pivot is always the smallest or largest element.

The partition step is the key: Lomuto's scheme is simpler (single pointer), Hoare's scheme is faster (fewer swaps). Choosing a good pivot is critical — **median of three** (first, middle, last) or **random pivot** avoids the worst case on nearly-sorted input.

Quick sort is in-place (O(log n) stack space), has excellent cache performance (sequential access), and is faster than merge sort in practice despite the same O(n log n) average. Python's built-in sort uses timsort, but C's `qsort` and many other standard libraries use quicksort variants.""",
    "code": """```python
import random

def quick_sort(arr, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo >= hi: return
    pivot_idx = partition(arr, lo, hi)
    quick_sort(arr, lo, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, hi)

def partition(arr, lo, hi):
    pivot_idx = random.randint(lo, hi)
    arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i
```""",
    "key_insight": "Random pivot selection gives O(n log n) expected time regardless of input. Quick sort's cache-friendliness (sequential memory access) makes it 2-3x faster than merge sort in practice.",
    "visualization": "https://visualgo.net/en/sorting"
},

"Heap Sort": {
    "explanation": """Heap sort builds a max-heap from the array, then repeatedly extracts the maximum to build the sorted array from right to left. It combines the guaranteed O(n log n) of merge sort with the O(1) extra space of insertion sort.

The process: (1) build a max-heap in O(n) using bottom-up heapify, (2) swap the root (maximum) with the last element, reduce heap size by 1, and sift down the new root. Repeat n-1 times.

Heap sort is not stable and has poor cache performance (jumping around the array during sift-down). In practice, it's slower than quicksort but useful as a guaranteed O(n log n) fallback. Introsort (used by C++ `std::sort`) starts with quicksort and switches to heapsort if recursion depth exceeds 2 log n.""",
    "code": """```python
def heap_sort(arr):
    n = len(arr)
    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, i, 0)
    return arr

def sift_down(arr, size, i):
    largest = i
    left, right = 2*i + 1, 2*i + 2
    if left < size and arr[left] > arr[largest]:   largest = left
    if right < size and arr[right] > arr[largest]:  largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        sift_down(arr, size, largest)
```""",
    "key_insight": "Heap sort gives O(n log n) worst-case with O(1) extra space — the only comparison sort that achieves both. The build-heap step is O(n), not O(n log n).",
    "visualization": "https://visualgo.net/en/sorting"
},

"Counting Sort": {
    "explanation": """Counting sort counts the occurrences of each value, then uses those counts to place elements directly into their sorted positions. It runs in O(n + k) time where k is the range of values. It's not a comparison sort — it doesn't compare elements against each other.

The algorithm: (1) count frequencies, (2) compute prefix sums (cumulative counts), (3) place each element at its computed position. This makes it stable when done correctly (iterate input in reverse when placing elements).

Counting sort is ideal when k is small relative to n (e.g., sorting grades 0-100, characters 'a'-'z', or ages 0-150). It's also used as the subroutine in radix sort.""",
    "code": """```python
def counting_sort(arr, max_val=None):
    if not arr: return arr
    if max_val is None: max_val = max(arr)
    count = [0] * (max_val + 1)
    for x in arr:
        count[x] += 1
    result = []
    for val, cnt in enumerate(count):
        result.extend([val] * cnt)
    return result
```""",
    "key_insight": "Counting sort breaks the O(n log n) comparison-sort lower bound by not comparing elements. It trades space (O(k) for counts) for time. Only practical when k is small.",
    "visualization": "https://visualgo.net/en/sorting"
},

"Radix Sort": {
    "explanation": """Radix sort sorts integers digit by digit, from least significant to most significant (LSD) or vice versa (MSD). Each digit is sorted using a stable subroutine like counting sort. For d digits with base b values, time is O(d × (n + b)).

LSD radix sort processes the least significant digit first using a stable sort. After all digits are processed, the array is sorted. This works because each pass preserves the relative order from previous passes (stability is essential).

Radix sort is practical for fixed-length integers, strings, and other data where "digits" can be extracted. For 32-bit integers, 4 passes of 8-bit counting sort gives O(4 × (n + 256)) = O(n). This is faster than O(n log n) comparison sorts for large n.""",
    "code": """```python
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
```""",
    "key_insight": "Radix sort achieves O(n) for fixed-width integers by sorting one digit at a time with a stable sort. The stability of each pass is what makes the overall sort correct.",
    "visualization": "https://visualgo.net/en/sorting"
},

"Bucket Sort": {
    "explanation": """Bucket sort distributes elements into buckets (ranges), sorts each bucket individually, then concatenates the results. Expected time is O(n + k) when elements are uniformly distributed across k buckets.

The algorithm: (1) create k empty buckets, (2) place each element in the bucket corresponding to its value range, (3) sort each bucket (with insertion sort for small buckets), (4) concatenate all buckets in order.

Bucket sort is ideal for uniformly distributed floating-point numbers in [0, 1). For n elements, use n buckets; each bucket gets ~1 element on average, making the per-bucket sort O(1). Real-world use: sorting by score ranges, histogram-based sorting.""",
    "code": """```python
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
```""",
    "key_insight": "Bucket sort achieves O(n) when elements are uniformly distributed. The trick is choosing the right number of buckets and bucket boundaries for the data distribution.",
    "visualization": "https://visualgo.net/en/sorting"
},

"Topological Sort": {
    "explanation": """Topological sort orders vertices of a directed acyclic graph (DAG) such that for every edge u → v, u comes before v. It's used for dependency resolution: build systems (make), task scheduling, course prerequisites, and package managers.

Two approaches: (1) **Kahn's algorithm** (BFS): start with nodes having no incoming edges (indegree 0), process them, reduce indegree of neighbors, add new zero-indegree nodes to the queue. (2) **DFS-based**: run DFS, add nodes to result in reverse post-order (when all descendants are visited, add the node).

If the graph has a cycle, topological sort is impossible. Kahn's algorithm detects cycles naturally: if the result has fewer nodes than the graph, there's a cycle. This makes it useful for cycle detection in directed graphs.""",
    "code": """```python
from collections import deque, defaultdict

# Kahn's algorithm (BFS-based)
def topological_sort(num_nodes, edges):
    graph = defaultdict(list)
    indegree = [0] * num_nodes
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    queue = deque(i for i in range(num_nodes) if indegree[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == num_nodes else []  # empty = cycle
```""",
    "key_insight": "Kahn's algorithm processes nodes in dependency order: start with nodes that have no prerequisites (indegree 0). If the result is shorter than the number of nodes, there's a cycle.",
    "visualization": "https://visualgo.net/en/dfsbfs"
},

# ══════════════════════════════════════════════════════════════════════════════
# ALGORITHMS — SEARCHING
# ══════════════════════════════════════════════════════════════════════════════

"Linear Search": {
    "explanation": """Linear search checks each element sequentially until finding the target or reaching the end. Time: O(n) worst/average, O(1) best. It works on unsorted data and requires no preprocessing.

While simple, linear search is the optimal choice for unsorted data, small arrays, or one-time searches. For repeated searches on the same data, sort first + binary search or use a hash set.

Linear search is also the only option when data arrives as a stream and you can't store everything. The sentinel optimization places the target at the end to avoid checking bounds in the loop.""",
    "code": """```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```""",
    "key_insight": "Linear search is optimal for unsorted data. If you're searching the same data repeatedly, consider sorting it (O(n log n) once) for O(log n) binary searches.",
    "visualization": "https://visualgo.net/en/sorting"
},

"Binary Search": {
    "explanation": """Binary search finds a target in a sorted array by repeatedly halving the search space. Compare the target with the middle element: if equal, found; if less, search the left half; if greater, search the right half. Time: O(log n).

The real power of binary search extends far beyond sorted arrays. It applies to any problem with a **monotonic predicate**: a function that is false for some prefix and true for some suffix (or vice versa). "Binary search on the answer" uses this to find the minimum/maximum value satisfying a condition.

Common bugs: integer overflow in `(lo + hi) / 2` (use `lo + (hi - lo) // 2`), infinite loops from wrong boundary updates, and off-by-one errors. Use the template: `lo, hi = inclusive bounds; while lo < hi; mid = lo + (hi - lo) // 2`.""",
    "code": """```python
# Standard binary search
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:   return mid
        elif arr[mid] < target:  lo = mid + 1
        else:                    hi = mid - 1
    return -1

# Binary search on answer: minimum capacity to ship within D days
def ship_within_days(weights, days):
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        # Can we ship with capacity mid in ≤ days?
        d, curr = 1, 0
        for w in weights:
            if curr + w > mid:
                d += 1
                curr = 0
            curr += w
        if d <= days: hi = mid
        else:         lo = mid + 1
    return lo
```""",
    "key_insight": "Binary search works whenever there's a monotonic predicate. 'Binary search on the answer' is the pattern: guess a value, check if it's feasible, narrow the range. This solves many optimization problems.",
    "visualization": "https://visualgo.net/en/binarysearch"
},

"Ternary Search": {
    "explanation": """Ternary search finds the maximum or minimum of a unimodal function (a function that increases then decreases, or vice versa) by dividing the search space into thirds. At each step, evaluate the function at two points (m1 and m2 at 1/3 and 2/3 of the range) and eliminate one-third of the search space.

Time: O(log₃ n) comparisons, but each step requires 2 function evaluations vs binary search's 1, making it slightly slower per comparison. However, it solves a different class of problems: finding extrema of unimodal functions.

Ternary search is used in competitive programming for optimization on continuous functions (e.g., minimizing distance, maximizing area). For discrete problems, binary search on the derivative (difference) is often simpler.""",
    "code": """```python
# Ternary search for minimum of unimodal function on [lo, hi]
def ternary_search(f, lo, hi, eps=1e-9):
    while hi - lo > eps:
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if f(m1) < f(m2):
            hi = m2
        else:
            lo = m1
    return (lo + hi) / 2
```""",
    "key_insight": "Ternary search finds extrema of unimodal functions where binary search can't. But for many discrete problems, you can convert to binary search by searching on the 'derivative' (adjacent differences).",
    "visualization": "https://cp-algorithms.com/num_methods/ternary_search.html"
},

"Quickselect": {
    "explanation": """Quickselect finds the kth smallest element in an unsorted array in O(n) average time using the partition step from quicksort. After partitioning, the pivot is in its final position. If the pivot is at index k, we're done. If k is less, recurse on the left; if greater, recurse on the right.

Unlike quicksort, quickselect only recurses on ONE side, giving O(n + n/2 + n/4 + ...) = O(n) average time. Worst case is O(n²) with bad pivots, but random pivot selection makes this extremely unlikely.

The median-of-medians algorithm guarantees O(n) worst case but has a large constant factor and is rarely used in practice. Python's `statistics.median` and numpy's `partition` use quickselect variants.""",
    "code": """```python
import random

def quickselect(arr, k):
    \"\"\"Find the kth smallest element (0-indexed).\"\"\"
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        pivot_idx = random.randint(lo, hi)
        arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]
        pivot = arr[hi]
        i = lo
        for j in range(lo, hi):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]
        if i == k:   return arr[i]
        elif i < k:  lo = i + 1
        else:        hi = i - 1
    return arr[lo]
```""",
    "key_insight": "Quickselect is quicksort but only recursing on one side. This halves the work each time: n + n/2 + n/4 + ... = 2n = O(n). Use it for 'kth largest/smallest' without fully sorting.",
    "visualization": "https://visualgo.net/en/sorting"
},

# ══════════════════════════════════════════════════════════════════════════════
# ALGORITHMS — GRAPH TRAVERSAL
# ══════════════════════════════════════════════════════════════════════════════

"Breadth-First Search (BFS)": {
    "explanation": """BFS explores a graph level by level using a queue. Starting from a source node, it visits all neighbors first, then all neighbors' neighbors, and so on. This guarantees the shortest path in unweighted graphs.

The template: initialize a queue with the start node, mark it visited, then repeatedly dequeue, process, and enqueue unvisited neighbors. For level-by-level processing, use the "queue size" trick: at the start of each iteration, note the queue size and process exactly that many nodes.

BFS applications: shortest path in unweighted graphs, level-order tree traversal, minimum steps/moves problems, connected components, and bi-directional search (BFS from both ends to meet in the middle).""",
    "code": """```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# Shortest path (unweighted)
def bfs_shortest(graph, start, end):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        if node == end: return dist
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, dist + 1))
    return -1
```""",
    "key_insight": "BFS guarantees shortest path in unweighted graphs because it explores nodes in order of increasing distance. Always mark nodes as visited WHEN ENQUEUING (not when dequeuing) to avoid duplicates.",
    "visualization": "https://visualgo.net/en/dfsbfs"
},

"Depth-First Search (DFS)": {
    "explanation": """DFS explores as far as possible along each branch before backtracking. It uses a stack (explicit or implicit via recursion). DFS is simpler to implement recursively and naturally handles tree-shaped problems.

DFS applications: cycle detection, topological sort, connected components, path finding, generating permutations/combinations, and solving puzzles (maze, N-queens). DFS on trees is the foundation of most tree algorithms.

Key DFS variants: **preorder** (process before children), **postorder** (process after children), and **inorder** (process between children, BST-specific). For graphs, track node states: WHITE (unvisited), GRAY (in current path), BLACK (fully processed) — GRAY→GRAY edge = cycle in directed graph.""",
    "code": """```python
# DFS iterative
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node in visited: continue
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return order

# DFS recursive: detect cycle in directed graph
def has_cycle_directed(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    def dfs(node):
        color[node] = GRAY
        for nei in graph[node]:
            if color[nei] == GRAY: return True   # back edge = cycle
            if color[nei] == WHITE and dfs(nei): return True
        color[node] = BLACK
        return False
    return any(dfs(i) for i in range(n) if color[i] == WHITE)
```""",
    "key_insight": "DFS uses three colors for cycle detection in directed graphs: WHITE (unvisited), GRAY (in current path), BLACK (done). A GRAY→GRAY edge means you've found a cycle back to the current path.",
    "visualization": "https://visualgo.net/en/dfsbfs"
},

# ══════════════════════════════════════════════════════════════════════════════
# ALGORITHMS — SHORTEST PATH
# ══════════════════════════════════════════════════════════════════════════════

"Dijkstra's Algorithm": {
    "explanation": """Dijkstra's algorithm finds the shortest path from a source to all other vertices in a weighted graph with non-negative edge weights. It uses a priority queue (min-heap) to always process the vertex with the smallest known distance.

The algorithm: (1) set all distances to infinity except source (0), (2) push source into the min-heap, (3) extract the minimum, (4) for each neighbor, if the path through the current node is shorter, update the distance and push to the heap. Continue until the heap is empty.

Time: O((V + E) log V) with a binary heap. Cannot handle negative edge weights — use Bellman-Ford for that. For interviews, always use the lazy deletion approach (allow duplicates in the heap, skip outdated entries).""",
    "code": """```python
import heapq
from collections import defaultdict

def dijkstra(graph, start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue  # skip outdated entry
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dict(dist)
```""",
    "key_insight": "The lazy deletion trick: allow duplicate entries in the heap and skip them when popped (`if d > dist[u]: continue`). This is simpler than decrease-key and works well in practice.",
    "visualization": "https://visualgo.net/en/sssp"
},

"Bellman-Ford": {
    "explanation": """Bellman-Ford finds shortest paths from a single source, even with negative edge weights. It relaxes all edges V-1 times. If any distance can still be reduced after V-1 iterations, there's a negative cycle.

Time: O(V × E). Slower than Dijkstra but handles negative weights. The SPFA (Shortest Path Faster Algorithm) optimization uses a queue to only re-process vertices whose distances changed, but worst case is still O(V × E).

Use Bellman-Ford when: (1) edges can have negative weights, (2) you need to detect negative cycles, (3) the graph is given as an edge list (not adjacency list).""",
    "code": """```python
def bellman_ford(n, edges, src):
    dist = [float('inf')] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # negative cycle
    return dist
```""",
    "key_insight": "After V-1 relaxations, all shortest paths are found (shortest path has at most V-1 edges). A Vth relaxation that still reduces a distance proves a negative cycle exists.",
    "visualization": "https://visualgo.net/en/sssp"
},

"Floyd-Warshall": {
    "explanation": """Floyd-Warshall finds shortest paths between ALL pairs of vertices in O(V³) time and O(V²) space. It uses dynamic programming: for each intermediate vertex k, check if the path i→k→j is shorter than the current path i→j.

The triple nested loop processes intermediate vertices in the outer loop. The DP relation: `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`. This handles negative weights but not negative cycles.

Use Floyd-Warshall when you need all-pairs shortest paths and V is small (up to ~500). For single-source shortest paths, Dijkstra or Bellman-Ford is faster.""",
    "code": """```python
def floyd_warshall(n, edges):
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n): dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
```""",
    "key_insight": "The order of the triple loop matters: k (intermediate vertex) MUST be the outer loop. Think of it as 'adding vertex k as a possible waypoint for all pairs'.",
    "visualization": "https://visualgo.net/en/sssp"
},

"A* Search": {
    "explanation": """A* is an informed search algorithm that finds the shortest path using a heuristic function h(n) that estimates the distance from node n to the goal. It explores nodes in order of f(n) = g(n) + h(n), where g(n) is the actual cost from start to n.

A* is optimal when h(n) is **admissible** (never overestimates) and **consistent** (h(n) ≤ cost(n,m) + h(m)). The most common heuristic for grids is Manhattan distance (4-directional) or Euclidean distance (any-direction). A* reduces to Dijkstra when h(n) = 0, and to greedy best-first search when g(n) = 0.

A* is used in game pathfinding, robotics, GPS navigation, and puzzle solving (15-puzzle, Rubik's cube). It's the standard algorithm for single-pair shortest path on grids.""",
    "code": """```python
import heapq

def a_star(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])  # Manhattan distance

    heap = [(0 + heuristic(start, goal), 0, start)]
    g_cost = {start: 0}
    came_from = {}
    while heap:
        f, g, current = heapq.heappop(heap)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = current[0]+dr, current[1]+dc
            neighbor = (nr, nc)
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and not grid[nr][nc]:
                new_g = g + 1
                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    heapq.heappush(heap, (new_g + heuristic(neighbor, goal), new_g, neighbor))
                    came_from[neighbor] = current
    return []
```""",
    "key_insight": "A* = Dijkstra + heuristic guidance. The heuristic steers the search toward the goal, dramatically reducing explored nodes. Manhattan distance is the standard heuristic for grid pathfinding.",
    "visualization": "https://www.redblobgames.com/pathfinding/a-star/introduction.html"
},

# ══════════════════════════════════════════════════════════════════════════════
# ALGORITHMS — GRAPH (MST, SCC, CYCLE)
# ══════════════════════════════════════════════════════════════════════════════

"Kruskal's MST": {
    "explanation": """Kruskal's algorithm finds the Minimum Spanning Tree by sorting all edges by weight and greedily adding the lightest edge that doesn't create a cycle (using Union-Find to check connectivity).

Time: O(E log E) for sorting + O(E α(V)) for Union-Find operations ≈ O(E log E). Kruskal's is preferred for sparse graphs (small E) and when edges are given as a list.

The MST property: a minimum spanning tree connects all vertices with the minimum total edge weight, using exactly V-1 edges.""",
    "code": """```python
def kruskal(n, edges):
    edges.sort(key=lambda e: e[2])  # sort by weight
    uf = UnionFind(n)  # see Union-Find implementation
    mst = []
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            if len(mst) == n - 1: break
    return mst
```""",
    "key_insight": "Kruskal's = sort edges + Union-Find. The greedy choice (always add cheapest non-cycle edge) is provably optimal for MST.",
    "visualization": "https://visualgo.net/en/mst"
},

"Prim's MST": {
    "explanation": """Prim's algorithm grows the MST from a starting vertex by repeatedly adding the cheapest edge connecting the tree to a non-tree vertex. It uses a min-heap to efficiently find the minimum-weight crossing edge.

Time: O((V + E) log V) with a binary heap. Prim's is preferred for dense graphs (large E) and when the graph is given as an adjacency list. It's conceptually similar to Dijkstra.

Both Kruskal's and Prim's find the same MST (or one of multiple MSTs if edge weights aren't unique). Choose Kruskal's for sparse graphs, Prim's for dense graphs.""",
    "code": """```python
import heapq
from collections import defaultdict

def prim(graph, n):
    visited = [False] * n
    heap = [(0, 0)]  # (weight, node)
    total_weight = 0
    edges_added = 0
    while heap and edges_added < n:
        w, u = heapq.heappop(heap)
        if visited[u]: continue
        visited[u] = True
        total_weight += w
        edges_added += 1
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (weight, v))
    return total_weight
```""",
    "key_insight": "Prim's grows the MST one vertex at a time (like Dijkstra grows shortest path tree). The min-heap always contains the cheapest edge to each non-tree vertex.",
    "visualization": "https://visualgo.net/en/mst"
},

"Tarjan's SCC": {
    "explanation": """Tarjan's algorithm finds all Strongly Connected Components (SCCs) in a directed graph using a single DFS pass. An SCC is a maximal set of vertices where every vertex is reachable from every other.

It tracks discovery time and the lowest reachable discovery time (lowlink) for each node. Nodes on the DFS stack form potential SCCs. When a node's lowlink equals its discovery time, it's the root of an SCC — pop all nodes from the stack up to this root.

Applications: simplifying directed graphs (contract SCCs into single nodes), 2-SAT solver, finding bridges and articulation points (modified version).""",
    "code": """```python
def tarjan_scc(graph, n):
    idx = [0]
    stack, on_stack = [], [False] * n
    index = [-1] * n
    lowlink = [0] * n
    sccs = []

    def strongconnect(v):
        index[v] = lowlink[v] = idx[0]
        idx[0] += 1
        stack.append(v)
        on_stack[v] = True
        for w in graph[v]:
            if index[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], index[w])
        if lowlink[v] == index[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v: break
            sccs.append(scc)

    for v in range(n):
        if index[v] == -1:
            strongconnect(v)
    return sccs
```""",
    "key_insight": "When lowlink[v] == index[v], v is the 'root' of an SCC. Everything on the stack above v (including v) forms the SCC. The single-pass DFS makes this efficient.",
    "visualization": "https://visualgo.net/en/dfsbfs"
},

"Kosaraju's SCC": {
    "explanation": """Kosaraju's algorithm finds SCCs using two DFS passes: (1) DFS on the original graph, recording finish order, (2) DFS on the reversed graph in reverse finish order. Each DFS tree in the second pass is an SCC.

The intuition: the first DFS orders vertices so that SCC roots come after their SCC members. Reversing the graph makes cross-SCC edges point backward. Processing in reverse finish order ensures the second DFS can't escape an SCC.

Kosaraju's is conceptually simpler than Tarjan's but requires two passes and storing the reversed graph. Both run in O(V + E).""",
    "code": """```python
def kosaraju_scc(graph, n):
    # Pass 1: DFS on original graph, record finish order
    visited = [False] * n
    order = []
    def dfs1(v):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]: dfs1(u)
        order.append(v)
    for i in range(n):
        if not visited[i]: dfs1(i)

    # Build reversed graph
    rev = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            rev[v].append(u)

    # Pass 2: DFS on reversed graph in reverse finish order
    visited = [False] * n
    sccs = []
    def dfs2(v, component):
        visited[v] = True
        component.append(v)
        for u in rev[v]:
            if not visited[u]: dfs2(u, component)
    for v in reversed(order):
        if not visited[v]:
            comp = []
            dfs2(v, comp)
            sccs.append(comp)
    return sccs
```""",
    "key_insight": "Two DFS passes: forward to get finish order, backward (on reversed graph) to extract SCCs. The reversed graph ensures DFS in the second pass can't cross SCC boundaries.",
    "visualization": "https://visualgo.net/en/dfsbfs"
},

"Floyd's Cycle Detection (Tortoise & Hare)": {
    "explanation": """Floyd's algorithm detects cycles in a sequence using two pointers: a slow pointer (tortoise, moves 1 step) and a fast pointer (hare, moves 2 steps). If there's a cycle, they'll eventually meet inside the cycle. If the fast pointer reaches null, there's no cycle.

To find the cycle START: after the pointers meet, move one pointer back to the head and advance both at the same speed. They'll meet at the cycle entrance. This works because the distance from the head to the cycle start equals the distance from the meeting point to the cycle start (going around the cycle).

Applications: linked list cycle detection, finding duplicate numbers (LeetCode 287), detecting infinite loops in state machines, and any problem involving repeated function application.""",
    "code": """```python
# Detect cycle and find cycle start
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            # Find cycle start
            slow = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow  # cycle start
    return None  # no cycle

# Find duplicate number (LeetCode 287)
def find_duplicate(nums):
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: break
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
```""",
    "key_insight": "After the tortoise and hare meet, resetting one to the start and advancing both at speed 1 finds the cycle entrance. This is because the distance from start to cycle entry equals the distance from meeting point to cycle entry.",
    "visualization": "https://visualgo.net/en/list"
},

# ══════════════════════════════════════════════════════════════════════════════
# ALGORITHMS — DYNAMIC PROGRAMMING
# ══════════════════════════════════════════════════════════════════════════════

"Knapsack (0/1)": {
    "explanation": """The 0/1 knapsack problem: given items with weights and values, find the maximum value that fits in a knapsack of capacity W. Each item can be taken at most once (0/1 choice).

The DP approach: `dp[i][w]` = max value using items 1..i with capacity w. Transition: either skip item i (`dp[i-1][w]`) or take it (`dp[i-1][w-weight[i]] + value[i]`). Time: O(n × W), Space: O(n × W), optimizable to O(W) using a 1D array (iterate W backwards).

This is the foundational DP problem. Many problems reduce to knapsack variants: subset sum, partition equal subset sum, target sum, and coin change.""",
    "code": """```python
# 0/1 Knapsack (space-optimized to O(W))
def knapsack(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):  # iterate backwards!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]

# Subset Sum: can we pick elements summing to target?
def subset_sum(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for t in range(target, num - 1, -1):
            dp[t] = dp[t] or dp[t - num]
    return dp[target]
```""",
    "key_insight": "The 1D optimization iterates capacity BACKWARDS to ensure each item is used at most once. Iterating forwards would allow reusing items (which is the unbounded knapsack variant).",
    "visualization": "https://algorithm-visualizer.org/"
},

"Unbounded Knapsack": {
    "explanation": """The unbounded knapsack allows each item to be used unlimited times. The only change from 0/1 knapsack: iterate capacity FORWARDS in the 1D DP, allowing items to be counted multiple times.

The classic example is the **coin change** problem: find the minimum number of coins to make a target amount, where each coin denomination can be used unlimited times.

The DP relation: `dp[w] = max(dp[w], dp[w - weight[i]] + value[i])` for each item. By iterating w forwards, `dp[w - weight[i]]` may already include item i, enabling reuse.""",
    "code": """```python
# Coin Change: minimum coins to make amount
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for a in range(coin, amount + 1):  # forwards = unlimited use
            dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Coin Change II: count ways to make amount
def coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]
    return dp[amount]
```""",
    "key_insight": "0/1 knapsack iterates capacity backwards (each item used once). Unbounded knapsack iterates forwards (items reused). This single change in loop direction switches between the two variants.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Longest Common Subsequence (LCS)": {
    "explanation": """LCS finds the longest subsequence present in both strings. A subsequence maintains relative order but doesn't need to be contiguous. It's the foundation for diff tools, version control, and bioinformatics sequence alignment.

DP approach: `dp[i][j]` = length of LCS of first i chars of s1 and first j chars of s2. If `s1[i-1] == s2[j-1]`, extend the LCS: `dp[i][j] = dp[i-1][j-1] + 1`. Otherwise, skip one char from either string: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

Time: O(m × n). To reconstruct the actual LCS, trace back through the DP table from `dp[m][n]`.""",
    "code": """```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# Space-optimized to O(n)
def lcs_optimized(s1, s2):
    m, n = len(s1), len(s2)
    prev = [0] * (n + 1)
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev = curr
    return prev[n]
```""",
    "key_insight": "LCS is the prototype 2D DP problem. The key insight: if characters match, extend the diagonal. If not, take the better of skipping from either string. The edit distance problem follows the same structure.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Longest Increasing Subsequence (LIS)": {
    "explanation": """LIS finds the longest subsequence where each element is strictly greater than the previous. The classic O(n²) DP: `dp[i]` = length of LIS ending at index i. For each i, check all j < i where `nums[j] < nums[i]`.

The O(n log n) approach uses patience sorting: maintain a list `tails` where `tails[i]` is the smallest tail of all increasing subsequences of length i+1. For each new element, binary search for the position to insert/replace. The length of `tails` is the LIS length.

LIS appears in many forms: longest chain of pairs, Russian doll envelopes, maximum number of non-overlapping intervals in order.""",
    "code": """```python
import bisect

# O(n log n) using patience sorting
def lis(nums):
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)

# O(n^2) DP (simpler, allows reconstruction)
def lis_dp(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```""",
    "key_insight": "The O(n log n) solution maintains the smallest possible tail for each LIS length. Binary search finds where each new element fits. The tails array isn't the actual LIS, but its length is correct.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Edit Distance (Levenshtein)": {
    "explanation": """Edit distance measures the minimum number of single-character operations (insert, delete, replace) to transform one string into another. It's fundamental in spell checking, DNA sequence alignment, and fuzzy matching.

DP approach: `dp[i][j]` = edit distance between first i chars of s1 and first j chars of s2. If characters match, `dp[i][j] = dp[i-1][j-1]` (no operation needed). Otherwise, take the minimum of insert (`dp[i][j-1]+1`), delete (`dp[i-1][j]+1`), or replace (`dp[i-1][j-1]+1`).

Time: O(m × n). Space: O(m × n), optimizable to O(n) since each row only depends on the previous row.""",
    "code": """```python
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],      # delete
                                   dp[i][j-1],      # insert
                                   dp[i-1][j-1])    # replace
    return dp[m][n]
```""",
    "key_insight": "Edit distance generalizes LCS to three operations. The base cases encode the cost of converting empty strings. Each cell considers three choices: insert, delete, or replace.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Matrix Chain Multiplication": {
    "explanation": """Matrix chain multiplication finds the optimal parenthesization to minimize the total number of scalar multiplications when multiplying a chain of matrices. The key insight: the result is the same regardless of parenthesization, but the number of operations varies enormously.

DP approach: `dp[i][j]` = minimum cost to multiply matrices i through j. Try every possible split point k: `dp[i][j] = min(dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1])` for all i ≤ k < j.

This is the prototype **interval DP** problem. The same pattern applies to optimal BST construction, burst balloons, minimum cost to merge stones, and palindrome partitioning.""",
    "code": """```python
def matrix_chain(dims):
    n = len(dims) - 1  # number of matrices
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):  # chain length
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n-1]
```""",
    "key_insight": "Interval DP pattern: fill the table by increasing interval length. For each interval [i,j], try every split point k. This pattern recurs in burst balloons, palindrome partitioning, and optimal BST.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Bitmask DP": {
    "explanation": """Bitmask DP uses a bitmask (integer) to represent a subset of elements as the DP state. Each bit position corresponds to an element: 1 = included, 0 = excluded. This allows iterating over all 2^n subsets as integer states.

Common operations: check if element i is in mask (`mask & (1 << i)`), add element i (`mask | (1 << i)`), remove element i (`mask & ~(1 << i)`), count set bits (`bin(mask).count('1')`).

Applications: Traveling Salesman Problem (TSP), assignment problems, Hamiltonian path, and any problem involving choosing subsets with constraints. Time: O(2^n × n) — practical for n ≤ 20.""",
    "code": """```python
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
```""",
    "key_insight": "A bitmask of n bits encodes which elements are 'used'. Iterate over all 2^n masks as DP states. Only practical for n ≤ 20 (2^20 = ~1M states).",
    "visualization": "https://cp-algorithms.com/algebra/all-submasks.html"
},

"Kadane's Algorithm": {
    "explanation": """Kadane's algorithm finds the maximum sum contiguous subarray in O(n) time. The idea: at each position, decide whether to extend the current subarray or start a new one. If the current sum is negative, starting fresh is always better.

DP interpretation: `dp[i]` = maximum sum ending at index i. Transition: `dp[i] = max(nums[i], dp[i-1] + nums[i])`. The answer is `max(dp)`. This can be done in O(1) space by tracking only the current and global maximums.

Variants: maximum product subarray (track both max and min due to negative numbers), maximum circular subarray (max of normal Kadane and total sum minus minimum subarray), and maximum sum with at most k elements.""",
    "code": """```python
def max_subarray(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Maximum product subarray
def max_product(nums):
    max_so_far = min_so_far = result = nums[0]
    for num in nums[1:]:
        candidates = (num, max_so_far * num, min_so_far * num)
        max_so_far, min_so_far = max(candidates), min(candidates)
        result = max(result, max_so_far)
    return result
```""",
    "key_insight": "At each position: extend or restart. If the running sum is negative, any future subarray is better off starting fresh. This greedy choice gives optimal results in one pass.",
    "visualization": "https://algorithm-visualizer.org/"
},

# ══════════════════════════════════════════════════════════════════════════════
# ALGORITHMS — STRING
# ══════════════════════════════════════════════════════════════════════════════

"KMP (Knuth-Morris-Pratt)": {
    "explanation": """KMP finds all occurrences of a pattern in a text in O(n + m) time by preprocessing the pattern into a failure function (partial match table). The failure function `lps[i]` stores the length of the longest proper prefix of pattern[0..i] that is also a suffix.

When a mismatch occurs at position j in the pattern, instead of restarting from the beginning, KMP jumps to `lps[j-1]` — the next position where a match could continue. This avoids re-examining characters in the text.

KMP is the standard string matching algorithm with guaranteed linear time. For practical use, Python's `str.find()` or `in` operator are simpler. KMP matters for interviews and when you need the failure function for other problems.""",
    "code": """```python
def kmp_search(text, pattern):
    def build_lps(p):
        lps = [0] * len(p)
        length = 0
        i = 1
        while i < len(p):
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                i += 1
        return lps

    lps = build_lps(pattern)
    matches = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
        elif j:
            j = lps[j - 1]
        else:
            i += 1
    return matches
```""",
    "key_insight": "The LPS (Longest Prefix Suffix) array lets KMP skip ahead on mismatch instead of restarting. Building the LPS array uses the same logic as the search itself.",
    "visualization": "https://www.cs.usfca.edu/~galles/visualization/KMP.html"
},

"Rabin-Karp": {
    "explanation": """Rabin-Karp uses rolling hash to find pattern matches in O(n + m) expected time. It computes a hash of the pattern and slides a window over the text, updating the hash in O(1) using the rolling hash formula.

The rolling hash: `hash = (hash - text[i] * base^(m-1)) * base + text[i+m]`. When hashes match, verify with actual string comparison to handle collisions. Using a large prime modulus reduces collision probability.

Rabin-Karp's advantage over KMP: it easily extends to multi-pattern matching (compute hashes for all patterns, check against text hash) and 2D pattern matching. Its disadvantage: O(n × m) worst case due to hash collisions.""",
    "code": """```python
def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n: return []
    BASE, MOD = 256, 10**9 + 7
    p_hash = t_hash = 0
    h = pow(BASE, m - 1, MOD)
    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD
    matches = []
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i+m] == pattern:
            matches.append(i)
        if i < n - m:
            t_hash = ((t_hash - ord(text[i]) * h) * BASE + ord(text[i+m])) % MOD
    return matches
```""",
    "key_insight": "Rolling hash updates the window hash in O(1) by removing the leftmost character's contribution and adding the new character. This makes substring comparison O(1) on average.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Z Algorithm": {
    "explanation": """The Z algorithm computes the Z-array: `Z[i]` = length of the longest substring starting at position i that matches a prefix of the string. It runs in O(n) time and is an alternative to KMP for string matching.

For pattern matching, concatenate `pattern + '$' + text` and compute the Z-array. Any position i where `Z[i] == len(pattern)` is a match. The '$' separator prevents the Z-array from crossing the boundary.

The Z algorithm is often simpler to implement than KMP and has the same complexity. It's popular in competitive programming.""",
    "code": """```python
def z_function(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z

def z_search(text, pattern):
    combined = pattern + '$' + text
    z = z_function(combined)
    m = len(pattern)
    return [i - m - 1 for i in range(m + 1, len(combined)) if z[i] == m]
```""",
    "key_insight": "Z[i] tells you how much of the string starting at i matches the prefix. For pattern matching, use pattern$text and find positions where Z[i] equals the pattern length.",
    "visualization": "https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm"
},

"Manacher's Algorithm": {
    "explanation": """Manacher's algorithm finds all palindromic substrings (or the longest one) in O(n) time. It exploits the mirror property of palindromes: if you know palindromes centered at positions left of center c, you can use that information for positions to the right of c.

The trick: insert a special character (like '#') between every character and at both ends. This converts the problem to only consider odd-length palindromes. `P[i]` = radius of the longest palindrome centered at position i in the modified string.

For interviews, knowing that Manacher's exists and runs in O(n) is usually sufficient. The expand-from-center approach (O(n²)) is often acceptable and much simpler to implement.""",
    "code": """```python
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
```""",
    "key_insight": "Manacher's uses the mirror property: palindromes are symmetric, so knowing one side gives you the other. The O(n²) expand-from-center approach is usually sufficient for interviews.",
    "visualization": "https://cp-algorithms.com/string/manacher.html"
},

"Aho-Corasick": {
    "explanation": """Aho-Corasick is a multi-pattern string matching algorithm that finds all occurrences of multiple patterns in a text simultaneously in O(n + m + z) time, where n is text length, m is total pattern length, and z is the number of matches.

It builds a trie from all patterns, then adds failure links (similar to KMP's failure function) that connect nodes to the longest proper suffix that is also a prefix of some pattern. This creates an automaton that processes the text character by character.

Aho-Corasick is used in intrusion detection systems (scanning network traffic for malware signatures), text editors (multi-find), and bioinformatics. It's essentially KMP generalized to multiple patterns.""",
    "code": """```python
from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.goto = [{}]
        self.fail = [0]
        self.output = [[]]

    def add_pattern(self, pattern, idx):
        state = 0
        for ch in pattern:
            if ch not in self.goto[state]:
                self.goto[state][ch] = len(self.goto)
                self.goto.append({})
                self.fail.append(0)
                self.output.append([])
            state = self.goto[state][ch]
        self.output[state].append(idx)

    def build(self):
        queue = deque()
        for ch, s in self.goto[0].items():
            queue.append(s)
        while queue:
            r = queue.popleft()
            for ch, s in self.goto[r].items():
                queue.append(s)
                state = self.fail[r]
                while state and ch not in self.goto[state]:
                    state = self.fail[state]
                self.fail[s] = self.goto[state].get(ch, 0)
                if self.fail[s] == s: self.fail[s] = 0
                self.output[s] = self.output[s] + self.output[self.fail[s]]

    def search(self, text):
        state = 0
        results = []
        for i, ch in enumerate(text):
            while state and ch not in self.goto[state]:
                state = self.fail[state]
            state = self.goto[state].get(ch, 0)
            for pattern_idx in self.output[state]:
                results.append((i, pattern_idx))
        return results
```""",
    "key_insight": "Aho-Corasick = Trie + KMP failure links. It processes the text once and matches all patterns simultaneously, making it much faster than running KMP for each pattern separately.",
    "visualization": "https://algorithm-visualizer.org/"
},

# ══════════════════════════════════════════════════════════════════════════════
# ALGORITHMS — GREEDY, BACKTRACKING, MATH, PATTERN
# ══════════════════════════════════════════════════════════════════════════════

"Interval Scheduling": {
    "explanation": """Interval scheduling selects the maximum number of non-overlapping intervals (or finds the minimum intervals to cover a range). The greedy approach: sort intervals by end time, greedily select the earliest-ending interval that doesn't overlap with the last selected one.

For minimum meeting rooms (interval partitioning), sort by start time and use a min-heap tracking end times. For interval merging, sort by start time and merge overlapping intervals.

The greedy choice (earliest end time) is optimal because it leaves the most room for future intervals. This is one of the classic greedy proofs: exchange argument.""",
    "code": """```python
# Maximum non-overlapping intervals
def max_non_overlapping(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by end time
    count = 0
    end = float('-inf')
    for s, e in intervals:
        if s >= end:
            count += 1
            end = e
    return count

# Merge overlapping intervals
def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return merged

# Minimum meeting rooms (min-heap)
import heapq
def min_rooms(intervals):
    intervals.sort()
    heap = []
    for s, e in intervals:
        if heap and heap[0] <= s:
            heapq.heapreplace(heap, e)
        else:
            heapq.heappush(heap, e)
    return len(heap)
```""",
    "key_insight": "Sort by END time for maximum non-overlapping. Sort by START time for merging and minimum rooms. The greedy choice of earliest end time provably maximizes the number of selected intervals.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Huffman Coding": {
    "explanation": """Huffman coding creates an optimal prefix-free binary code where frequent characters get shorter codes. It uses a greedy algorithm: repeatedly merge the two least-frequent nodes into a new node until one tree remains.

The algorithm: (1) create a leaf for each character with its frequency, (2) build a min-heap, (3) extract the two minimum nodes, create a new internal node with their sum as frequency, (4) insert the new node, (5) repeat until one node remains. Left edges = 0, right edges = 1.

Huffman coding is used in JPEG, MP3, gzip/deflate, and is the foundation of data compression. The prefix-free property (no code is a prefix of another) ensures unique decodability.""",
    "code": """```python
import heapq

def huffman_coding(freq):
    heap = [(f, i, c) for c, f in freq.items() for i in [0]]
    heapq.heapify(heap)
    codes = {c: '' for c in freq}
    if len(heap) == 1:
        codes[heap[0][2]] = '0'
        return codes
    counter = len(freq)
    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        heapq.heappush(heap, (f1 + f2, counter, (left, right)))
        counter += 1
    def assign(node, code):
        if isinstance(node, str):
            codes[node] = code
            return
        left, right = node
        assign(left, code + '0')
        assign(right, code + '1')
    assign(heap[0][2], '')
    return codes
```""",
    "key_insight": "The greedy choice of always merging the two least-frequent nodes produces optimal prefix-free codes. More frequent characters naturally end up with shorter paths (codes) in the tree.",
    "visualization": "https://www.cs.usfca.edu/~galles/visualization/Huffman.html"
},

"N-Queens": {
    "explanation": """The N-Queens problem places N queens on an N×N chessboard so no two queens attack each other (no same row, column, or diagonal). It's the classic backtracking problem.

The approach: place queens one row at a time. For each row, try each column. Check if the position is safe (no conflict with previously placed queens). If safe, place the queen and recurse to the next row. If stuck, backtrack.

Optimize with sets: track occupied columns, diagonals (row-col), and anti-diagonals (row+col). This makes the safety check O(1) instead of scanning all placed queens.""",
    "code": """```python
def solve_n_queens(n):
    results = []
    cols, diags, anti_diags = set(), set(), set()

    def backtrack(row, queens):
        if row == n:
            results.append(queens[:])
            return
        for col in range(n):
            if col in cols or (row-col) in diags or (row+col) in anti_diags:
                continue
            cols.add(col); diags.add(row-col); anti_diags.add(row+col)
            queens.append(col)
            backtrack(row + 1, queens)
            queens.pop()
            cols.remove(col); diags.remove(row-col); anti_diags.remove(row+col)

    backtrack(0, [])
    return results
```""",
    "key_insight": "Use three sets (columns, diagonals, anti-diagonals) for O(1) conflict checking. Diagonals share the same row-col value; anti-diagonals share the same row+col value.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Permutations / Combinations / Subsets": {
    "explanation": """These three problems form the backbone of backtracking. All follow the same template: make a choice, recurse, undo the choice (backtrack).

**Subsets**: for each element, choose to include or exclude it. 2^n subsets total. **Permutations**: for each position, try every unused element. n! permutations total. **Combinations**: like subsets but with a fixed size k. Use a start index to avoid duplicates.

For duplicates in the input, sort first and skip consecutive equal elements at the same decision level. This pruning is essential for problems like "combination sum" with repeated candidates.""",
    "code": """```python
# Subsets
def subsets(nums):
    result = []
    def backtrack(start, curr):
        result.append(curr[:])
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(0, [])
    return result

# Permutations
def permutations(nums):
    result = []
    def backtrack(curr, remaining):
        if not remaining:
            result.append(curr[:])
            return
        for i in range(len(remaining)):
            curr.append(remaining[i])
            backtrack(curr, remaining[:i] + remaining[i+1:])
            curr.pop()
    backtrack([], nums)
    return result

# Combinations (n choose k)
def combinations(n, k):
    result = []
    def backtrack(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, n + 1):
            curr.append(i)
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(1, [])
    return result
```""",
    "key_insight": "The backtracking template: choose → explore → unchoose. Subsets: include/exclude each element. Permutations: try each unused element at each position. Combinations: subsets of fixed size k.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Euclidean Algorithm (GCD)": {
    "explanation": """The Euclidean algorithm finds the Greatest Common Divisor (GCD) of two numbers in O(log(min(a,b))) time. The key insight: `gcd(a, b) = gcd(b, a % b)`, with base case `gcd(a, 0) = a`.

The extended Euclidean algorithm also finds integers x and y such that `ax + by = gcd(a, b)`. This is used in modular inverse computation, RSA cryptography, and solving linear Diophantine equations.

Python's `math.gcd` implements this. For LCM: `lcm(a, b) = a * b // gcd(a, b)`.""",
    "code": """```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# Extended Euclidean: finds x, y such that ax + by = gcd(a, b)
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y
```""",
    "key_insight": "gcd(a, b) = gcd(b, a % b) reduces the problem by at least half each step (the remainder is always less than b), giving O(log n) time. The Fibonacci numbers are the worst case.",
    "visualization": "https://visualgo.net/en/math"
},

"Sieve of Eratosthenes": {
    "explanation": """The Sieve of Eratosthenes finds all prime numbers up to n in O(n log log n) time. It starts by assuming all numbers are prime, then iterates from 2 upward, marking all multiples of each prime as composite.

Optimization: start marking from p² (all smaller multiples are already marked by smaller primes). Only iterate up to √n. This is the fastest general-purpose primality sieve for n up to ~10^8.

For larger ranges or single-number primality testing, use Miller-Rabin. For finding primes in a range [L, R], use a segmented sieve.""",
    "code": """```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
```""",
    "key_insight": "Start marking composites from p² because all smaller multiples of p have a smaller prime factor and are already marked. This optimization cuts the work significantly.",
    "visualization": "https://visualgo.net/en/math"
},

"Fast Exponentiation": {
    "explanation": """Fast exponentiation (binary exponentiation) computes a^n in O(log n) multiplications by repeatedly squaring. The idea: a^n = (a^(n/2))² if n is even, a × a^(n-1) if n is odd.

This is essential for modular exponentiation: `pow(a, n, mod)` computes a^n mod m without overflow. Python's built-in `pow(a, n, mod)` uses this algorithm.

Applications: modular arithmetic in cryptography (RSA), matrix exponentiation for linear recurrences (Fibonacci in O(log n)), and computing large Fibonacci numbers.""",
    "code": """```python
def fast_pow(base, exp, mod=None):
    result = 1
    base = base % mod if mod else base
    while exp > 0:
        if exp & 1:
            result = result * base % mod if mod else result * base
        exp >>= 1
        base = base * base % mod if mod else base * base
    return result

# Matrix exponentiation for Fibonacci
def fib(n):
    if n <= 1: return n
    def mat_mult(A, B):
        return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
                [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
    def mat_pow(M, p):
        result = [[1,0],[0,1]]
        while p:
            if p & 1: result = mat_mult(result, M)
            M = mat_mult(M, M)
            p >>= 1
        return result
    return mat_pow([[1,1],[1,0]], n)[0][1]
```""",
    "key_insight": "Squaring halves the exponent each step: a^16 = (a^8)² = ((a^4)²)² = ... Only O(log n) multiplications needed. Python's built-in pow(a, n, mod) already does this.",
    "visualization": "https://cp-algorithms.com/algebra/binary-exp.html"
},

"Flood Fill": {
    "explanation": """Flood fill colors all connected cells of the same value starting from a given cell. It's a BFS/DFS on a grid, commonly used in paint programs (bucket fill), image processing, and game maps (region detection).

The algorithm: from the starting cell, recursively (or iteratively) visit all 4-connected neighbors that have the same original color and change them to the new color. Mark cells as visited by changing their color.""",
    "code": """```python
def flood_fill(image, sr, sc, new_color):
    original = image[sr][sc]
    if original == new_color: return image
    rows, cols = len(image), len(image[0])
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols: return
        if image[r][c] != original: return
        image[r][c] = new_color
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            dfs(r+dr, c+dc)
    dfs(sr, sc)
    return image
```""",
    "key_insight": "Flood fill is just DFS/BFS on a grid with color-matching as the visited condition. Change the color in-place to mark cells as visited (no extra visited set needed).",
    "visualization": "https://algorithm-visualizer.org/"
},

"Reservoir Sampling": {
    "explanation": """Reservoir sampling selects k random items from a stream of unknown length n, giving each item an equal 1/n probability. The algorithm: keep the first k items, then for each subsequent item i, replace a random item in the reservoir with probability k/i.

This is essential when you can't store all items (streaming data) or don't know the total count in advance. Single-element version (k=1): keep item i with probability 1/i.

Applications: random sampling from databases, streaming analytics, and randomized algorithms.""",
    "code": """```python
import random

def reservoir_sample(stream, k):
    reservoir = []
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir
```""",
    "key_insight": "Each item has probability k/n of being in the final sample, even though n is unknown during processing. The proof uses induction on the stream length.",
    "visualization": "https://en.wikipedia.org/wiki/Reservoir_sampling"
},

"Fisher-Yates Shuffle": {
    "explanation": """Fisher-Yates (Knuth shuffle) produces a uniformly random permutation of an array in O(n) time. For each position i from n-1 down to 1, swap arr[i] with a randomly chosen element from arr[0..i].

This is the correct way to shuffle an array. A common mistake is the naive shuffle (for each position, swap with any random position), which produces a biased distribution — some permutations are more likely than others.

Used in card games, randomized algorithms, A/B testing, and any application requiring unbiased random ordering.""",
    "code": """```python
import random

def shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
```""",
    "key_insight": "Swap with a random element from the REMAINING (unshuffled) portion, not the entire array. This produces exactly n! equally likely permutations. The naive 'swap with any position' produces n^n outcomes, which doesn't divide evenly into n! permutations.",
    "visualization": "https://bost.ocks.org/mike/shuffle/"
},

"Boyer-Moore Majority Vote": {
    "explanation": """Boyer-Moore majority vote finds the element that appears more than n/2 times (the majority element) in O(n) time and O(1) space. It maintains a candidate and a count: when the count drops to 0, pick the current element as the new candidate.

The algorithm works because the majority element has more occurrences than all other elements combined. Every time a non-majority element cancels a majority element, there are still enough majority elements left.

To verify, make a second pass to confirm the candidate actually appears > n/2 times (the algorithm can return a wrong answer if no majority exists).""",
    "code": """```python
def majority_element(nums):
    candidate = count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate  # verify with a second pass if majority not guaranteed
```""",
    "key_insight": "Think of it as a voting war: the majority element has more 'soldiers' than all others combined. Even if every non-majority element cancels one majority element, the majority survives.",
    "visualization": "https://algorithm-visualizer.org/"
},

# ══════════════════════════════════════════════════════════════════════════════
# PARADIGMS
# ══════════════════════════════════════════════════════════════════════════════

"Dynamic Programming": {
    "explanation": """Dynamic Programming (DP) solves problems by breaking them into overlapping subproblems and storing results to avoid recomputation. The two approaches: **top-down** (recursion + memoization) and **bottom-up** (iterative, filling a table).

The key to recognizing DP: (1) **optimal substructure** — the optimal solution contains optimal solutions to subproblems, (2) **overlapping subproblems** — the same subproblems are solved repeatedly. If only (1) holds, use divide-and-conquer; if both hold, use DP.

Common DP patterns: linear (1D array), grid (2D), interval, knapsack, string (LCS/edit distance), tree, bitmask, and digit DP. Start with brute-force recursion, add memoization, then optimize to bottom-up if needed.""",
    "code": """```python
# Top-down (memoization) - Fibonacci
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# Bottom-up (tabulation) - Fibonacci
def fib_bottom_up(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```""",
    "key_insight": "The DP process: (1) define the state (what changes between subproblems), (2) write the recurrence (how states relate), (3) identify base cases, (4) determine computation order (bottom-up) or use memoization (top-down).",
    "visualization": "https://algorithm-visualizer.org/"
},

"Greedy Algorithm": {
    "explanation": """Greedy algorithms make the locally optimal choice at each step, hoping to reach the global optimum. They work when the problem has the **greedy choice property** (a locally optimal choice leads to a globally optimal solution) and **optimal substructure**.

Greedy algorithms are typically faster and simpler than DP. The challenge is proving correctness — the exchange argument is the standard proof technique: show that swapping any non-greedy choice for the greedy one doesn't make things worse.

Common greedy problems: interval scheduling (sort by end time), Huffman coding (merge least frequent), fractional knapsack (best value/weight ratio), and minimum spanning tree (cheapest edge).""",
    "code": """```python
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
```""",
    "key_insight": "Greedy works when you can prove the greedy choice is safe — taking it never prevents you from reaching the optimal solution. If you can't prove it, consider DP instead.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Divide & Conquer": {
    "explanation": """Divide and Conquer breaks a problem into smaller independent subproblems, solves them recursively, then combines the results. Unlike DP, the subproblems don't overlap.

The template: (1) **Divide** the problem into subproblems, (2) **Conquer** by solving subproblems recursively, (3) **Combine** the solutions. The time complexity is analyzed using the Master Theorem.

Classic examples: merge sort (divide array, sort halves, merge), quick sort (partition, sort partitions), binary search (halve search space), closest pair of points, and Strassen's matrix multiplication.""",
    "code": """```python
# Maximum subarray using divide and conquer
def max_subarray_dc(nums, lo=0, hi=None):
    if hi is None: hi = len(nums) - 1
    if lo == hi: return nums[lo]
    mid = (lo + hi) // 2
    left_max = max_subarray_dc(nums, lo, mid)
    right_max = max_subarray_dc(nums, mid + 1, hi)
    # Max crossing subarray
    left_sum = float('-inf')
    s = 0
    for i in range(mid, lo - 1, -1):
        s += nums[i]
        left_sum = max(left_sum, s)
    right_sum = float('-inf')
    s = 0
    for i in range(mid + 1, hi + 1):
        s += nums[i]
        right_sum = max(right_sum, s)
    return max(left_max, right_max, left_sum + right_sum)
```""",
    "key_insight": "The Master Theorem gives the complexity: T(n) = aT(n/b) + O(n^d). Compare log_b(a) with d to determine if divide, combine, or both dominate.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Backtracking": {
    "explanation": """Backtracking systematically explores all possible solutions by making choices, and when a choice leads to a dead end, undoing it (backtracking) and trying the next option. It's DFS on the decision tree.

The template: (1) make a choice, (2) recurse, (3) undo the choice. The key optimization is **pruning**: detect dead ends early and skip entire branches of the search tree.

Backtracking problems: N-Queens, Sudoku solver, permutations/combinations/subsets, word search, palindrome partitioning, and constraint satisfaction problems.""",
    "code": """```python
# Sudoku solver
def solve_sudoku(board):
    def is_valid(r, c, num):
        for i in range(9):
            if board[r][i] == num or board[i][c] == num:
                return False
        br, bc = 3*(r//3), 3*(c//3)
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if board[i][j] == num:
                    return False
        return True

    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for num in '123456789':
                        if is_valid(r, c, num):
                            board[r][c] = num
                            if solve(): return True
                            board[r][c] = '.'  # backtrack
                    return False
        return True

    solve()
```""",
    "key_insight": "Backtracking = DFS + pruning. The power comes from cutting off branches early. The more constraints you can check before recursing, the faster the algorithm runs.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Recursion": {
    "explanation": """Recursion solves a problem by having a function call itself on a smaller instance. Every recursive solution has: (1) a **base case** (stops the recursion), (2) a **recursive case** (breaks the problem down and calls itself).

The mental model: trust that the recursive call solves the smaller problem correctly, and focus on how to combine it with the current step. This "leap of faith" is how to think about recursion — don't try to trace every call.

Common pitfalls: missing base case (infinite recursion), stack overflow (Python default limit: 1000), and doing too much work per call. Tail recursion (where the recursive call is the last operation) can be optimized by some compilers but not Python.""",
    "code": """```python
# Power set using recursion
def power_set(nums, idx=0):
    if idx == len(nums):
        return [[]]
    rest = power_set(nums, idx + 1)
    return rest + [[nums[idx]] + s for s in rest]

# Tower of Hanoi
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)
```""",
    "key_insight": "Think of recursion as delegation: 'I'll handle this one step, and trust the recursive call to handle the rest.' Don't trace all the calls — define the contract and trust it.",
    "visualization": "https://pythontutor.com/"
},

# ══════════════════════════════════════════════════════════════════════════════
# TECHNIQUES
# ══════════════════════════════════════════════════════════════════════════════

"Two Pointers": {
    "explanation": """The two-pointer technique uses two indices that move through the data, typically from opposite ends toward the center (converging) or from the same end at different speeds (sliding window). It reduces O(n²) brute force to O(n).

Common patterns: (1) **Converging pointers** on sorted arrays (Two Sum, Container With Most Water), (2) **Same-direction pointers** for in-place operations (remove duplicates, partition), (3) **Left-right partitioning** (Dutch National Flag / 3-way partition).

Two pointers work when the problem has a monotonic relationship: moving one pointer in a direction always increases or decreases the objective, allowing you to eliminate possibilities.""",
    "code": """```python
# Container With Most Water
def max_area(height):
    lo, hi = 0, len(height) - 1
    best = 0
    while lo < hi:
        best = max(best, min(height[lo], height[hi]) * (hi - lo))
        if height[lo] < height[hi]: lo += 1
        else: hi -= 1
    return best

# Remove duplicates in-place from sorted array
def remove_duplicates(nums):
    if not nums: return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write
```""",
    "key_insight": "Two pointers exploit ordering or partitioning to skip unnecessary comparisons. The key question: 'when I move this pointer, what can I guarantee about the elements I'm skipping?'",
    "visualization": "https://algorithm-visualizer.org/"
},

"Sliding Window": {
    "explanation": """The sliding window technique maintains a window (subarray/substring) that expands or contracts as it moves through the data. It solves problems involving contiguous sequences in O(n) time.

**Fixed-size window**: advance both ends together, maintaining a window of size k. **Variable-size window**: expand the right end to include more, shrink the left end when a constraint is violated. The template: expand right → update state → shrink left while invalid → record answer.

Classic problems: maximum sum subarray of size k, longest substring without repeating characters, minimum window substring, and longest subarray with sum ≤ k.""",
    "code": """```python
# Minimum window substring
from collections import Counter

def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    left = 0
    best = (0, float('inf'))
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:  # window contains all chars of t
            if right - left < best[1] - best[0]:
                best = (left, right)
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[best[0]:best[1]+1] if best[1] != float('inf') else ""
```""",
    "key_insight": "The variable-size sliding window template: expand right to satisfy the condition, then shrink left to find the minimum/optimal window. Each element is added and removed at most once → O(n).",
    "visualization": "https://algorithm-visualizer.org/"
},

"Fast & Slow Pointers": {
    "explanation": """Fast and slow pointers (Floyd's tortoise and hare) use two pointers moving at different speeds to detect cycles, find middle elements, or identify patterns in linked lists and sequences.

**Cycle detection**: slow moves 1 step, fast moves 2 steps. If they meet, there's a cycle. To find the cycle start, reset slow to head and advance both at speed 1. **Finding the middle**: when fast reaches the end, slow is at the middle.

This technique uses O(1) space compared to O(n) for a hash set approach. It works because the fast pointer closes the gap by 1 each step in a cycle.""",
    "code": """```python
# Find middle of linked list
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Linked list cycle detection + cycle start (see Floyd's Cycle Detection)
# Happy number (detect cycle in digit-square sequence)
def is_happy(n):
    def next_num(x):
        return sum(int(d)**2 for d in str(x))
    slow = fast = n
    while True:
        slow = next_num(slow)
        fast = next_num(next_num(fast))
        if fast == 1: return True
        if slow == fast: return False
```""",
    "key_insight": "In a cycle of length C, the fast pointer gains 1 step per iteration on the slow pointer. They meet after at most C iterations. This makes cycle detection O(n) time, O(1) space.",
    "visualization": "https://visualgo.net/en/list"
},

"Prefix Sum": {
    "explanation": """Prefix sum precomputes cumulative sums so that any range sum query [L, R] can be answered in O(1). The prefix array: `prefix[i] = arr[0] + arr[1] + ... + arr[i-1]`. Then `sum(L, R) = prefix[R+1] - prefix[L]`.

This extends to 2D: `prefix[i][j]` = sum of rectangle from (0,0) to (i-1,j-1). A 2D range sum uses inclusion-exclusion on four corners.

Prefix sums are used in subarray sum problems (subarray sum equals K: count pairs where prefix[j] - prefix[i] = K using a hash map), difference arrays, and integral images.""",
    "code": """```python
# Subarray sum equals K
from collections import defaultdict
def subarray_sum(nums, k):
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    curr_sum = 0
    count = 0
    for num in nums:
        curr_sum += num
        count += prefix_count[curr_sum - k]
        prefix_count[curr_sum] += 1
    return count

# 2D prefix sum
def build_2d_prefix(matrix):
    m, n = len(matrix), len(matrix[0])
    p = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            p[i+1][j+1] = matrix[i][j] + p[i][j+1] + p[i+1][j] - p[i][j]
    return p  # sum(r1,c1,r2,c2) = p[r2+1][c2+1]-p[r1][c2+1]-p[r2+1][c1]+p[r1][c1]
```""",
    "key_insight": "Prefix sum converts range sum queries from O(n) to O(1). Combined with a hash map (prefix_count), it solves 'subarray sum equals K' in O(n) by looking up complement prefix sums.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Difference Array": {
    "explanation": """A difference array supports O(1) range updates on an array: adding a value v to all elements in [L, R]. Instead of updating each element, increment `diff[L] += v` and `diff[R+1] -= v`. The original array is recovered by taking the prefix sum of the difference array.

This is the inverse of prefix sums: prefix sum converts point values to range sums, while difference arrays convert range updates to point updates. After all updates, one prefix sum pass gives the final array.

Applications: flight booking (add passengers to a range of stops), meeting room schedules, and any problem with multiple range increment operations.""",
    "code": """```python
# Apply multiple range updates efficiently
def range_updates(n, updates):
    diff = [0] * (n + 1)
    for l, r, val in updates:
        diff[l] += val
        if r + 1 <= n:
            diff[r + 1] -= val
    # Recover actual values via prefix sum
    result = [0] * n
    result[0] = diff[0]
    for i in range(1, n):
        result[i] = result[i-1] + diff[i]
    return result
```""",
    "key_insight": "Difference array is the inverse of prefix sum. Mark +v at the start and -v after the end of a range. One final prefix sum pass reconstructs the array with all updates applied.",
    "visualization": "https://cp-algorithms.com/data_structures/difference_array.html"
},

"Sweep Line": {
    "explanation": """Sweep line processes events sorted by position (usually x-coordinate or time), maintaining active state as the line sweeps from left to right. It converts 2D geometric problems into 1D problems.

The pattern: (1) create events (interval starts and ends), (2) sort events, (3) process events left to right, maintaining a data structure (set, heap, or counter) of active intervals.

Applications: interval intersection, rectangle overlap area, closest pair of points, and calendar booking conflicts.""",
    "code": """```python
# Count maximum overlapping intervals
def max_overlap(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))   # interval starts
        events.append((end, -1))    # interval ends
    events.sort()
    max_count = count = 0
    for _, delta in events:
        count += delta
        max_count = max(max_count, count)
    return max_count
```""",
    "key_insight": "Convert intervals to +1/-1 events at start/end points. Sort by position, sweep through, track the running count. The maximum count is the answer for overlap problems.",
    "visualization": "https://algorithm-visualizer.org/"
},

"Memoization": {
    "explanation": """Memoization caches the results of expensive function calls and returns the cached result when the same inputs occur again. It's the top-down approach to DP: write the recursive solution, then add caching.

In Python, use `@functools.lru_cache` or `@functools.cache` for automatic memoization. For custom caching, use a dictionary keyed by the function arguments.

Memoization is equivalent to bottom-up DP in terms of what it computes, but it only computes states that are actually needed (lazy evaluation). Bottom-up DP computes all states. Memoization is often easier to write but may have higher overhead due to recursion and hash table lookups.""",
    "code": """```python
from functools import lru_cache

# Minimum cost climbing stairs with memoization
@lru_cache(maxsize=None)
def min_cost(costs, i=0):
    if i >= len(costs): return 0
    return costs[i] + min(min_cost(costs, i+1), min_cost(costs, i+2))

# Grid paths with memoization
@lru_cache(maxsize=None)
def unique_paths(m, n):
    if m == 1 or n == 1: return 1
    return unique_paths(m-1, n) + unique_paths(m, n-1)
```""",
    "key_insight": "Memoization = recursion + cache. Write the brute-force recursive solution, then add @lru_cache. If you can write the recursion, you've solved the DP problem. Optimization to bottom-up can come later.",
    "visualization": "https://pythontutor.com/"
},

"Bit Manipulation": {
    "explanation": """Bit manipulation uses bitwise operators (AND, OR, XOR, NOT, shifts) to solve problems efficiently. Key operations: check if bit is set (`n & (1 << i)`), set a bit (`n | (1 << i)`), clear a bit (`n & ~(1 << i)`), toggle (`n ^ (1 << i)`).

Essential tricks: `n & (n-1)` clears the lowest set bit (used to count set bits). `n & -n` isolates the lowest set bit. XOR of a number with itself is 0 — used to find the single non-duplicate element.

Common problems: single number (XOR all elements), counting bits, power of two check (`n & (n-1) == 0`), and subset enumeration with bitmasks.""",
    "code": """```python
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
```""",
    "key_insight": "XOR is the Swiss Army knife of bit manipulation: a^a=0, a^0=a. This property finds the unique element in O(n) time O(1) space. Brian Kernighan's trick (n & (n-1)) counts bits in O(k) where k = number of set bits.",
    "visualization": "https://visualgo.net/en/bitmask"
},

}

# ─── ENRICHMENT LOGIC ────────────────────────────────────────────────────────

def slugify(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def enrich_page(filepath, content_entry):
    text = filepath.read_text()

    sections_to_add = []

    if "explanation" in content_entry:
        sections_to_add.append(f"## How It Works\n\n{content_entry['explanation']}")

    if "code" in content_entry:
        sections_to_add.append(f"## Implementation\n\n{content_entry['code']}")

    if "key_insight" in content_entry:
        sections_to_add.append(f"## Key Insight\n\n> {content_entry['key_insight']}")

    if "visualization" in content_entry:
        sections_to_add.append(f"## Visualization\n\n- [Interactive Visualization]({content_entry['visualization']})")

    enrichment = "\n\n".join(sections_to_add)

    # Insert before "## LeetCode Problems" or "## Resources" (whichever comes first)
    for marker in ["## LeetCode Problems", "## Resources"]:
        if marker in text:
            text = text.replace(marker, enrichment + "\n\n" + marker, 1)
            break
    else:
        text += "\n\n" + enrichment

    filepath.write_text(text)


def main():
    enriched = 0
    skipped = 0

    for dirpath, _, filenames in DOCS.walk() if hasattr(DOCS, 'walk') else [(str(d), [], [f.name for f in d.iterdir() if f.is_file()]) for d in [DOCS] + [p for p in DOCS.rglob('*') if p.is_dir()]]:
        dirpath = Path(dirpath)
        for fname in filenames:
            if not fname.endswith('.md'):
                continue
            filepath = dirpath / fname
            text = filepath.read_text()

            # Extract title from frontmatter
            title_match = re.search(r'^title:\s*"(.+)"', text, re.MULTILINE)
            if not title_match:
                continue
            title = title_match.group(1)

            if title in CONTENT:
                enrich_page(filepath, CONTENT[title])
                enriched += 1
            else:
                skipped += 1

    print(f"Enriched {enriched} pages, {skipped} pages without custom content")


if __name__ == "__main__":
    main()
