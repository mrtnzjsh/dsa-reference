from typing import Any, Optional

class AVLNode:
    def __init__(self, value: Any, height: int = 1, left: Optional[AVLNode] = None, right: Optional[AVLNode] = None) -> None:
        """
        Initialize an AVL tree node.
        
        Args:
            value: The value to store in the node
            height: The height of the node (defaults to 1)
            left: The left child node (defaults to None)
            right: The right child node (defaults to None)
        """
        self.value = value
        self.height = height
        self.left = left
        self.right = right


class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: Any, node: Optional[AVLNode] = None) -> AVLNode:
        """
        Insert a new value into the AVL tree while maintaining balance.
        
        Steps:
        1. If tree is empty, create root node
        2. Otherwise, recursively insert the value in appropriate subtree
        3. Update height of current node after insertion
        4. Get balance factor
        5. Check balance and perform rotations as needed:
           a. Left Left case: rotate right on current node
           b. Left Right case: rotate left on left child, then rotate right
           c. Right Right case: rotate left on current node
           d. Right Left case: rotate right on right child, then rotate left
        6. Return the node (may be root after rotations)
        
        The AVL tree maintains height balance by ensuring the difference
        in heights between left and right subtrees is at most 1 for every node.
        
        Args:
            value: The value to insert
            node: The starting node for the insertion (defaults to root)
        
        Returns:
            AVLNode: The root node of the tree (may change after rotations)
        """
        if self.root is None:
            self.root = AVLNode(value)
            return self.root

        if value < node.value:
            node.left = self.insert(value, node.left)
        else:
            node.right = self.insert(value, node.right)

        # Update height
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.get_balance(node)

        # Left heavy and left value
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        # Right heavy and right value
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        # Left heavy and right value
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right heavy and left value
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node


    def height(self, node: Optional[AVLNode] = None) -> int:
        """
        Get the height of a node in the AVL tree.
        
        Steps:
        1. If node is None, return 0 (empty tree has height 0)
        2. Return the stored height of the node
        
        The height of a node is defined as:
        - 0 for an empty tree
        - 1 + max(height of left child, height of right child) for non-empty nodes
        
        Args:
            node: The node to get the height of (defaults to root)
        
        Returns:
            int: The height of the node, or 0 if the node is None
        """
        if node is None:
            return 0
        return node.height

    def get_balance(self, node: Optional[AVLNode] = None) -> int:
        """
        Calculate the balance factor to determine if the tree needs rebalancing.
        
        Steps:
        1. If node is None, return 0 (empty tree is balanced)
        2. Subtract the height of the right subtree from the height of the left subtree
        3. Return the balance factor
        
        A balance factor of:
        - 0 or negative: Right subtree is taller or balanced
        - Positive: Left subtree is taller
        
        Args:
            node: The root node of the subtree to check
        
        Returns:
            int: The difference between left subtree height and right subtree height
        """
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y: AVLNode) -> AVLNode:
        """
        Perform a right rotation around node y.
        This right rotation transforms the structure to restore balance
        when the left subtree becomes heavier than the right subtree.
        
        Steps:
        1. Save the left child of y as x
        2. Store the right child of x as T2
        3. Make x the new root of this subtree
        4. Move y to be the right child of x
        5. Make T2 the left child of y
        6. Update heights of y and x
        
        Args:
            y: The node to rotate around
            
        Returns:
            AVLNode: The new root of the rotated subtree
        """
        x = y.left
        T2 = x.right

        # rotate
        x.right = y
        y.left = T2

        # update heights
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        return x

    def rotate_left(self, x: AVLNode) -> AVLNode:
        """
        Perform a left rotation around node x.
        This left rotation transforms the structure to restore balance
        when the right subtree becomes heavier than the left subtree.
        
        Steps:
        1. Save the right child of x as y
        2. Store the left child of y as T2
        3. Make y the new root of this subtree
        4. Move x to be the left child of y
        5. Make T2 the right child of x
        6. Update heights of x and y
        
        Args:
            x: The node to rotate around
            
        Returns:
            AVLNode: The new root of the rotated subtree
        """
        y = x.right
        T2 = y.left

        # rotate
        y.left = x
        x.right = T2

        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        return y

    def find_min(self, node: AVLNode) -> AVLNode:
        """
        Find the node with the minimum value in a subtree using
        the leftmost node traversal method.
        
        Steps:
        1. Start from the given node
        2. Keep traversing left until no left child exists
        3. Return the last node reached (smallest value in the subtree)
        
        Args:
            node: The root node of the subtree
        
        Returns:
            AVLNode: The node with the minimum value in the subtree
        """
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def delete(self, value: Any, node: Optional[AVLNode] = None) -> Optional[AVLNode]:
        """
        Delete a value from the AVL tree while maintaining balance and
        updating all necessary heights.
        
        Steps:
        1. Standard BST delete:
           a. If value < node.value, search left subtree
           b. If value > node.value, search right subtree
           c. If value matches node:
              - If 0 children: replace node with None
              - If 1 child: replace node with its child
              - If 2 children: replace with inorder successor (min of right subtree)
        2. Update height of current node
        3. Get balance factor
        4. Perform rotations based on balance and child balance:
           a. Left Left case: rotate right
           b. Left Right case: rotate left on left child, then rotate right
           c. Right Right case: rotate left
           d. Right Left case: rotate right on right child, then rotate left
        5. Return the node
        
        Args:
            value: The value to delete
            node: The starting node for the search (defaults to root)
        
        Returns:
            Optional[AVLNode]: The root node of the tree after deletion, or None
        """
        if node is None:
            return None

        if value < node.value:
            node.left = self.delete(value, node.left)
        elif value > node.value:
            node.right = self.delete(value, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            if node.right is None:
                temp = node.left
                node = None
                return temp

            # Node with two children: Get inorder successor (smallest node in right subtree)
            temp = self.find_min(node.right)

            # Copy the inorder successor's content to this node
            node.value = temp.value

            # Delete the inorder successor
            node.right = self.delete(node.right, temp.value)

        # If tree had only one node, return
        if node is None:
            return None

        # Update height of ancestor node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.get_balance(node)

        # Left heavy and Left value
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)

        # Left heavy and Right value
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right heavy and right value
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)

        # Right heavy and left value
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
