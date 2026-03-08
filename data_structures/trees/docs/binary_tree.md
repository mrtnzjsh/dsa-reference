# Binary Tree

A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child. Binary trees are widely used in computer science for efficient data storage and organization.

## Types of Binary Trees

- Full Binary Tree: Every node has either 0 or 2 children
- Complete Binary Tree: All levels are completely filled except possibly the last level, which is filled from left to right
- Perfect Binary Tree: All internal nodes have two children and all leaves are at the same level
- Balanced Binary Tree: The heights of the two subtrees of any node differ by at most one
- Binary Search Tree: A binary tree where the left subtree contains nodes with keys less than the node's key, and the right subtree contains nodes with keys greater than the node's key

## Time Complexities

### Array-Based Binary Tree

- Access: O(1) - Direct array index access
- Search: O(log n) - Finding an element involves binary search on the array
- Insertion: O(n) - Finding the correct position may require shifting elements
- Deletion: O(n) - Finding and removing an element may require shifting elements

### Node-Based Binary Tree

- Search (BST): O(log n) average case, O(n) worst case
- Insertion: O(log n) average case, O(n) worst case
- Deletion: O(log n) average case, O(n) worst case
- Traversal: O(n) - Visits each node exactly once
- Height/Depth Calculation: O(n) - May need to traverse the entire tree

## Binary Tree Traversals

- In-order: Left node, current node, right node
- Pre-order: Current node, left node, right node
- Post-order: Left node, right node, current node

## Binary Tree In Applications

- Binary Search Trees: Used for efficient searching, insertion, and deletion
- Expression Trees: Represent algebraic expressions in computer algebra systems
- Binary Heaps: Used in priority queues and heap sort algorithms
- Huffman Coding: Used in data compression
- Syntax Trees: Used in compilers to represent the syntax of source code

## Binary Tree In Algorithms

- Tree Traversal: Various traversal methods to visit all nodes
- Tree Recursion: Many tree algorithms naturally use recursive approaches
- Tree Rotations: Used in self-balancing binary search trees
- Heap Operations: Maintaining the heap property through sift-down and sift-up operations
- Pathfinding: Shortest path algorithms in graphs