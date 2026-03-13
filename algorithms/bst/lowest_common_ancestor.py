"""
Lowest Common Ancestor (LCA) in Binary Search Tree

ALGORITHM OVERVIEW:
The Lowest Common Ancestor of two nodes in a BST is the deepest node that is an
ancestor of both nodes. Unlike generic binary trees, BSTs have the property that
all nodes in the left subtree of a node have values less than the node's value,
and all nodes in the right subtree have values greater than the node's value.

MATHEMATICAL FOUNDATION:
For nodes p and q:
- If both p and q are in the left subtree of node x, LCA is in left subtree
- If both p and q are in the right subtree of node x, LCA is in right subtree
- If one is in left and one in right, then node x is the LCA

The LCA can be found in O(log n) time for a balanced BST in the worst case.

TIME COMPLEXITY: O(h) where h is the height of the tree
- Average case: O(log n) for balanced BST
- Worst case: O(n) for skewed tree
SPACE COMPLEXITY: O(1) additional space (no recursion stack if iterative)

TRADE-OFFS:
- BST LCA: Fast due to BST property, only requires single traversal
- Generic tree LCA: O(n) time in worst case for unbalanced trees, can use
  LCA with parent pointers (O(h) time) or RMQ algorithms (O(n) preprocessing)

EXAMPLE:
Tree structure:
        20
       /  \
      10   30
     / \     \
    5  15   25  35
   /\     /
  3  7  22

Finding LCA(15, 25):
- Start at root (20)
- 15 is in left subtree, 25 is in right subtree
- LCA is 20

Finding LCA(5, 15):
- Start at root (20)
- Both 5 and 15 are in left subtree
- Move to node (10)
- Both are in left subtree
- Move to node (5)
- Found: LCA(5, 15) = 5
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


class LowestCommonAncestor:
    """Implementation of LCA algorithm for Binary Search Trees."""
    
    @staticmethod
    def find_lca(root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
        """
        Find the Lowest Common Ancestor of nodes with values p and q in a BST.
        
        Args:
            root: Root of the BST
            p: Value of first node
            q: Value of second node
            
        Returns:
            The LCA node or None if not found
            
        Time Complexity: O(h) where h is tree height
        Space Complexity: O(1) if iterative, O(h) if recursive
            
        Examples:
            >>> # Create tree: 20(10,30), 10(5,15), 30(25,35)
            >>> root = TreeNode(20, TreeNode(10, TreeNode(5), TreeNode(15)), TreeNode(30, TreeNode(25), TreeNode(35)))
            >>> # Find LCA(15, 25) -> should be 20
            >>> lca = LowestCommonAncestor.find_lca(root, 15, 25)
            >>> assert lca.val == 20
            >>> # Find LCA(5, 15) -> should be 10
            lca = LowestCommonAncestor.find_lca(root, 5, 15)
            >>> assert lca.val == 10
            >>> # Find LCA(22, 7) -> should be 20
            lca = LowestCommonAncestor.find_lca(root, 22, 7)
            >>> assert lca.val == 20
        """
        if root is None:
            return None
            
        current = root
        while current is not None:
            # Both nodes are in right subtree
            if current.val < p and current.val < q:
                current = current.right
            # Both nodes are in left subtree
            elif current.val > p and current.val > q:
                current = current.left
            # Current node is LCA
            else:
                return current
                
        return current
    
    @staticmethod
    def find_lca_recursive(root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
        """
        Recursive implementation of LCA algorithm.
        
        Args:
            root: Root of the BST
            p: Value of first node
            q: Value of second node
            
        Returns:
            The LCA node or None if not found
            
        Time Complexity: O(h)
        Space Complexity: O(h) for recursion stack
        """
        if root is None or root.val == p or root.val == q:
            return root
            
        if root.val > p and root.val > q:
            return LowestCommonAncestor.find_lca_recursive(root.left, p, q)
        if root.val < p and root.val < q:
            return LowestCommonAncestor.find_lca_recursive(root.right, p, q)
            
        return root


def find_lca_bst(root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
    """
    Iterative function to find LCA of two nodes in BST.
    
    Args:
        root: Root of BST
        p: Value of first node
        q: Value of second node
        
    Returns:
        LCA node or None
        
    Edge Cases:
        - p or q not in tree: returns None
        - p equals q: returns p or q (itself)
        - Duplicate values: first occurrence is considered
    """
    node = root
    while node is not None:
        if node.val < p and node.val < q:
            node = node.right
        elif node.val > p and node.val > q:
            node = node.left
        else:
            return node
    return None


def find_lca_generic(root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
    """
    LCA for generic binary tree (not using BST property).
    
    This is O(n) time complexity and uses the path storage approach.
    """
    def find_path(node: Optional[TreeNode], target: int, path: list[TreeNode]) -> bool:
        if node is None:
            return False
            
        path.append(node)
        if node.val == target:
            return True
            
        if (node.left and find_path(node.left, target, path)) or \
           (node.right and find_path(node.right, target, path)):
            return True
            
        path.pop()
        return False
    
    if not root:
        return None
        
    path_p: list[TreeNode] = []
    path_q: list[TreeNode] = []
    
    if not find_path(root, p, path_p) or not find_path(root, q, path_q):
        return None
        
    # Find the first mismatching node
    lca_index = 0
    min_length = min(len(path_p), len(path_q))
    while lca_index < min_length and path_p[lca_index] == path_q[lca_index]:
        lca_index += 1
        
    return path_p[lca_index - 1] if lca_index > 0 else None


def build_example_tree() -> TreeNode:
    """Build example BST for testing."""
    #        20
    #       /  \
    #      10   30
    #     / \     \
    #    5  15   25  35
    #   /\     /
    #  3  7  22
    root = TreeNode(20,
                  TreeNode(10,
                        TreeNode(5,
                            TreeNode(3),
                            TreeNode(7)),
                        TreeNode(15)),
                  TreeNode(30,
                        TreeNode(25,
                            TreeNode(22)),
                        TreeNode(35)))
    return root


def main() -> None:
    """Demonstrate LCA algorithm with examples."""
    root = build_example_tree()
    
    print("BST Structure:")
    print("        20")
    print("       /  \\")
    print("      10   30")
    print("     / \\     \\")
    print("    5  15   25  35")
    print("   /\\     /")
    print("  3  7  22")
    print()
    
    test_cases = [
        (15, 25, 20, "Both nodes in different subtrees of root"),
        (5, 15, 10, "Both nodes in same left subtree of root"),
        (22, 7, 20, "Nodes from different branches"),
        (3, 35, 20, "Nodes at extreme edges"),
        (25, 25, 25, "Same node (should return itself)"),
    ]
    
    print("LCA Test Cases:")
    print("-" * 60)
    for p, q, expected, description in test_cases:
        lca = find_lca_bst(root, p, q)
        status = "✓" if lca and lca.val == expected else "✗"
        print(f"{status} LCA({p}, {q}): {lca.val if lca else 'None'}")
        print(f"   Expected: {expected} - {description}")
    print()
    
    print("Recursive LCA Results:")
    print("-" * 60)
    for p, q, expected, _ in test_cases:
        lca = LowestCommonAncestor.find_lca_recursive(root, p, q)
        status = "✓" if lca and lca.val == expected else "✗"
        print(f"{status} Recursive LCA({p}, {q}): {lca.val if lca else 'None'}")
    print()
    
    # Demonstrate with generic tree (not BST property)
    print("Generic Tree LCA (using path method):")
    print("-" * 60)
    # Create a non-BST tree
    non_bst_root = TreeNode(20,
                          TreeNode(30, TreeNode(10, None, TreeNode(15)),
                                TreeNode(25)),
                          TreeNode(40,
                                TreeNode(35),
                                TreeNode(50)))
    lca_gen = find_lca_generic(non_bst_root, 15, 25)
    print(f"LCA(15, 25) in generic tree: {lca_gen.val if lca_gen else 'None'}")
    print(f"   Note: In BST this would use O(log n), but generic tree needs O(n)")


if __name__ == "__main__":
    main()
