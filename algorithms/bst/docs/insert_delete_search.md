# Binary Search Tree (BST) Insert, Delete, and Search

## Overview

This module provides comprehensive implementations of Binary Search Tree operations including insertion, deletion, and searching. BST is a fundamental data structure that enables efficient data retrieval and management with average-case time complexity of O(log n) for these operations.

A Binary Search Tree is a node-based binary tree data structure which has the following properties:
- The left subtree of a node contains only nodes with keys lesser than the node's key
- The right subtree of a node contains only nodes with keys greater than the node's key
- Both the left and right subtrees must also be binary search trees

## Mathematical Foundations

The BST property can be formally expressed as:
For any node x:
- left_child.key < x.key < right_child.key (if both children exist)
- For any path from root to leaf, keys are monotonically increasing

If we consider the height h of a BST with n nodes:
- Worst case: h = n (skewed tree, resembling a linked list)
- Best case: h = ⌊log₂(n)⌋ (balanced tree)
- Average case: h ≈ O(log n)

The mathematical relationship between nodes and height depends on tree balance:
- Complete binary tree: minimum height for given number of nodes
- Skewed tree: maximum height, no balance achieved

## Algorithm Steps

### Search Operation
Algorithm: Compare target value with current node's value and recursively search:
1. Start at root node
2. If target equals current node: return True (found)
3. If target less than current: traverse left subtree
4. If target greater than current: traverse right subtree
5. If leaf node reached: return False (not found)

Mathematical complexity:
- Best case: O(log n) if balanced, O(1) if target at root
- Average case: O(log n) if balanced
- Worst case: O(n) if tree is completely unbalanced (skewed)

### Insertion Operation
Algorithm: Find appropriate position for new value:
1. If tree empty: create new root node
2. Start at root node
3. If target less than current: traverse left
4. If target greater than current: traverse right
5. If empty position found: create new node
6. If duplicate: return False (no insertion)

Mathematical complexity:
- Best case: O(log n) if balanced
- Average case: O(log n)
- Worst case: O(n) for skewed trees

### Deletion Operation
Algorithm: Three cases for deletion:

Case 1: Leaf node (no children)
- Simply remove the node, its parent's appropriate child pointer becomes None

Case 2: Node with one child
- Replace node with its single child, effectively bypassing the node

Case 3: Node with two children
- Find inorder successor (smallest in right subtree) or predecessor
- Copy successor's value to the node
- Delete the successor from right subtree
- This maintains BST property

Mathematical complexity:
- Best case: O(log n) if balanced
- Average case: O(log n)
- Worst case: O(n) for deletion of root in skewed tree

### Inorder Traversal
Algorithm: Visit nodes in ascending order:
1. Traverse left subtree
2. Visit current node
3. Traverse right subtree

Time Complexity: O(n) - visits each node exactly once

### Preorder Traversal
Algorithm: Visit nodes in root-left-right order:
1. Visit current node
2. Traverse left subtree
3. Traverse right subtree

Time Complexity: O(n) - visits each node exactly once

### Postorder Traversal
Algorithm: Visit nodes in left-right-root order:
1. Traverse left subtree
2. Traverse right subtree
3. Visit current node

Time Complexity: O(n) - visits each node exactly once

### Find Minimum
Algorithm: Find leftmost node (following left pointers):
1. Start at root
2. While left child exists, move to left child
3. Return value at current node

Time Complexity: Best: O(1), Average: O(log n), Worst: O(n)

### Find Maximum
Algorithm: Find rightmost node (following right pointers):
1. Start at root
2. While right child exists, move to right child
3. Return value at current node

Time Complexity: Best: O(1), Average: O(log n), Worst: O(n)

### Find Lowest Common Ancestor (LCA)
Algorithm:
1. Start at root
2. If both values are less than current: go left
3. If both values are greater than current: go right
4. Otherwise: current node is the LCA

Time Complexity: Best: O(1), Average: O(log n), Worst: O(n)

### Get Height
Algorithm: Find maximum depth of any node from the root:
1. Base case: empty tree has height -1
2. For case: height = max(left_height, right_height) + 1

Time Complexity: O(n)

### Get Depth
Algorithm: Find number of edges from root to node:
1. Start at root
2. Count steps as traversing
3. Return depth if found, None otherwise

Time Complexity: Best: O(log n), Average: O(log n), Worst: O(n)

### Range Query
Algorithm: Find all values in specified range:
1. Use BST property to traverse only relevant nodes
2. Collect values within min and max bounds

Time Complexity: Best: O(k + log n), Average: O(k + log n), Worst: O(n)

## Input

- `value`: Value to search for in the tree
- `target`: The integer value to search for in the array

## Output

Returns the index of the target if found, otherwise returns -1
Returns True if value exists in tree, False otherwise

## Example

```python
>>> bst = BinarySearchTree()
>>> bst.insert(10)
True
>>> bst.insert(5)
True
>>> bst.insert(15)
True
>>> bst.search(5)
True
>>> bst.search(7)
False
>>> bst.delete(10)
True
>>> bst.search(10)
False
>>> bst.inorder_traversal()
[5, 15]
```

### Step-by-step example for insert_delete_search with values [10, 5, 15, 7]:

**After inserting 10:**
```
       10
```

**After inserting 5:**
```
       10
      /
     5
```

**After inserting 15:**
```
       10
      /  \
     5    15
```

**After inserting 7:**
```
       10
      /  \
     5    15
      \
       7
```

**Search for value 7:**
```
Start at root 10: 7 < 10 → go left
Go to node 5: 7 > 5 → go right
Go to node 7: 7 == 7 → found!
```

**Delete leaf node 5:**
```
Original:
       10
      /  \
     5    15
      \
       7

After deletion of 5:
       10
        \
         7
       /
     15
```

**Delete node with one child (7):**
```
Original:
       10
        \
         7
       /
     15

After deletion of 7:
       10
        \
         15
```

**Delete node with two children (15):**
Find inorder successor: 17
Copy value, then delete successor
```
       10
        \
         7
        /
       17
```

## Complexity Analysis

### Time Complexity

Let n be the number of nodes in the tree, h be the height:

**Search:**
- Best: O(1) (target at root)
- Average: O(log n) for balanced tree
- Worst: O(n) for completely skewed tree

**Insertion:**
- Best: O(log n) for balanced tree
- Average: O(log n)
- Worst: O(n) for completely skewed tree

**Deletion:**
- Best: O(log n) for balanced tree
- Average: O(log n)
- Worst: O(n) for completely skewed tree

**Traversals (inorder, preorder, postorder):**
- Best: O(n) for balanced tree
- Average: O(n)
- Worst: O(n) for any tree

**Find Min/Max:**
- Best: O(1) (tree with only root)
- Average: O(log n) for balanced tree
- Worst: O(n) for completely skewed tree

**Find LCA:**
- Best: O(1) (values at root)
- Average: O(log n) for balanced tree
- Worst: O(n) for completely skewed tree

**Get Height:**
- Best: O(log n) for balanced tree
- Average: O(log n)
- Worst: O(n) for completely skewed tree

**Get Depth:**
- Best: O(1) (target at root)
- Average: O(log n) for balanced tree
- Worst: O(n) for completely skewed tree

**Range Query:**
- Best: O(k + log n) where k is number of matching values
- Average: O(k + log n)
- Worst: O(n) if range includes all values

### Space Complexity

- O(n) total space for n nodes
- O(h) recursion stack space
- O(1) iterative approach uses minimal space
- O(k) for result list in range query

## Notes

Trade-offs Between Approaches:

1. Iterative vs Recursive:
   - Recursive: More intuitive, shorter code, automatic call stack
   - Iterative: Better for very deep trees (no stack overflow), minimal space

2. Different deletion strategies:
   - Inorder successor: Always find rightmost node, simpler but changes structure
   - Inorder predecessor: Find leftmost node, also simple
   - Choose based on preference and specific requirements

3. Value handling:
   - Allow duplicates: Requires additional logic
   - Reject duplicates: Simpler, maintains unique values property

4. Balancing strategies:
   - Maintain balance during insertion (like AVL trees)
   - Delete balanced tree periodically (like B-trees)
   - No explicit balancing (simple BST)

Practical Applications:

1. Database indexing systems
2. Dictionary implementations
3. Symbol tables in compilers
4. Sorting algorithms (tree sort)
5. Network routing algorithms
6. Binary search optimization
7. Decision support systems
8. Network routing and routing tables
9. Range queries and interval data structures
10. Implementation of other balanced tree structures

Edge Cases and Considerations:

1. Empty tree: All operations should handle None/root case
2. Duplicate values: Should be rejected or handled consistently
3. Deleting node with two children: Requires careful successor/predecessor selection
4. Deleting root node: Special case if root has one or two children
5. Skewed trees: Performance degrades to O(n), consider rotation or balancing
6. Very large trees: Memory considerations and recursion depth limits
7. Concurrent access: Not thread-safe, requires synchronization
8. Persistent trees: Version control requires different data structures

Implementation Notes:

- Python's typing module is used for type annotations
- Input validation ensures robust error handling
- Docstrings provide comprehensive documentation
- Test cases in __main__ demonstrate all operations
