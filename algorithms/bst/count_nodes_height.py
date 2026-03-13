"""
Count Nodes and Tree Height in Binary Search Tree

ALGORITHM OVERVIEW:
This module provides algorithms to count the number of nodes and calculate the
height of a Binary Search Tree (BST). These are fundamental operations that help
understand the size and shape of the tree structure.

MATHEMATICAL FOUNDATION:

Node Count (n):
- A tree with root r has n nodes if 1 + nodes(r.left) + nodes(r.right) = n
- This is a classic recurrence relation: f(n) = f(n-1) + f(n-2) + 1 (similar to Fibonacci)

Tree Height (h):
- Height is the number of edges on the longest path from root to leaf
- Or equivalently, the number of nodes on the longest path minus 1
- Empty tree has height -1 or 0 depending on definition (here we use 0 for single node)
- Balanced BST: height ≈ log₂(n)
- Skewed BST: height ≈ n-1

Time Complexity:
- Count nodes: O(n) - must visit every node
- Height: O(n) - must visit every node in worst case
Space Complexity:
- Count nodes: O(h) for recursion stack
- Height: O(h) for recursion stack

TRADE-OFFS:
- Height calculation: Can be done with recursion or simple iterative approach
- Counting nodes: Recursion is most straightforward, could use DFS iterative
- Balanced vs Skewed: Performance identical but tree structure differs

OPTIMIZATIONS:
- For height: can use iterative approach with parent pointers or BFS
- For count nodes: can use Morris traversal to count without recursion

EXAMPLES:

Perfect Binary Tree (height 2, 7 nodes):
        1
       / \
      2   3
     / \ /
    4  5 6

Skewed BST (height 5, 6 nodes):
1
 \
  2
   \
    3
     \
      4
       \
        5

Balanced BST (height 3, 7 nodes):
        4
       / \
      2   6
     / \ / \
    1  3 5  7
"""

from __future__ import annotations
from typing import Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    """Binary tree node with value and child pointers."""
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


class BSTMetrics:
    """Implementation of node counting and height calculation for BSTs."""
    
    @staticmethod
    def count_nodes(root: Optional[TreeNode]) -> int:
        """
        Count the number of nodes in a BST.
        
        Args:
            root: Root of the BST
            
        Returns:
            Total number of nodes in the tree
            
        Time Complexity: O(n) - visits each node exactly once
        Space Complexity: O(h) - recursion stack depth
            
        Mathematical Relation:
            count(root) = 1 + count(root.left) + count(root.right)
            Base case: count(None) = 0
        """
        if root is None:
            return 0
        return 1 + BSTMetrics.count_nodes(root.left) + BSTMetrics.count_nodes(root.right)
    
    @staticmethod
    def count_nodes_iterative(root: Optional[TreeNode]) -> int:
        """
        Iterative implementation of node counting using Morris traversal.
        
        Args:
            root: Root of the BST
            
        Returns:
            Total number of nodes in the tree
            
        Time Complexity: O(n)
        Space Complexity: O(1) - uses Morris traversal to avoid recursion stack
            
        Uses threaded binary tree concept for in-order traversal without extra stack.
        """
        count = 0
        current = root
        
        while current is not None:
            if current.left is None:
                count += 1
                current = current.right
            else:
                # Find inorder successor
                predecessor = current.left
                while predecessor.right is not None and predecessor.right != current:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    count += 1
                    current = current.right
        
        return count
    
    @staticmethod
    def calculate_height(root: Optional[TreeNode]) -> int:
        """
        Calculate the height of a BST (maximum depth from root to leaf).
        
        Args:
            root: Root of the BST
            
        Returns:
            Height of the tree (edges on longest path)
            
        Time Complexity: O(n) - visits all nodes in worst case
        Space Complexity: O(h) - recursion stack depth
            
        Mathematical Relation:
            height(root) = 1 + max(height(root.left), height(root.right))
            Base case: height(None) = -1 (or 0 depending on definition)
        """
        if root is None:
            return -1
        return 1 + max(BSTMetrics.calculate_height(root.left), 
                      BSTMetrics.calculate_height(root.right))
    
    @staticmethod
    def calculate_height_iterative(root: Optional[TreeNode]) -> int:
        """
        Calculate height iteratively using BFS.
        
        Args:
            root: Root of the BST
            
        Returns:
            Height of the tree
            
        Time Complexity: O(n)
        Space Complexity: O(w) where w is max width of tree
        """
        if root is None:
            return -1
            
        height = -1
        queue = [root]
        
        while queue:
            level_size = len(queue)
            height += 1
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return height
    
    @staticmethod
    def calculate_min_max_heights(root: Optional[TreeNode]) -> tuple[int, int]:
        """
        Calculate minimum and maximum heights in the tree.
        
        Args:
            root: Root of the BST
            
        Returns:
            Tuple of (min_height, max_height)
            
        Time Complexity: O(n * w) where w is width
        Space Complexity: O(w)
        """
        if root is None:
            return (0, 0)
            
        min_height = float('inf')
        max_height = -float('inf')
        queue = [(root, 0)]
        
        while queue:
            node, depth = queue.pop(0)
            min_height = min(min_height, depth)
            max_height = max(max_height, depth)
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return (min_height, max_height)
    
    @staticmethod
    def check_balanced(root: Optional[TreeNode]) -> bool:
        """
        Check if a BST is height-balanced (AVL condition).
        
        A tree is balanced if the heights of the two subtrees of any node
        differ by no more than 1.
        
        Args:
            root: Root of the BST
            
        Returns:
            True if balanced, False otherwise
            
        Time Complexity: O(n) - each node checked once
        Space Complexity: O(h)
        """
        def check(node: Optional[TreeNode]) -> tuple[bool, int]:
            if node is None:
                return (True, -1)
                
            left_balanced, left_height = check(node.left)
            if not left_balanced:
                return (False, 0)
                
            right_balanced, right_height = check(node.right)
            if not right_balanced:
                return (False, 0)
                
            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            
            return (balanced, height)
        
        return check(root)[0]


def build_perfect_tree() -> TreeNode:
    """Build a perfect binary tree (height 2, 7 nodes)."""
    #        1
    #       / \
    #      2   3
    #     / \ /
    #    4  5 6
    return TreeNode(1,
                  TreeNode(2,
                        TreeNode(4),
                        TreeNode(5)),
                  TreeNode(3,
                        TreeNode(6)))


def build_skewed_tree() -> TreeNode:
    """Build a right-skewed BST (height 4, 5 nodes)."""
    return TreeNode(1,
                  None,
                  TreeNode(2,
                        None,
                        TreeNode(3,
                            None,
                            TreeNode(4,
                                None,
                                TreeNode(5))))


def build_balanced_tree() -> TreeNode:
    """Build a balanced BST (height 2, 7 nodes)."""
    #        4
    #       / \
    #      2   6
    #     / \ / \
    #    1  3 5  7
    return TreeNode(4,
                  TreeNode(2,
                        TreeNode(1),
                        TreeNode(3)),
                  TreeNode(6,
                        TreeNode(5),
                        TreeNode(7)))


def main() -> None:
    """Demonstrate node counting and height calculation."""
    print("=" * 70)
    print("BST Node Count and Height Tests")
    print("=" * 70)
    print()
    
    trees = {
        "Perfect Tree": build_perfect_tree(),
        "Skewed Tree": build_skewed_tree(),
        "Balanced Tree": build_balanced_tree(),
    }
    
    for tree_name, tree in trees.items():
        print(f"{tree_name}:")
        print("-" * 70)
        
        count_recursive = BSTMetrics.count_nodes(tree)
        count_iterative = BSTMetrics.count_nodes_iterative(tree)
        
        height_recursive = BSTMetrics.calculate_height(tree)
        height_iterative = BSTMetrics.calculate_height_iterative(tree)
        
        min_height, max_height = BSTMetrics.calculate_min_max_heights(tree)
        is_balanced = BSTMetrics.check_balanced(tree)
        
        print(f"  Nodes:        {count_recursive} (recursive), {count_iterative} (iterative)")
        print(f"  Height:       {height_recursive} (recursive), {height_iterative} (iterative)")
        print(f"  Min Height:   {min_height}")
        print(f"  Max Height:   {max_height}")
        print(f"  Balanced:     {'✓ Yes' if is_balanced else '✗ No'}")
        
        # Expected values
        expected_count = sum(2 ** i for i in range(4))  # 1+2+4 = 7
        expected_height = 2
        if "Perfect" in tree_name:
            expected_count = 7
            expected_height = 2
        elif "Skewed" in tree_name:
            expected_count = 5
            expected_height = 4
        elif "Balanced" in tree_name:
            expected_count = 7
            expected_height = 2
            
        print(f"  Expected:     count={expected_count}, height={expected_height}")
        print(f"  Match:        {'✓' if (count_recursive == expected_count and height_recursive == expected_height) else '✗'}")
    
    print()
    print("Height Analysis:")
    print("-" * 70)
    
    # Compare tree heights
    perfect_h = BSTMetrics.calculate_height(build_perfect_tree())
    skewed_h = BSTMetrics.calculate_height(build_skewed_tree())
    balanced_h = BSTMetrics.calculate_height(build_balanced_tree())
    
    print(f"Perfect tree height: {perfect_h}")
    print(f"Skewed tree height:  {skewed_h}")
    print(f"Balanced tree height: {balanced_h}")
    print()
    print(f"Skewed vs Perfect: {skewed_h} vs {perfect_h} (ratio: {skewed_h/perfect_h:.1f}x)")
    print(f"Skewed vs Balanced: {skewed_h} vs {balanced_h} (ratio: {skewed_h/balanced_h:.1f}x)")
    print()
    print("Key Insight:")
    print("-" * 70)
    print("A skewed tree has O(n) height vs O(log n) for balanced BST")
    print("This dramatically affects BST operation performance")


if __name__ == "__main__":
    main()
