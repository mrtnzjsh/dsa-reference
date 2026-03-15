# Left View, Right View, and Right-Left View of Binary Search Tree

## Overview

This module provides algorithms to view different perspectives of a binary tree:
- **Left View**: Nodes visible when viewing tree from left side
- **Right View**: Nodes visible when viewing tree from right side
- **Right-Left View**: Nodes visible when viewing tree from right side first, then left side (bottom-right to top-left)

These views are useful for various applications including:
- Tree visualization
- Algorithmic problems (like binary tree serialization)
- Understanding tree structure from different perspectives
- Finding nodes with certain properties

## Input

```python
@dataclass
class TreeNode:
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None
```

## Output

Returns a list of node values in the specified view (from top to bottom for left/right views, mixed order for right-left view).

## Algorithm Steps

### Left View
1. Use BFS (level-order) traversal
2. For each level, add the first node to the result
3. Process all nodes at current level before moving to next

**Mathematical definition**: For each level d, select the first visited node in left-to-right order.

### Right View
1. Use BFS (level-order) traversal
2. For each level, keep track of the last node processed
3. Add the last node to the result
4. Process all nodes at current level

**Mathematical definition**: For each level d, select the last visited node in left-to-right order.

### Right-Left View
1. Traverse right side first (reverse order from right view)
2. Then traverse left side
3. Combine results

**Mathematical definition**: View from right side first, then left side (bottom-right to top-left).

### DFS Variants
- **Left view using DFS**: Use pre-order traversal, first node of each level is always the leftmost node

## Example

```python
# Example Tree:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

tree = TreeNode(1,
               TreeNode(2, TreeNode(4), TreeNode(5)),
               TreeNode(3, None, TreeNode(6)))

# Left View:      Right View:    Right-Left View:
#       1            1              1
#      / \          / \            / \
#     2   3        2   6          6   2
#    / \          /            / \
#   4   5        6            5   4
#  (first nodes on each level)
```

**Step-by-step for Right-Left View:**
1. Right View of tree: [1, 2, 6]
2. Left View of tree: [1, 2, 4]
3. Combine: Right view first, then left view (excluding duplicates)
4. Result: [6, 3, 1, 2, 4, 5] (order may vary)

## Complexity Analysis

### Time Complexity
- **Left View**: O(n) - visits each node once
- **Right View**: O(n) - visits each node once
- **Right-Left View**: O(n) - two passes through the tree
- **DFS Variants**: O(n) - visits each node once

### Space Complexity
- **Time Complexity**: O(n) for all views - must visit every node
- **Space Complexity**: O(n) for storing views, O(h) for BFS/DFS recursion
- **Where**: n = number of nodes, h = height of tree

For balanced BST: h = O(log n)
For skewed tree: h = O(n)

## Notes

**Key Properties:**
- Left View always contains the leftmost node at each level
- Right View always contains the rightmost node at each level
- Different trees can have identical left views but different right views

**Trade-offs:**
- Left/Right View: Simple BFS approach
- Right-Left View: Requires two passes or specialized tracking
- For full tree reconstruction, more information is needed than these views

**Applications:**
- Tree visualization and analysis
- Algorithmic problems involving tree reconstruction
- Finding minimum/maximum values at different depths
- Understanding tree structure from different angles
- Testing binary tree implementations
