

from __future__ import annotations
from typing import Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    """Binary tree node with value and child pointers."""
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


class ValidateBST:
    """Implementation of Binary Search Tree validation algorithm."""
    
    @staticmethod
    def is_valid_bst(root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is a valid Binary Search Tree.
        
        Uses range validation approach where each node has valid range
        of values it can have based on its ancestors.
        
        Args:
            root: Root of the binary tree to validate
            
        Returns:
            True if tree is a valid BST, False otherwise
            
        Time Complexity: O(n) - visit each node once
        Space Complexity: O(h) - recursion stack depth
            
        Examples:
            >>> # Valid BST
            >>> root = TreeNode(20, TreeNode(10), TreeNode(30))
            >>> assert ValidateBST.is_valid_bst(root) == True
            
            >>> # Invalid BST - node 30 has left child
            >>> invalid = TreeNode(20, TreeNode(10), TreeNode(30, TreeNode(25)))
            >>> assert ValidateBST.is_valid_bst(invalid) == False
            
            >>> # Empty tree is valid
            >>> assert ValidateBST.is_valid_bst(None) == True
        """
        def validate(node: Optional[TreeNode],
                    min_val: float = float('-inf'),
                    max_val: float = float('inf')) -> bool:
            if node is None:
                return True
                
            # Check if current node violates BST property
            if not (min_val < node.val < max_val):
                return False
                
            # Recursively validate left and right subtrees
            return (validate(node.left, min_val, node.val) and 
                   validate(node.right, node.val, max_val))
        
        return validate(root)
    
    @staticmethod
    def is_valid_bst_iterative(root: Optional[TreeNode]) -> bool:
        """
        Iterative implementation of BST validation using stack.
        
        Args:
            root: Root of the binary tree to validate
            
        Returns:
            True if tree is a valid BST, False otherwise
            
        Time Complexity: O(n)
        Space Complexity: O(h) for the stack
            
        Uses in-order traversal to check if values are strictly increasing.
        """
        if root is None:
            return True
            
        stack: list[tuple[TreeNode, float, float]] = []
        stack.append((root, float('-inf'), float('inf')))
        prev_value = float('-inf')
        
        while stack:
            node, min_val, max_val = stack.pop()
            
            if node is None:
                continue
                
            # Check BST property
            if not (min_val < node.val < max_val):
                return False
                
            # Update previous value
            if node.val <= prev_value:
                return False
            prev_value = node.val
            
            # Push right child first (for correct order)
            if node.right:
                stack.append((node.right, node.val, max_val))
            # Push left child
            if node.left:
                stack.append((node.left, min_val, node.val))
        
        return True
    
    @staticmethod
    def is_valid_bst_with_duplicates(root: Optional[TreeNode]) -> bool:
        """
        Check BST with non-strict inequality (allows duplicates).
        
        Uses >= and <= for checking right subtree nodes.
        
        Args:
            root: Root of the binary tree to validate
            
        Returns:
            True if tree is a valid BST with duplicates allowed
            
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def validate(node: Optional[TreeNode],
                    min_val: int = float('-inf'),
                    max_val: int = float('inf')) -> bool:
            if node is None:
                return True
                
            # Allow duplicates on right subtree
            if not (min_val < node.val <= max_val):
                return False
                
            return (validate(node.left, min_val, node.val) and 
                   validate(node.right, node.val, max_val))
        
        return validate(root)
    
    @staticmethod
    def find_invalid_node(root: Optional[TreeNode]) -> Optional[int]:
        """
        Find the value of first node that violates BST property.
        
        Args:
            root: Root of the binary tree to validate
            
        Returns:
            Value of invalid node or None if valid
        """
        prev_value = float('-inf')
        
        def validate(node: Optional[TreeNode],
                    min_val: float = float('-inf'),
                    max_val: float = float('inf')) -> Optional[int]:
            if node is None:
                return None
                
            if not (min_val < node.val < max_val):
                return node.val
                
            left_error = validate(node.left, min_val, node.val)
            if left_error:
                return left_error
                
            right_error = validate(node.right, node.val, max_val)
            if right_error:
                return right_error
                
            return None
        
        return validate(root)


def build_valid_bst() -> TreeNode:
    """Build a valid BST for testing."""
    #        20
    #       /  \
    #      10   30
    #     / \   / \
    #    5  15 25  35
    #   /\
    #  3  7
    return TreeNode(20,
                  TreeNode(10,
                        TreeNode(5,
                            TreeNode(3),
                            TreeNode(7)),
                        TreeNode(15)),
                  TreeNode(30,
                        TreeNode(25),
                        TreeNode(35)))


def build_invalid_bst_left_violation() -> TreeNode:
    """Build invalid BST with left subtree violation."""
    #        20
    #       /  \
    #      30   35
    #     /
    #    25
    return TreeNode(20,
                  TreeNode(30,
                        TreeNode(25)),
                  TreeNode(35))


def build_invalid_bst_right_violation() -> TreeNode:
    """Build invalid BST with right subtree violation."""
    #        20
    #         \
    #          30
    #           \
    #            35
    return TreeNode(20,
                  None,
                  TreeNode(30,
                        None,
                        TreeNode(35)))


def build_invalid_bst_duplicates() -> TreeNode:
    """Build invalid BST with duplicate values."""
    #        20
    #       /  \
    #      10   30
    #     / \
    #    10  15
    return TreeNode(20,
                  TreeNode(10,
                        TreeNode(10),
                        TreeNode(15)),
                  TreeNode(30))


def build_tree_with_negative_values() -> TreeNode:
    """Build BST with negative numbers (valid)."""
    #        0
    #       /  \
    #      -5   5
    #     /     \
    #    -10    10
    return TreeNode(0,
                  TreeNode(-5,
                        TreeNode(-10)),
                  TreeNode(5,
                        None,
                        TreeNode(10)))


def main() -> None:
    """Demonstrate BST validation with examples."""
    print("=" * 70)
    print("Binary Search Tree Validation Tests")
    print("=" * 70)
    print()
    
    valid_bst = build_valid_bst()
    print("Valid BST Structure:")
    print("        20")
    print("       /  \\")
    print("      10   30")
    print("     / \\   / \\")
    print("    5  15 25  35")
    print("   /\\")
    print("  3  7")
    print()
    
    print("Validation Results:")
    print("-" * 70)
    
    test_cases = [
        (valid_bst, "Valid BST", True),
        (build_invalid_bst_left_violation(), "Invalid: Left subtree violation", False),
        (build_invalid_bst_right_violation(), "Invalid: Right subtree violation", False),
        (build_invalid_bst_duplicates(), "Invalid: Duplicate values", False),
        (build_tree_with_negative_values(), "Valid: Tree with negative values", True),
        (None, "Empty tree", True),
    ]
    
    for tree, description, expected in test_cases:
        is_valid = ValidateBST.is_valid_bst(tree)
        is_valid_iter = ValidateBST.is_valid_bst_iterative(tree)
        status = "✓" if is_valid == expected else "✗"
        print(f"{status} {description}")
        print(f"   Recursive: {is_valid}, Iterative: {is_valid_iter}")
        
        if not is_valid:
            invalid = ValidateBST.find_invalid_node(tree)
            if invalid is not None:
                print(f"   Invalid node value: {invalid}")
    
    print()
    print("Iterative Validation:")
    print("-" * 70)
    
    # Compare implementations
    is_valid_recursive = ValidateBST.is_valid_bst(valid_bst)
    is_valid_iterative = ValidateBST.is_valid_bst_iterative(valid_bst)
    
    print(f"Valid BST - Recursive: {is_valid_recursive}, Iterative: {is_valid_iterative}")
    print(f"Both methods: {'✓ Match' if is_valid_recursive == is_valid_iterative else '✗ Mismatch'}")
    print()
    
    print("Performance Note:")
    print("-" * 70)
    print("Both recursive and iterative implementations have O(n) time complexity")
    print("but different space usage:")
    print("  - Recursive: O(h) space (height of tree)")
    print("  - Iterative: O(h) space (for stack)")
    print("For balanced BST: h = O(log n)")
    print("For skewed tree: h = O(n)")


if __name__ == "__main__":
    main()
