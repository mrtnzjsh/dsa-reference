"""
Binary Search Tree (BST) Algorithm Suite

This module provides comprehensive implementations of Binary Search Tree operations
including insertion, deletion, and searching. BST is a fundamental data structure
that enables efficient data retrieval and management with average-case time complexity
of O(log n) for these operations.

ALGORITHM OVERVIEW
==================
A Binary Search Tree is a node-based binary tree data structure which has the
following properties:
- The left subtree of a node contains only nodes with keys lesser than the node's key
- The right subtree of a node contains only nodes with keys greater than the node's key
- Both the left and right subtrees must also be binary search trees

Mathematical Foundations
------------------------
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

OPERATIONS
==========
1. Search: Find if a value exists in the tree
2. Insert: Add a new value while maintaining BST property
3. Delete: Remove a value while maintaining BST property

Search Operation
----------------
Algorithm: Compare target value with current node's value and recursively search:
- If target equals current node: value found
- If target < current node: search left subtree
- If target > current node: search right subtree

Mathematical complexity:
- Best case: O(log n) if balanced, O(1) if target at root
- Average case: O(log n) if balanced
- Worst case: O(n) if tree is completely unbalanced (skewed)

Insertion Operation
-------------------
Algorithm: Find appropriate position for new value:
- If tree empty: create new root node
- If target < current node: traverse left, insert if empty
- If target > current node: traverse right, insert if empty
- If target equals current: update node's value or handle as duplicate

Mathematical complexity:
- Best case: O(log n) if balanced
- Average case: O(log n)
- Worst case: O(n) for skewed trees

Deletion Operation
-----------------
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

Step-by-Step Example
-------------------

Initial Tree (empty):
```
None
```

After inserting 10:
```
      10
```

After inserting 5:
```
      10
     /
    5
```

After inserting 15:
```
      10
     /  \
    5    15
```

After inserting 7:
```
      10
     /  \
    5    15
     \
      7
```

Search for value 7:
```
Start at root 10: 7 < 10 → go left
Go to node 5: 7 > 5 → go right
Go to node 7: 7 == 7 → found!
```

Delete leaf node 5:
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

Delete node with one child (7):
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

Delete node with two children (15):
Find inorder successor: 17
Copy value, then delete successor
```
      10
       \
        7
       /
      17
```

Time Complexity Analysis
------------------------
Let n be the number of nodes in the tree, h be the height:

Search:
- Best: O(1) (target at root)
- Average: O(log n) for balanced tree
- Worst: O(n) for completely skewed tree

Insertion:
- Best: O(log n) for balanced tree
- Average: O(log n)
- Worst: O(n) for completely skewed tree

Deletion:
- Best: O(log n) for balanced tree
- Average: O(log n)
- Worst: O(n) for completely skewed tree

Space Complexity
---------------
- O(n) total space for n nodes
- O(h) recursion stack space
- O(1) iterative approach uses minimal space

Trade-offs Between Approaches
-----------------------------
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

Practical Applications
----------------------
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

Edge Cases and Considerations
-----------------------------
1. Empty tree: All operations should handle None/root case
2. Duplicate values: Should be rejected or handled consistently
3. Deleting node with two children: Requires careful successor/predecessor selection
4. Deleting root node: Special case if root has one or two children
5. Skewed trees: Performance degrades to O(n), consider rotation or balancing
6. Very large trees: Memory considerations and recursion depth limits
7. Concurrent access: Not thread-safe, requires synchronization
8. Persistent trees: Version control requires different data structures

Implementation Notes
--------------------
- Python's typing module is used for type annotations
- Input validation ensures robust error handling
- Docstrings provide comprehensive documentation
- Test cases in __main__ demonstrate all operations
"""

from __future__ import annotations
from typing import Optional, TypeVar, List
from dataclasses import dataclass, field
import sys


T = TypeVar('T', bound='Comparable')


class Comparable:
    """
    Base class for types that can be compared using standard comparison operators.
    """
    def __lt__(self, other: object) -> bool:
        """Check if this instance is less than another."""
        raise NotImplementedError("Subclasses must implement __lt__")

    def __gt__(self, other: object) -> bool:
        """Check if this instance is greater than another."""
        raise NotImplementedError("Subclasses must implement __gt__")

    def __eq__(self, other: object) -> bool:
        """Check if this instance equals another."""
        raise NotImplementedError("Subclasses must implement __eq__")


@dataclass
class TreeNode:
    """
    Represents a node in a Binary Search Tree.

    Attributes:
        value: The value stored in the node
        left: Reference to the left child node (Optional[TreeNode])
        right: Reference to the right child node (Optional[TreeNode])

    Mathematical Properties:
        - Invariant: left.value < node.value < right.value when both exist
        - This invariant must be maintained during all operations
    """
    value: T
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None

    def __repr__(self) -> str:
        """String representation of the node."""
        return f"TreeNode(value={self.value!r})"


class BinarySearchTree:
    """
    Binary Search Tree implementation with search, insert, and delete operations.

    This class provides all core BST operations with comprehensive error handling.

    Mathematical Properties:
        - BST Property: For any node x, all nodes in left subtree have values < x.value
        - Inorder Traversal: Returns values in ascending order
        - Height: Maximum depth from root to any leaf node

    Example:
        >>> bst = BinarySearchTree()
        >>> bst.insert(10)
        >>> bst.insert(5)
        >>> bst.insert(15)
        >>> bst.search(5)
        True
        >>> bst.search(7)
        False
        >>> bst.delete(10)
        >>> bst.search(10)
        False
    """

    def __init__(self):
        """Initialize an empty Binary Search Tree."""
        self.root: Optional[TreeNode] = None
        self._node_count = 0

    @property
    def size(self) -> int:
        """
        Get the number of nodes in the tree.

        Returns:
            int: Number of nodes in the BST
        """
        return self._node_count

    def is_empty(self) -> bool:
        """
        Check if the BST is empty.

        Returns:
            bool: True if tree has no nodes, False otherwise
        """
        return self._node_count == 0

    def search(self, value: T) -> bool:
        """
        Search for a value in the BST.

        Algorithm:
        1. Start at root node
        2. If target equals current node: return True (found)
        3. If target less than current: traverse left subtree
        4. If target greater than current: traverse right subtree
        5. If leaf node reached: return False (not found)

        Time Complexity:
            Best: O(1) - target at root
            Average: O(log n) - balanced tree
            Worst: O(n) - completely skewed tree

        Space Complexity:
            O(h) for recursion (h = height), O(1) for iterative

        Args:
            value: Value to search for in the tree

        Returns:
            bool: True if value exists in tree, False otherwise

        Raises:
            TypeError: If value is not comparable with existing tree values
        """
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def insert(self, value: T) -> bool:
        """
        Insert a new value into the BST while maintaining BST property.

        Algorithm:
        1. If tree empty: create new root node
        2. Start at root node
        3. If target less than current: traverse left
        4. If target greater than current: traverse right
        5. If empty position found: create new node
        6. If duplicate: return False (no insertion)

        Time Complexity:
            Best: O(log n) - balanced tree
            Average: O(log n)
            Worst: O(n) - completely skewed tree

        Space Complexity:
            O(1) for iterative approach

        Args:
            value: Value to insert into the tree

        Returns:
            bool: True if insertion was successful, False if value already exists

        Raises:
            TypeError: If value is not comparable with existing tree values

        Examples:
            >>> bst = BinarySearchTree()
            >>> bst.insert(10)
            True
            >>> bst.insert(10)
            False
            >>> bst.insert(5)
            True
            >>> bst.insert(15)
            True
        """
        if self.root is None:
            self.root = TreeNode(value)
            self._node_count += 1
            return True

        current = self.root
        while True:
            if value == current.value:
                return False  # Duplicate value, don't insert
            elif value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    self._node_count += 1
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    self._node_count += 1
                    return True
                current = current.right

    def delete(self, value: T) -> bool:
        """
        Delete a value from the BST while maintaining BST property.

        Three Cases for Deletion:
        Case 1: Leaf Node - Simply remove the node
        Case 2: One Child - Replace node with its child
        Case 3: Two Children - Replace with inorder successor or predecessor

        Inorder Successor:
        - Smallest value in right subtree
        - Found by going left until no left child exists
        - Has no left child (by definition)

        Inorder Predecessor:
        - Largest value in left subtree
        - Found by going right until no right child exists

        Time Complexity:
            Best: O(log n) - balanced tree
            Average: O(log n)
            Worst: O(n) - completely skewed tree

        Space Complexity:
            O(1) for iterative approach

        Args:
            value: Value to delete from the tree

        Returns:
            bool: True if deletion was successful, False if value not found

        Raises:
            TypeError: If value is not comparable with existing tree values

        Examples:
            >>> bst = BinarySearchTree()
            >>> for v in [10, 5, 15]:
            ...     bst.insert(v)
            >>> bst.delete(10)
            True
            >>> bst.size
            2
            >>> bst.delete(20)
            False
        """
        # Find the node to delete and its parent
        parent = None
        current = self.root

        while current is not None and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        # Value not found
        if current is None:
            return False

        # Case 1: Node has no children (leaf node)
        if current.left is None and current.right is None:
            # Update parent's pointer
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
            self._node_count -= 1
            return True

        # Case 2: Node has only one child
        elif current.left is None or current.right is None:
            child = current.left if current.left is not None else current.right

            # Update parent's pointer
            if parent is None:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child
            self._node_count -= 1
            return True

        # Case 3: Node has two children
        else:
            # Find inorder successor (smallest in right subtree)
            successor_parent = current
            successor = current.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            # Copy successor's value to current node
            current.value = successor.value

            # Delete successor (which has at most one right child)
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

            self._node_count -= 1
            return True

    def inorder_traversal(self) -> List[T]:
        """
        Perform inorder traversal of the BST.

        Inorder traversal visits nodes in ascending order:
        - Left subtree
        - Current node
        - Right subtree

        Time Complexity: O(n) - visits each node exactly once
        Space Complexity: O(h) for recursion, O(n) for all nodes in worst case

        Returns:
            List[T]: Values in ascending order

        Examples:
            >>> bst = BinarySearchTree()
            >>> for v in [10, 5, 15, 7, 12, 20]:
            ...     bst.insert(v)
            >>> bst.inorder_traversal()
            [5, 7, 10, 12, 15, 20]
        """
        result: List[T] = []

        def _inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            _inorder(node.left)
            result.append(node.value)
            _inorder(node.right)

        _inorder(self.root)
        return result

    def preorder_traversal(self) -> List[T]:
        """
        Perform preorder traversal of the BST.

        Preorder traversal visits nodes in root-left-right order:
        - Current node
        - Left subtree
        - Right subtree

        Time Complexity: O(n) - visits each node exactly once
        Space Complexity: O(h) for recursion, O(n) for all nodes in worst case

        Returns:
            List[T]: Values in preorder traversal order

        Examples:
            >>> bst = BinarySearchTree()
            >>> for v in [10, 5, 15]:
            ...     bst.insert(v)
            >>> bst.preorder_traversal()
            [10, 5, 15]
        """
        result: List[T] = []

        def _preorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            result.append(node.value)
            _preorder(node.left)
            _preorder(node.right)

        _preorder(self.root)
        return result

    def postorder_traversal(self) -> List[T]:
        """
        Perform postorder traversal of the BST.

        Postorder traversal visits nodes in left-right-root order:
        - Left subtree
        - Right subtree
        - Current node

        Time Complexity: O(n) - visits each node exactly once
        Space Complexity: O(h) for recursion, O(n) for all nodes in worst case

        Returns:
            List[T]: Values in postorder traversal order

        Examples:
            >>> bst = BinarySearchTree()
            >>> for v in [10, 5, 15]:
            ...     bst.insert(v)
            >>> bst.postorder_traversal()
            [5, 15, 10]
        """
        result: List[T] = []

        def _postorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            _postorder(node.left)
            _postorder(node.right)
            result.append(node.value)

        _postorder(self.root)
        return result

    def find_min(self) -> Optional[T]:
        """
        Find the minimum value in the BST.

        The minimum value is the leftmost node (following left pointers).

        Time Complexity:
            Best: O(1) - tree with only root
            Average: O(log n) - balanced tree
            Worst: O(n) - completely skewed tree

        Space Complexity: O(1)

        Returns:
            Optional[T]: Minimum value, or None if tree is empty

        Examples:
            >>> bst = BinarySearchTree()
            >>> for v in [15, 10, 20, 5]:
            ...     bst.insert(v)
            >>> bst.find_min()
            5
            >>> bst.delete(5)
            True
            >>> bst.find_min()
            10
        """
        if self.root is None:
            return None

        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self) -> Optional[T]:
        """
        Find the maximum value in the BST.

        The maximum value is the rightmost node (following right pointers).

        Time Complexity:
            Best: O(1) - tree with only root
            Average: O(log n) - balanced tree
            Worst: O(n) - completely skewed tree

        Space Complexity: O(1)

        Returns:
            Optional[T]: Maximum value, or None if tree is empty

        Examples:
            >>> bst = BinarySearchTree()
            >>> for v in [15, 10, 20, 25]:
            ...     bst.insert(v)
            >>> bst.find_max()
            25
            >>> bst.delete(25)
            True
            >>> bst.find_max()
            20
        """
        if self.root is None:
            return None

        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def find_ancestor(self, value1: T, value2: T) -> Optional[T]:
        """
        Find the lowest common ancestor (LCA) of two values in the BST.

        Algorithm:
        1. Start at root
        2. If both values are less than current: go left
        3. If both values are greater than current: go right
        4. Otherwise: current node is the LCA

        Time Complexity:
            Best: O(1) - values at root
            Average: O(log n) - balanced tree
            Worst: O(n) - completely skewed tree

        Space Complexity: O(1) for iterative approach

        Args:
            value1: First value
            value2: Second value

        Returns:
            Optional[T]: Lowest common ancestor value, or None if tree is empty

        Examples:
            >>> bst = BinarySearchTree()
            >>> for v in [10, 5, 15, 7, 12, 20]:
            ...     bst.insert(v)
            >>> bst.find_ancestor(5, 7)
            10
            >>> bst.find_ancestor(7, 15)
            10
            >>> bst.find_ancestor(5, 20)
            10
        """
        if self.root is None:
            return None

        current = self.root
        while True:
            if value1 < current.value and value2 < current.value:
                current = current.left
            elif value1 > current.value and value2 > current.value:
                current = current.right
            else:
                return current.value

    def get_height(self) -> int:
        """
        Get the height of the BST.

        Height is the maximum depth of any node from the root.
        Empty tree has height -1, single node has height 0.

        Time Complexity: O(n) - visits all nodes
        Space Complexity: O(h) for recursion, O(n) in worst case

        Returns:
            int: Height of the tree

        Examples:
            >>> bst = BinarySearchTree()
            >>> bst.get_height()
            -1
            >>> bst.insert(10)
            True
            >>> bst.get_height()
            0
            >>> bst.insert(5)
            True
            >>> bst.insert(15)
            True
            >>> bst.get_height()
            1
        """
        def _height(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1
            left_height = _height(node.left)
            right_height = _height(node.right)
            return max(left_height, right_height) + 1

        return _height(self.root)

    def get_depth(self, value: T) -> Optional[int]:
        """
        Get the depth (level) of a value in the BST.

        Depth is the number of edges from root to node.
        Root node has depth 0, children have depth 1, etc.

        Time Complexity:
            Best: O(log n) - balanced tree
            Average: O(log n)
            Worst: O(n) - completely skewed tree

        Space Complexity: O(h) for recursion, O(1) for iterative

        Args:
            value: Value to find depth for

        Returns:
            Optional[int]: Depth of value, or None if value not found

        Examples:
            >>> bst = BinarySearchTree()
            >>> for v in [10, 5, 15, 7, 12]:
            ...     bst.insert(v)
            >>> bst.get_depth(10)
            0
            >>> bst.get_depth(5)
            1
            >>> bst.get_depth(7)
            2
            >>> bst.get_depth(99)
            None
        """
        if self.root is None:
            return None

        depth = 0
        current = self.root

        while current is not None:
            if value == current.value:
                return depth
            elif value < current.value:
                current = current.left
            else:
                current = current.right
            depth += 1

        return None

    def range_query(self, min_val: T, max_val: T) -> List[T]:
        """
        Find all values in a specified range.

        Uses the BST property to efficiently traverse only relevant nodes.

        Time Complexity:
            Best: O(k + log n) where k is number of matching values
            Average: O(k + log n)
            Worst: O(n) if range includes all values

        Space Complexity: O(k) for result list

        Args:
            min_val: Minimum value (inclusive)
            max_val: Maximum value (inclusive)

        Returns:
            List[T]: All values in the range

        Examples:
            >>> bst = BinarySearchTree()
            >>> for v in [10, 5, 15, 7, 12, 20, 3, 8, 18, 25]:
            ...     bst.insert(v)
            >>> bst.range_query(7, 18)
            [7, 8, 10, 12, 15, 18]
            >>> bst.range_query(1, 4)
            [3]
        """
        result: List[T] = []

        def _range_query(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            if min_val < node.value:
                _range_query(node.left)

            if min_val <= node.value <= max_val:
                result.append(node.value)

            if max_val > node.value:
                _range_query(node.right)

        _range_query(self.root)
        return result

    def __len__(self) -> int:
        """
        Get the number of nodes in the tree.

        Returns:
            int: Number of nodes
        """
        return self._node_count

    def __str__(self) -> str:
        """
        String representation of the tree.

        Returns:
            str: String representation of tree structure
        """
        if self.root is None:
            return "Empty BST"

        lines = []
        self._build_string(self.root, "", True, lines)
        return "\n".join(lines)

    def _build_string(self, node: Optional[TreeNode], prefix: str, is_tail: bool,
                      lines: List[str]) -> None:
        """Helper method to build string representation of tree."""
        if node is not None:
            lines.append(f"{prefix}{'└── ' if is_tail else '├── '}{node.value}")

            child_prefix = prefix + ("    " if is_tail else "│   ")
            if node.right is not None or node.left is not None:
                # Always add right child marker (it might be None)
                self._build_string(node.right, child_prefix, node.left is None, lines)


class IntegerBST(BinarySearchTree):
    """
    Convenience class for Binary Search Trees with integer values.

    Provides type hints and common operations for integer-valued BSTs.
    """

    def search(self, value: int) -> bool:
        """Search for an integer value in the tree."""
        return super().search(value)

    def insert(self, value: int) -> bool:
        """Insert an integer value into the tree."""
        return super().insert(value)

    def delete(self, value: int) -> bool:
        """Delete an integer value from the tree."""
        return super().delete(value)

    def find_min(self) -> Optional[int]:
        """Find the minimum integer value in the tree."""
        return super().find_min()

    def find_max(self) -> Optional[int]:
        """Find the maximum integer value in the tree."""
        return super().find_max()


class ComparableInt(Comparable):
    """Comparable integer type for use in Generic BST."""

    def __init__(self, value: int):
        """Initialize a comparable integer."""
        self._value = value

    def __lt__(self, other: object) -> bool:
        """Check if this integer is less than another."""
        if not isinstance(other, ComparableInt):
            return NotImplemented
        return self._value < other._value

    def __gt__(self, other: object) -> bool:
        """Check if this integer is greater than another."""
        if not isinstance(other, ComparableInt):
            return NotImplemented
        return self._value > other._value

    def __eq__(self, other: object) -> bool:
        """Check if this integer equals another."""
        if not isinstance(other, ComparableInt):
            return NotImplemented
        return self._value == other._value

    def __repr__(self) -> str:
        """String representation."""
        return f"ComparableInt({self._value})"


def build_bst_from_sorted_list(sorted_list: List[T]) -> BinarySearchTree:
    """
    Build a balanced BST from a sorted list.

    This creates a minimum-height tree from sorted input.
    This is the construction method for balanced BSTs.

    Algorithm:
        - Divide list into two halves
        - Middle element becomes root
        - Left half becomes left subtree
        - Right half becomes right subtree
        - Recursively apply

    Time Complexity: O(n) - each element visited once
    Space Complexity: O(n) - creates n nodes, O(log n) recursion

    Args:
        sorted_list: Sorted list of values (ascending order)

    Returns:
        BinarySearchTree: Balanced BST built from sorted list

    Examples:
        >>> sorted_list = [1, 3, 5, 7, 9, 11]
        >>> bst = build_bst_from_sorted_list(sorted_list)
        >>> bst.get_height()
        2
        >>> bst.inorder_traversal()
        [1, 3, 5, 7, 9, 11]
    """
    def _build(sorted_list: List[T], start: int, end: int) -> Optional[TreeNode]:
        """Helper method to build balanced BST."""
        if start > end:
            return None

        mid = (start + end) // 2
        node = TreeNode(sorted_list[mid])
        node.left = _build(sorted_list, start, mid - 1)
        node.right = _build(sorted_list, mid + 1, end)

        return node

    bst = BinarySearchTree()
    bst.root = _build(sorted_list, 0, len(sorted_list) - 1)
    bst._node_count = len(sorted_list)
    return bst


def bst_operations_example() -> None:
    """Comprehensive example demonstrating all BST operations."""
    print("BST Operations Demonstration\n")
    print("=" * 50)

    # Create a new BST
    bst = BinarySearchTree()
    print(f"Created empty BST: {bst}")

    # Insert example
    print("\n1. Insertion Example:")
    print("-" * 50)
    insert_values = [50, 30, 70, 20, 40, 60, 80, 35]
    print(f"Inserting values: {insert_values}")

    for value in insert_values:
        success = bst.insert(value)
        status = "✓" if success else "✗"
        print(f"  {status} Inserted {value} (size: {bst.size})")

    print(f"\nFinal tree structure:")
    print(bst)
    print(f"\nTree stats: height={bst.get_height()}, size={bst.size}")

    # Inorder traversal
    print("\nInorder traversal (ascending order):")
    print(f"  {bst.inorder_traversal()}")

    # Search examples
    print("\n2. Search Examples:")
    print("-" * 50)
    search_values = [35, 25, 90]
    for value in search_values:
        found = bst.search(value)
        status = "✓ Found" if found else "✗ Not found"
        print(f"  {status}: Searching for {value}")

    # Find min and max
    print("\n3. Min/Max Values:")
    print("-" * 50)
    print(f"  Minimum: {bst.find_min()}")
    print(f"  Maximum: {bst.find_max()}")

    # Range query
    print("\n4. Range Query:")
    print("-" * 50)
    min_range, max_range = 25, 65
    result = bst.range_query(min_range, max_range)
    print(f"  Values between {min_range} and {max_range}: {result}")

    # Depth queries
    print("\n5. Depth Queries:")
    print("-" * 50)
    depths = [50, 30, 70, 20, 35]
    for value in depths:
        depth = bst.get_depth(value)
        status = "Found at depth" if depth is not None else "Not found"
        print(f"  {status}: {value} → {depth if depth is not None else 'N/A'}")

    # Ancestor query
    print("\n6. Lowest Common Ancestor:")
    print("-" * 50)
    pairs = [(35, 40), (20, 80), (25, 65), (30, 70)]
    for val1, val2 in pairs:
        ancestor = bst.find_ancestor(val1, val2)
        if ancestor is not None:
            print(f"  LCA of {val1} and {val2}: {ancestor}")
        else:
            print(f"  One or both values not found")

    # Deletion examples
    print("\n7. Deletion Examples:")
    print("-" * 50)

    # Case 1: Delete leaf node
    print("\n  a) Delete leaf node 20:")
    print(f"    Before: {bst}")
    bst.delete(20)
    print(f"    After: {bst}")
    print(f"    Size: {bst.size}")

    # Case 2: Delete node with one child
    print("\n  b) Delete node with one child (70 → 80):")
    print(f"    Before: {bst}")
    bst.delete(70)
    print(f"    After: {bst}")
    print(f"    Size: {bst.size}")

    # Case 3: Delete node with two children
    print("\n  c) Delete node with two children (50):")
    print(f"    Before: {bst}")
    bst.delete(50)
    print(f"    After: {bst}")
    print(f"    Size: {bst.size}")

    # Tree sort example
    print("\n8. Tree Sort Example:")
    print("-" * 50)
    unsorted = [34, 7, 23, 32, 5, 62]
    print(f"  Unsorted list: {unsorted}")
    bst_sort = BinarySearchTree()
    for value in unsorted:
        bst_sort.insert(value)
    sorted_list = bst_sort.inorder_traversal()
    print(f"  Sorted list:   {sorted_list}")

    # Balanced BST from sorted list
    print("\n9. Balanced BST from Sorted List:")
    print("-" * 50)
    sorted_list = [10, 20, 30, 40, 50, 60]
    balanced_bst = build_bst_from_sorted_list(sorted_list)
    print(f"  Original list: {sorted_list}")
    print(f"  After balancing:")
    print(balanced_bst)
    print(f"  Height: {balanced_bst.get_height()}")
    print(f"  Traversal: {balanced_bst.inorder_traversal()}")


if __name__ == "__main__":
    """Main execution with comprehensive examples."""
    try:
        bst_operations_example()
        print("\n" + "=" * 50)
        print("All BST operations demonstrated successfully!")
    except Exception as e:
        print(f"\nError running demonstration: {e}")
        sys.exit(1)
