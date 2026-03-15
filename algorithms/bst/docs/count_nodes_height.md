# Count Nodes and Height in Binary Search Tree

## Overview

This algorithm provides fundamental operations for Binary Search Trees (BSTs): counting nodes and calculating tree height. These operations are essential for understanding BST size and structure, and are used in various tree-related algorithms and analyses.

## Algorithm Steps

### Node Counting (count Nodes)

The node counting follows a simple recursive divide-and-conquer approach:

1. **Base Case**: If the root is `None`, return 0 (empty tree has no nodes)
2. **Recursive Case**: Return 1 + count(root.left) + count(root.right)
3. This visits each node exactly once
4. Total count includes all nodes in both subtrees plus the root itself

Mathematical recurrence: `count(root) = 1 + count(root.left) + count(root.right)`

### Height Calculation

Tree height represents the number of edges on the longest path from root to leaf:

1. **Base Case**: If the root is `None`, return -1 (empty tree has height -1)
2. **Recursive Case**: Return 1 + max(height(root.left), height(root.right))
3. Calculates the maximum depth from root to any leaf node

Mathematical recurrence: `height(root) = 1 + max(height(root.left), height(root.right))`

### Iterative Variants

**Iterative Node Count ( Morris Traversal**
- Avoids recursion stack by using threaded binary tree concepts
- Temporarily modifies tree structure during traversal
- Returns to original structure after counting
- O(1) space complexity

**Iterative Height: BFS
- Uses queue-based breadth-first traversal
- Tracks level by level
- Time: O(n), Space: O(w) where w is max width