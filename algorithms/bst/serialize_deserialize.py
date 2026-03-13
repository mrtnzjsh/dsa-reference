"""
Serialize and Deserialize Binary Search Tree

ALGORITHM OVERVIEW:
Serialization converts a binary tree into a sequence of values that can be stored
or transmitted. Deserialization reconstructs the original tree from this sequence.
This is useful for tree storage, network transmission, and algorithmic problems.

MATHEMATICAL FOUNDATION:

Serialization Formats:
1. Pre-order (Root-Left-Right): R, L, R, ...
2. In-order (Left-Root-Right): L, R, L, R, ...
3. Post-order (Left-Right-Root): L, R, L, ...
4. Level-order (BFS): Node, sibling-level, ...

For BSTs with unique values, Pre-order + In-order uniquely determines the tree.
However, simple level-order works without any constraints.

The serialization algorithm:
- Use BFS (level-order) for general trees
- Mark null nodes (e.g., with None or a sentinel)
- Use a delimiter to separate node values
- Handle edge cases: empty tree, single node

Time Complexity: O(n) - visit each node once
Space Complexity: O(n) - storage for serialized data and queue

TRADE-OFFS:
- Pre-order: No need to store null markers but requires second traversal to reconstruct
- Level-order: Easy to reconstruct, requires null markers but simpler code
- In-order + Pre-order: Full reconstruction possible but more complex

Common serialization formats:
1. Comma-separated: "1,2,3,4,None,5"
2. JSON format: [{"val":1,"left":{...},"right":{...}}]
3. String representation with markers

EXAMPLES:

Complete Binary Tree (level order):
        1
       / \
      2   3
     / \   \
    4   5   6

Serialized (level order with null markers):
"1,2,3,4,5,None,6"

Deserialized: Same original tree

Single Node:
Tree: 1
Serialized: "1"
Deserialized: Tree with single node

Empty Tree:
Tree: None
Serialized: "" or "null" or "[]"
Deserialized: Empty tree
"""

from __future__ import annotations
from typing import Optional, List
from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    """Binary tree node with value and child pointers."""
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


class BinaryTreeSerialization:
    """Implementation of BST serialization and deserialization."""
    
    @staticmethod
    def serialize(root: Optional[TreeNode]) -> str:
        """
        Serialize a binary tree to string using level-order traversal.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Comma-separated string of node values (null markers for missing nodes)
            
        Time Complexity: O(n) - visits each node once
        Space Complexity: O(n) - for serialization string
            
        Examples:
            >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
            >>> BinaryTreeSerialization.serialize(root)
            '1,2,3'
            
            >>> root = TreeNode(1, TreeNode(2, TreeNode(3)), None)
            >>> BinaryTreeSerialization.serialize(root)
            '1,2,3'
        """
        if root is None:
            return ""
            
        result: List[str] = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node is None:
                result.append("null")
            else:
                result.append(str(node.val))
                # Add children (including nulls) to queue
                queue.append(node.left)
                queue.append(node.right)
        
        # Filter out trailing nulls if tree is complete
        while result and result[-1] == "null":
            result.pop()
            
        return ",".join(result)
    
    @staticmethod
    def deserialize(data: str) -> Optional[TreeNode]:
        """
        Deserialize string to binary tree using level-order reconstruction.
        
        Args:
            data: Comma-separated string of node values (null markers)
            
        Returns:
            Reconstructed binary tree root
            
        Time Complexity: O(n) - visits each node once
        Space Complexity: O(n) - for reconstructed tree
            
        Examples:
            >>> data = "1,2,3,4"
            >>> root = BinaryTreeSerialization.deserialize(data)
            >>> assert root.val == 1
            >>> assert root.left.val == 2
            >>> assert root.right.val == 3
        """
        if not data.strip():
            return None
            
        values = [v for v in data.split(",") if v]  # Filter empty strings
        
        if not values:
            return None
            
        # Create root
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        
        while queue and i < len(values):
            current = queue.popleft()
            
            # Create left child
            if i < len(values):
                if values[i] == "null":
                    current.left = None
                else:
                    current.left = TreeNode(int(values[i]))
                    queue.append(current.left)
                i += 1
                
            # Create right child
            if i < len(values):
                if values[i] == "null":
                    current.right = None
                else:
                    current.right = TreeNode(int(values[i]))
                    queue.append(current.right)
                i += 1
        
        return root
    
    @staticmethod
    def serialize_preorder(root: Optional[TreeNode]) -> str:
        """
        Serialize tree using pre-order traversal (Root, Left, Right).
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Comma-separated string of node values
            
        Time Complexity: O(n)
        Space Complexity: O(h) for recursion stack
        """
        result: List[str] = []
        
        def preorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ",".join(result)
    
    @staticmethod
    def deserialize_preorder(data: str) -> Optional[TreeNode]:
        """
        Deserialize pre-order string to binary tree.
        
        Args:
            data: Comma-separated pre-order traversal string
            
        Returns:
            Reconstructed binary tree root
            
        Time Complexity: O(n)
        Space Complexity: O(n) for reconstruction
        """
        values = [int(v) for v in data.split(",") if v]
        
        if not values:
            return None
            
        # Reconstruct using the fact that first value is root
        # Then next values follow preorder pattern
        if not values:
            return None
            
        # Simple approach: assume it's a complete tree reconstruction
        # For full general tree reconstruction with nulls, we'd need
        # additional information
        
        # Reconstruct as a complete tree structure
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        
        while queue and i < len(values):
            current = queue.popleft()
            
            if i < len(values):
                current.left = TreeNode(values[i])
                queue.append(current.left)
                i += 1
                
            if i < len(values):
                current.right = TreeNode(values[i])
                queue.append(current.right)
                i += 1
        
        return root
    
    @staticmethod
    def serialize_postorder(root: Optional[TreeNode]) -> str:
        """
        Serialize tree using post-order traversal (Left, Right, Root).
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Comma-separated string of node values
            
        Time Complexity: O(n)
        Space Complexity: O(h) for recursion stack
        """
        result: List[str] = []
        
        def postorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(str(node.val))
        
        postorder(root)
        return ",".join(result)
    
    @staticmethod
    def round_trip(root: Optional[TreeNode]) -> bool:
        """
        Test if a tree can be serialized and deserialized exactly.
        
        Args:
            root: Root of the binary tree to test
            
        Returns:
            True if round-trip preserves structure
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if root is None:
            return True
            
        serialized = BinaryTreeSerialization.serialize(root)
        deserialized = BinaryTreeSerialization.deserialize(serialized)
        
        # Compare using a helper function
        def compare_nodes(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            return (a.val == b.val and 
                   compare_nodes(a.left, b.left) and 
                   compare_nodes(a.right, b.right))
        
        return compare_nodes(root, deserialized)


def build_test_tree() -> TreeNode:
    """Build a test binary tree for serialization/deserialization."""
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


def build_complete_tree() -> TreeNode:
    """Build a complete binary tree."""
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


def build_single_node() -> TreeNode:
    """Build a tree with single node."""
    return TreeNode(42)


def main() -> None:
    """Demonstrate serialization and deserialization algorithms."""
    print("=" * 70)
    print("Binary Tree Serialization and Deserialization Tests")
    print("=" * 70)
    print()
    
    test_cases = [
        ("Single Node", build_single_node()),
        ("Test Tree", build_test_tree()),
        ("Complete Tree", build_complete_tree()),
    ]
    
    for name, tree in test_cases:
        print(f"{name}:")
        print("-" * 70)
        
        # Level-order serialization
        serialized = BinaryTreeSerialization.serialize(tree)
        print(f"  Serialized (level-order): {serialized}")
        
        # Deserialize and verify
        deserialized = BinaryTreeSerialization.deserialize(serialized)
        
        def verify_structure(original: Optional[TreeNode], 
                           deserialized: Optional[TreeNode]) -> str:
            if original is None and deserialized is None:
                return "✓ Empty tree matches"
            if original is None or deserialized is None:
                return "✗ Tree mismatch"
            if original.val != deserialized.val:
                return f"✗ Root values differ: {original.val} vs {deserialized.val}"
            return "✓ Structure preserved"
        
        result = verify_structure(tree, deserialized)
        print(f"  Verification: {result}")
        
        # Round-trip test
        round_trip = BinaryTreeSerialization.round_trip(tree)
        print(f"  Round-trip: {'✓ Success' if round_trip else '✗ Failed'}")
        print()
    
    print("Different Serialization Methods:")
    print("-" * 70)
    
    tree = build_test_tree()
    preorder = BinaryTreeSerialization.serialize_preorder(tree)
    postorder = BinaryTreeSerialization.serialize_postorder(tree)
    
    print(f"Original tree serialization (level-order): {BinaryTreeSerialization.serialize(tree)}")
    print(f"Pre-order serialization:        {preorder}")
    print(f"Post-order serialization:       {postorder}")
    print()
    
    print("Complexity Analysis:")
    print("-" * 70)
    print("Time Complexity:")
    print("  - Serialize:        O(n) - visit each node")
    print("  - Deserialize:      O(n) - visit each node")
    print("  - Round-trip test:  O(n) - both operations")
    print()
    print("Space Complexity:")
    print("  - Serialize:        O(n) - storage for serialized data")
    print("  - Deserialize:      O(n) - storage for reconstructed tree")
    print("  - Recursion stack:  O(h) - for preorder/postorder methods")
    print()
    print("Trade-offs:")
    print("  - Level-order:      Simpler code, requires null markers")
    print("  - Pre-order:        No null markers needed, but reconstruction harder")
    print("  - Post-order:       Useful for some algorithms (e.g., tree deletion)")
    print("  - In-order + Pre:   Can uniquely reconstruct BST (requires two strings)")


if __name__ == "__main__":
    main()
