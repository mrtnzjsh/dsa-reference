"""
Build Binary Search Tree from Sorted Array

This module provides algorithms to construct a balanced Binary Search Tree (BST) 
from a sorted array, demonstrating a fundamental technique for maintaining tree 
balance through pre-processing.
"""

from __future__ import annotations

from typing import List, Optional, Tuple


class TreeNode:
    """Node class for Binary Search Tree.
    
    Attributes:
        val: The value stored in the node
        left: Reference to left child node
        right: Reference to right child node
    """

    def __init__(
        self, val: int, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None
    ):
        """Initialize a new tree node.
        
        Args:
            val: The value to store in the node
            left: Optional left child node
            right: Optional right child node
        """
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """Return string representation of node."""
        return f"TreeNode({self.val})"


def build_balanced_bst(
    sorted_arr: List[int],
) -> Optional[TreeNode]:
    """Build a balanced BST from a sorted array.
    
    This algorithm creates a balanced BST by recursively selecting the middle 
    element as the root, then recursively building subtrees from left and right 
    halves. This ensures the tree remains height-balanced.
    
    Mathematical Foundation:
    - A balanced BST has height h ≈ log₂(n), where n is the number of elements
    - Selecting the median element as root minimizes tree height
    - The property holds: height(left) ≤ h-1 and height(right) ≤ h-1
    - Recursive construction: T(n) = 2T(n/2) + O(1)
    
    Step-by-Step Example:
    Input: [1, 2, 3, 4, 5]
    
    1. Pick middle element: index = (0 + 4) // 2 = 2 → value = 3
       Tree:       3
                 / \
                1   5
               
    2. Build left subtree from [1, 2]
       - Pick middle: index = (0 + 1) // 2 = 0 → value = 1
       Tree:       3
                 / \
                1   5
               / \
              (empty)
         
    3. Build right subtree from [4]
       - Single element
       Tree:       3
                 / \
                1   5
                   /
                  4
               
    Final Height: 2 (root level + 2)
    Inorder Traversal: [1, 2, 3, 4, 5] ✓

    Args:
        sorted_arr: Sorted list of integers (non-decreasing order)
    
    Returns:
        Root node of the balanced BST, or None if array is empty
    
    Time Complexity: O(n)
        - Each element is visited exactly once during construction
        - The recursion creates O(log n) levels for balanced trees
    
    Space Complexity: O(n)
        - O(n) for the tree nodes
        - O(log n) for recursion stack in balanced case
    
    Trade-offs:
        Insertion Method:
            - Build balanced: O(n) total, maintains balance
            - Sequential insert: O(n log n), can become unbalanced
            - Best for: Pre-processed sorted data, maintaining balance
            - Worst for: Random insertion order without rebalancing
        
        Sorted Array Building:
            ✓ Optimal for sorted input
            ✓ Always produces balanced tree
            ✓ Minimal total complexity
            ✗ Requires sorted input
            ✗ Extra memory for temporary arrays (if implemented iteratively)
        
        Sequential Insertion:
            ✓ Works with any input order
            ✓ No pre-processing required
            ✗ Can create skewed trees
            ✗ O(n log n) worst-case for sorted input
    
    Practical Applications:
        1. Tree Sorting: Convert sorted array to BST then perform inorder traversal
        2. Efficient Range Queries: O(log n) access to min/max values
        3. Order Statistics: Quick find of k-th smallest element
        4. Data Structure Construction: Building balanced structures for use cases
        5. Database Indexing: Creating balanced index structures from sorted data
    
    Edge Cases:
        - Empty array: Returns None
        - Single element: Returns node with that element, height = 0
        - Duplicates: Implementation includes last element on right side
          Example: [1, 1, 2] → root=2, left subtree=[1,1]
    
    Raises:
        TypeError: If input is not a list or contains non-integer elements
    """
    if not isinstance(sorted_arr, list):
        raise TypeError("Input must be a list")
    
    for item in sorted_arr:
        if not isinstance(item, int):
            raise TypeError("All elements must be integers")
    
    if len(sorted_arr) == 0:
        return None
    
    def _build_recursive(
        left: int, right: int
    ) -> Optional[TreeNode]:
        """Recursively build balanced BST from sorted subarray.
        
        Args:
            left: Left index of current subarray
            right: Right index of current subarray
        
        Returns:
            Root node of balanced BST for subarray
        """
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = TreeNode(sorted_arr[mid])
        node.left = _build_recursive(left, mid - 1)
        node.right = _build_recursive(mid + 1, right)
        return node
    
    return _build_recursive(0, len(sorted_arr) - 1)


def calculate_tree_height(root: Optional[TreeNode]) -> int:
    """Calculate the height of a binary tree.
    
    Height is defined as the number of edges on the longest path from root to leaf.
    
    Args:
        root: Root node of the tree
    
    Returns:
        Height of the tree (0 for empty tree)
    
    Time Complexity: O(n)
        - Each node visited exactly once
    """
    if root is None:
        return 0
    return 1 + max(calculate_tree_height(root.left), calculate_tree_height(root.right))


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Perform inorder traversal of BST.
    
    Inorder traversal of BST visits nodes in ascending order.
    
    Args:
        root: Root node of the tree
    
    Returns:
        List of values in ascending order
    """
    result = []
    
    def _traverse(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        _traverse(node.left)
        result.append(node.val)
        _traverse(node.right)
    
    _traverse(root)
    return result


def print_tree_structure(root: Optional[TreeNode]) -> str:
    """Print tree structure for visualization.
    
    Args:
        root: Root node of the tree
    
    Returns:
        String representation of tree structure
    """
    if root is None:
        return "Empty tree"
    
    lines = []
    current = [root]
    
    while current:
        next_level = []
        line_values = []
        
        for node in current:
            if node:
                line_values.append(str(node.val))
                next_level.append(node.left)
                next_level.append(node.right)
            else:
                line_values.append("N")
        
        lines.append(" ".join(line_values))
        current = next_level
    
    return "\n".join(lines)


if __name__ == "__main__":
    """Example usage and demonstration of the algorithm."""
    
    # Example 1: Balanced BST from sorted array
    print("=" * 50)
    print("Example 1: Building Balanced BST from [1, 2, 3, 4, 5]")
    print("=" * 50)
    
    sorted_array = [1, 2, 3, 4, 5]
    root = build_balanced_bst(sorted_array)
    
    print("\nInput array:", sorted_array)
    print("\nTree Structure:")
    print(print_tree_structure(root))
    
    height = calculate_tree_height(root)
    print(f"\nTree Height: {height}")
    print(f"Expected height for 5 nodes: log₂(5) ≈ 2.32 → ceil: 3")
    
    inorder_result = inorder_traversal(root)
    print(f"Inorder Traversal: {inorder_result}")
    print(f"Is sorted: {inorder_result == sorted(sorted_array)}")
    
    # Example 2: Single element array
    print("\n" + "=" * 50)
    print("Example 2: Single Element [7]")
    print("=" * 50)
    
    single_element = [7]
    root = build_balanced_bst(single_element)
    print("\nInput array:", single_element)
    print("\nTree Structure:")
    print(print_tree_structure(root))
    print(f"\nTree Height: {calculate_tree_height(root)}")
    print(f"Inorder Traversal: {inorder_traversal(root)}")
    
    # Example 3: Empty array
    print("\n" + "=" * 50)
    print("Example 3: Empty Array []")
    print("=" * 50)
    
    empty_array = []
    root = build_balanced_bst(empty_array)
    print("\nInput array:", empty_array)
    print("\nTree Structure:")
    print(print_tree_structure(root))
    print(f"\nTree Height: {calculate_tree_height(root)}")
    print(f"Inorder Traversal: {inorder_traversal(root)}")
    
    # Example 4: Array with duplicates
    print("\n" + "=" * 50)
    print("Example 4: Array with Duplicates [1, 1, 2, 3, 4]")
    print("=" * 50)
    
    duplicates_array = [1, 1, 2, 3, 4]
    root = build_balanced_bst(duplicates_array)
    
    print("\nInput array:", duplicates_array)
    print("\nTree Structure:")
    print(print_tree_structure(root))
    print(f"\nTree Height: {calculate_tree_height(root)}")
    print(f"Inorder Traversal: {inorder_traversal(root)}")
    print(f"Original array: {sorted_array}")
    
    # Example 5: Increasing sequence (worst case for sequential insert, best for our algorithm)
    print("\n" + "=" * 50)
    print("Example 5: Increasing Sequence [10, 20, 30, 40, 50, 60, 70]")
    print("=" * 50)
    
    increasing_array = [10, 20, 30, 40, 50, 60, 70]
    root = build_balanced_bst(increasing_array)
    
    print("\nInput array:", increasing_array)
    print("\nTree Structure:")
    print(print_tree_structure(root))
    print(f"\nTree Height: {calculate_tree_height(root)}")
    print(f"Expected height for 7 nodes: log₂(7) ≈ 2.81 → ceil: 3")
    print(f"Inorder Traversal: {inorder_traversal(root)}")
    
    # Complexity comparison
    print("\n" + "=" * 50)
    print("Complexity Analysis")
    print("=" * 50)
    print("\nFor building BST from n elements:")
    print("- Time Complexity: O(n)")
    print("  * Each element processed exactly once")
    print("  * No nested loops, pure linear scan")
    print("\n- Space Complexity: O(n)")
    print("  * O(n) for tree nodes")
    print("  * O(log n) recursion stack for balanced tree")
    print("\nBenefits of building from sorted array:")
    print("  ✓ Always produces balanced tree")
    print("  ✓ Minimal total time complexity")
    print("  ✓ Enables O(log n) search, insert, delete")
    print("\nAlternative: Sequential Insertion")
    print("  * Time Complexity: O(n log n)")
    print("  * Can create skewed trees")
    print("  * Requires balancing algorithm (AVL, Red-Black)")
