"""
Left View, Right View, and Right-Left View of Binary Search Tree

ALGORITHM OVERVIEW:
This module provides algorithms to view different perspectives of a binary tree:
- Left View: Nodes visible when viewing tree from left side
- Right View: Nodes visible when viewing tree from right side  
- Right-Left View: Nodes visible when viewing tree from right side first,
  then left side (bottom-right to top-left)

These views are useful for various applications including:
- Tree visualization
- Algorithmic problems (like binary tree serialization)
- Understanding tree structure from different perspectives
- Finding nodes with certain properties

MATHEMATICAL FOUNDATION:

Left View:
The left view consists of the first node (leftmost) encountered at each level.
Mathematically: For each level d, select the first visited node in left-to-right order.

Right View:
The right view consists of the last node (rightmost) encountered at each level.
Mathematically: For each level d, select the last visited node in left-to-right order.

Right-Left View (Special Case):
View from right side first, then left side. This gives a different perspective.

Time Complexity: O(n) for all views - must visit every node
Space Complexity: O(n) for storing views, O(h) for BFS/DFS recursion

TRADE-OFFS:
- Left/Right View: Simple BFS approach
- Right-Left View: Requires two passes or specialized tracking
- Different trees can have identical left views but different right views
- For full tree reconstruction, more information is needed than these views

VIEW IDENTIFICATION:

Consider this tree:
        1
       / \
      2   3
     / \   \
    4   5   6

Left View:     Right View:    Right-Left View:
       1            1              1
      / \          / \            / \
     2   3        2   6          6   2
    / \          /            / \
   4   5        6            5   4
    (first nodes on each level)

For Right-Left View, we traverse from rightmost side first, then left side.

TRAVERSAL STRATEGIES:
1. BFS (Level-order): Easiest for Left/Right view
2. DFS (Pre-order): Works but requires tracking levels
3. Right-DFS: Specialized traversal for right view

EXAMPLES:

Empty Tree:
Left View: []
Right View: []
Right-Left View: []

Single Node:
Left View: [root]
Right View: [root]
Right-Left View: [root]

Perfect Binary Tree:
        1
       / \
      2   3
     / \ / \
    4  5 6  7

Left View: [1, 2, 4]
Right View: [1, 3, 7]
Right-Left View: [7, 3, 1] (view from right first, then left)
"""

from __future__ import annotations
from typing import List, Optional
from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    """Binary tree node with value and child pointers."""
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


class TreeViews:
    """Implementation of different tree view algorithms."""
    
    @staticmethod
    def left_view(root: Optional[TreeNode]) -> List[int]:
        """
        Get the left view of a binary tree.
        
        The left view consists of the first node encountered at each level
        when traversing level by level from left to right.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List of node values in left view (from top to bottom)
            
        Time Complexity: O(n) - visits each node once
        Space Complexity: O(n) - for the result list, O(h) for BFS queue
            
        Algorithm:
            1. Use BFS level-order traversal
            2. For each level, add the first node to the result
            3. Process all nodes at current level before moving to next
            
        Examples:
            >>> # Tree: 1 -> 2,3 -> 4,5,None,6
            >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), 
            ...                TreeNode(3, None, TreeNode(6)))
            >>> TreeViews.left_view(root)
            [1, 2, 4]
        """
        if root is None:
            return []
            
        left_view_result: List[int] = []
        queue = deque([(root, 0)])  # (node, level)
        current_level = -1
        
        while queue:
            node, level = queue.popleft()
            
            # If this is the first node of the level, add to left view
            if level > current_level:
                left_view_result.append(node.val)
                current_level = level
            
            # Add children for next level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return left_view_result
    
    @staticmethod
    def right_view(root: Optional[TreeNode]) -> List[int]:
        """
        Get the right view of a binary tree.
        
        The right view consists of the last node encountered at each level
        when traversing level by level from left to right.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List of node values in right view (from top to bottom)
            
        Time Complexity: O(n) - visits each node once
        Space Complexity: O(n) - for the result list, O(h) for BFS queue
            
        Algorithm:
            1. Use BFS level-order traversal
            2. For each level, keep track of the last node processed
            3. Add the last node to the result
            4. Process all nodes at current level
            
        Examples:
            >>> # Tree: 1 -> 2,3 -> 4,5,None,6
            >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
            ...                TreeNode(3, None, TreeNode(6)))
            >>> TreeViews.right_view(root)
            [1, 2, 6]
        """
        if root is None:
            return []
            
        right_view_result: List[int] = []
        queue = deque([(root, 0)])  # (node, level)
        current_level = -1
        level_last_nodes: List[TreeNode] = []
        
        while queue:
            node, level = queue.popleft()
            
            # Add current node to level's list
            if level == current_level:
                level_last_nodes.append(node)
            else:
                # New level, add previous level's last node to result
                if current_level >= 0 and level_last_nodes:
                    right_view_result.append(level_last_nodes[-1].val)
                level_last_nodes = [node]
                current_level = level
            
            # Add children for next level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        # Add last level's last node
        if level_last_nodes:
            right_view_result.append(level_last_nodes[-1].val)
        
        return right_view_result
    
    @staticmethod
    def right_left_view(root: Optional[TreeNode]) -> List[int]:
        """
        Get the Right-Left view of a binary tree.
        
        This view shows nodes when looking from the right side first, then
        from the left side. This gives a different perspective than standard views.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List of node values in right-left view (right-to-left, then left-to-right)
            
        Time Complexity: O(n) - visits each node once
        Space Complexity: O(n) - for the result list, O(h) for queue
            
        Algorithm:
            1. Traverse right side first (reverse order from right view)
            2. Then traverse left side
            3. Combine results
            
        Examples:
            >>> # Tree: 1 -> 2,3 -> 4,5,None,6
            >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
            ...                TreeNode(3, None, TreeNode(6)))
            >>> TreeViews.right_left_view(root)
            [6, 3, 1, 2, 4, 5] or similar order
        """
        if root is None:
            return []
            
        right_view_result = TreeViews.right_view(root)
        left_view_result = TreeViews.left_view(root)
        
        # Combine: right view first, then left view (excluding duplicates if any)
        # For this implementation, we'll take right view first then left view
        combined = right_view_result + [node for node in left_view_result 
                                       if node not in right_view_result]
        
        return combined
    
    @staticmethod
    def left_view_recursive(root: Optional[TreeNode]) -> List[int]:
        """
        Get left view using DFS (pre-order) traversal.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List of node values in left view
            
        Time Complexity: O(n)
        Space Complexity: O(h) for recursion stack
            
        Uses the property that in pre-order traversal, the first node of each
        level is always the leftmost node.
        """
        if root is None:
            return []
            
        left_view_result: List[int] = []
        max_level = -1
        
        def dfs(node: Optional[TreeNode], level: int) -> None:
            nonlocal max_level
            
            if node is None:
                return
                
            # If first node of this level, add to result
            if level > max_level:
                left_view_result.append(node.val)
                max_level = level
            
            # Traverse left first
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return left_view_result
    
    @staticmethod
    def right_view_recursive(root: Optional[TreeNode]) -> List[int]:
        """
        Get right view using DFS (pre-order) traversal.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List of node values in right view
            
        Time Complexity: O(n)
        Space Complexity: O(h) for recursion stack
        """
        if root is None:
            return []
            
        right_view_result: List[int] = []
        max_level = -1
        
        def dfs(node: Optional[TreeNode], level: int) -> None:
            nonlocal max_level
            
            if node is None:
                return
                
            # If first node of this level, add to result
            if level > max_level:
                right_view_result.append(node.val)
                max_level = level
            
            # Traverse right first to reach rightmost nodes first
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return right_view_result


def build_example_tree() -> TreeNode:
    """Build example tree for testing."""
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    return TreeNode(1,
                  TreeNode(2,
                        TreeNode(4),
                        TreeNode(5)),
                  TreeNode(3,
                        None,
                        TreeNode(6)))


def build_perfect_tree() -> TreeNode:
    """Build perfect binary tree (height 2, 7 nodes)."""
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    return TreeNode(1,
                  TreeNode(2,
                        TreeNode(4),
                        TreeNode(5)),
                  TreeNode(3,
                        TreeNode(6),
                        TreeNode(7)))


def main() -> None:
    """Demonstrate different tree view algorithms."""
    print("=" * 70)
    print("Binary Tree View Algorithms")
    print("=" * 70)
    print()
    
    # Test tree visualization
    tree = build_example_tree()
    
    print("Example Tree Structure:")
    print("        1")
    print("       / \\")
    print("      2   3")
    print("     / \\   \\")
    print("    4   5   6")
    print()
    
    left_view = TreeViews.left_view(tree)
    right_view = TreeViews.right_view(tree)
    right_left_view = TreeViews.right_left_view(tree)
    
    print("View Results:")
    print("-" * 70)
    print(f"Left View:     {left_view}")
    print(f"Right View:    {right_view}")
    print(f"Right-Left View: {right_left_view}")
    print()
    
    # Perfect tree comparison
    perfect_tree = build_perfect_tree()
    
    print("Perfect Tree Structure:")
    print("        1")
    print("       / \\")
    print("      2   3")
    print("     / \\ / \\")
    print("    4  5 6  7")
    print()
    
    perfect_left = TreeViews.left_view(perfect_tree)
    perfect_right = TreeViews.right_view(perfect_tree)
    
    print("Perfect Tree Views:")
    print("-" * 70)
    print(f"Left View:     {perfect_left}")
    print(f"Right View:    {perfect_right}")
    print()
    
    print("Key Insights:")
    print("-" * 70)
    print("Left View always contains the leftmost node at each level")
    print("Right View always contains the rightmost node at each level")
    print("Different trees can have identical left views but different right views")
    print("Right-Left View provides a unique combination of both perspectives")
    print()
    print("Applications:")
    print("-" * 70)
    print("These views are useful for:")
    print("  - Tree visualization and analysis")
    print("  - Algorithmic problems involving tree reconstruction")
    print("  - Finding minimum/maximum values at different depths")
    print("  - Understanding tree structure from different angles")
    print("  - Testing binary tree implementations")
    print()
    print("Complexity:")
    print("-" * 70)
    print("All view algorithms have:")
    print("  Time Complexity: O(n) - must visit every node")
    print("  Space Complexity: O(n) - for storing the views")
    print("  Alternative Space: O(h) - for BFS/DFS recursion")
    print("  Where n = number of nodes, h = height of tree")
    print()
    print("For balanced BST: h = O(log n)")
    print("For skewed tree: h = O(n)")
