from typing import Any, Optional

class TreeNode:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
    A node-based binary tree uses objects or records to represent nodes, 
    where each node contains its value and pointers to its left and right children.
    """
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: Any, root: Optional[TreeNode] = None) -> TreeNode:
        if self.root is None:
            self.root = TreeNode(value)
            return self.root

        if root is None:
            return TreeNode(value)
        if value < root.value:
            root.left = self.insert(value, root.left)
        else:
            root.right = self.insert(value, root.right)

        return root

    def search(self, value: Any, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None and self.root is None:
            return None

        if root is None:
            root = self.root

        if root.value = value:
            return root
        elif root.value < value:
            return self.search(value, root.left)
        else:
            return self.search(value, root.right)

    def find_min(self, value: Any, root: TreeNode) -> TreeNode:
        while root.left is not None:
            root = root.left
        return root

    def delete(self, value: Any, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            root = self.root
        
        if value < root.value:
            self.delete(value, root.left)
        elif value > root.value:
            self.delete(value, root.right)
        else:
            # Node is <= 1 child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Get in-order successor (smallest node in right subtree)
            successor = self.find_min(root.right)
            root.value = successor.value
            root.right = self.delete(successor.value, root.right)

        return root


