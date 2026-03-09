from typing import Any, Optional
from enum import Enum

class Color(Enum):
    RED = "RED"
    BLACK = "BLACK"

class RBNode:
    def __init__(self, value: Any, left: Optional[RBNode] = None, right: Optional[RBNode] = None, parent: Optional[RBNode] = None) -> None:
        self.value = value
        self.color = Color.RED
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self) -> None:
        """
        Initialize an empty Red-Black tree with a null root.
        The tree maintains the Red-Black tree properties through
        color-coded nodes and rotations during insertion.
        """
        self.root = None
    
    def insert(self, value: Any, node: Optional[RBNode] = None) -> RBNode:
        """
        Insert a new value into the Red-Black tree while maintaining
        the Red-Black tree properties.
        
        Steps:
        1. Create a new node with RED color
        2. Find the appropriate position in the tree
        3. Link the new node as a child of its parent
        4. Call fix_insert to restore Red-Black properties
        
        Returns the root node (same as input node if not changed)
        """
        # if self.root is None:
        #     self.root = RBNode(node)
        #     return self.root

        new_node = RBNode(value)
        parent = None
        curr = node

        while curr is not None:
            parent = curr
            if new_node.value < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        new_node.parent = parent

        # If the tree was empty
        if parent is None:
            self.root = new_node
            node = new_node
        # If not empty, insert the new node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(node, new_node)

        return node

    def fix_insert(self, node: RBNode, new_node: RBNode):
        """
        Fix the Red-Black tree properties after insertion using the
        standard Red-Black insertion fix-up algorithm.
        
        Steps:
        1. Check if parent is RED (which would violate the red parent rule)
        2. Case 1: Parent is left child of grandparent and uncle is RED
           - Recolor: Make uncle, parent, and grandparent BLACK, RED
           - Move up: Set new_node to grandparent and repeat
        3. Case 2: Parent is right child of grandparent and uncle is BLACK
           - If new_node is left child: Perform right rotation on parent
           - Set parent BLACK, grandparent RED, left rotation on grandparent
        4. Case 3: Parent is right child of grandparent (mirror of case 2)
           - Similar to case 2 but with left and right swapped
        5. Case 4: Parent is left child of grandparent and uncle is BLACK
           - Similar to case 2 but swapped
        6. Finally, make the root BLACK to ensure all properties are satisfied
        """
        while new_node.parent is not None and new_node.parent.color == Color.RED:
            if new_node.parent == new_node.parent.parent.right:
                uncle = new_node.parent.parent.left
                if uncle is not None and uncle.color == Color.RED:
                    # If Uncle is RED
                    uncle.color = Color.BLACK
                    new_node.parent.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        # Uncle is black and new node is left child
                        new_node = new_node.parent
                        self.rotate_right(node, new_node)
                    # Uncle is black and new node is right child
                    new_node.parent.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    self.rotate_left(node, new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.right
                if uncle is not None and uncle.color == Color.RED:
                    # Uncle is RED
                    uncle.color = Color.BLACK
                    new_node.parent.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        # Uncle is black and new node is right child
                        new_node = new_node.parent
                        self.rotate_left(node, new_node)
                    # Uncle is black and new node is left child
                    new_node.parent.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    self.rotate_right(node, new_node.parent.parent)

        node.color = Color.BLACK

    def rotate_left(self, node: RBNode, x: RBNode):
        """
        Perform a left rotation around node x in the Red-Black tree.
        This rotation changes the tree structure by making y (the right child
        of x) the new root of the subtree, while maintaining the BST property.
        
        Steps:
        1. Save the right child of x as y
        2. Move y's left subtree to be x's right subtree
        3. Link y to x's parent
        4. If x had no parent, make y the root
        5. Otherwise, set the appropriate child pointer in the parent
        6. Make x the left child of y
        7. Link x to y as its parent
        
        This rotation is essential for maintaining Red-Black properties
        during insertion and deletion operations.
        """
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            node = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, node: RBNode, y: RBNode):
        """
        Perform a right rotation around node y in the Red-Black tree.
        This rotation changes the tree structure by making x (the left child
        of y) the new root of the subtree, while maintaining the BST property.
        
        Steps:
        1. Save the left child of y as x
        2. Move x's right subtree to be y's left subtree
        3. Link x to y's parent
        4. If y had no parent, make x the root
        5. Otherwise, set the appropriate child pointer in the parent
        6. Make y the right child of x
        7. Link y to x as its parent
        
        This rotation is the mirror operation of rotate_left and is
        essential for maintaining Red-Black properties during insertion
        and deletion operations.
        """
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def search(self, value: Any, node: Optional[RBNode] = None) -> Optional[RBNode]:
        """
        Search for a value in the Red-Black tree.

        Steps:
        1. Start from the root node
        2. If the target value is equal to the current node's value, return the node
        3. If the target value is less than the current node's value, search left subtree
        4. If the target value is greater than the current node's value, search right subtree
        5. Return the found node or None if not found

        Args:
            value: The value to search for
            node: The starting node for the search (defaults to root)

        Returns:
            The found node or None if the value is not in the tree
        """
        while node is not None and node.value != value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def find_min(node: RBNode) -> RBNode:
        """
        Find the node with the minimum value in a subtree.

        Steps:
        1. Start from the given node
        2. Keep traversing left until you reach a leaf node
        3. Return the last node reached (minimum value in the subtree)

        Args:
            node: The root node of the subtree

        Returns:
            The node with the minimum value in the subtree
        """
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def transplant(self, node: RBNode, u: RBNode, v: RBNode) -> None:
        """
        Replace subtree rooted at u with subtree rooted at v while preserving
        parent-child relationships.

        Steps:
        1. If u is the root, set root to v
        2. Otherwise, link u's parent to v
        3. Set v's parent to u's parent

        This is used in deletion to replace a node with its child/children.
        """
        if u.parent is None:
            node = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def fix_delete(self, node: RBNode, x: RBNode) -> None:
        """
        Fix the Red-Black tree properties after deletion using the
        standard Red-Black deletion fix-up algorithm.

        Steps:
        1. Start while x is not the root and x is BLACK
        2. If x is left child:
           a. Get sibling w
           b. If w is RED: recolor w BLACK, parent RED, rotate left
           c. If w's children are both BLACK: recolor w RED, move up
           d. If w's right child is BLACK: recolor w's left child BLACK, w RED, rotate right, get new w
           e. Recolor: w takes parent's color, parent BLACK, w's right child BLACK, rotate left
        3. If x is right child: similar to left case with left/right swapped
        4. Make x BLACK to complete the fix
        """
        while x is not node and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.rotate_left(node, x.parent)
                    w = x.parent.right
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self.rotate_right(node, w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self.rotate_left(node, x.parent)
                    x = node
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.rotate_right(node, x.parent)
                    w = x.parent.left
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self.rotate_left(node, w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self.rotate_right(node, x.parent)
                    x = node
        x.color = Color.BLACK
                            

    def delete(self, value: Any, node: Optional[RBNode] = None) -> RBNode:
        """
        Delete a value from the Red-Black tree while maintaining Red-Black properties.

        Steps:
        1. Find the node to delete using search
        2. Standard BST delete (node with 0, 1, or 2 children)
        3. If the deleted node had two children, replace with inorder successor
        4. Call fix_delete to restore Red-Black properties if needed
        5. Return the root node

        Args:
            value: The value to delete
            node: The starting node for the search (defaults to root)

        Returns:
            The root node of the tree after deletion
        """
        if node is None:
            node = self.root

        curr_node = self.search(node, value)
        if curr_node is None:
            return node

        # 1 - Standard BST delete
        original_color = curr_node.color
        if curr_node.left is None:
            self.transplant(self, curr_node, curr_node.right)
            x = curr_node.right
        elif curr_node.right is None:
            self.transplant(self, curr_node, curr_node.left)
            x = curr_node.left
        else:
            y = self.find_min(curr_node.right)
            original_color = y.color
            x = y.right
            if y.parent == curr_node:
                x.parent = y
            else:
                self.transplant(self, y, y.right)
                y.right = curr_node.right
                y.right.parent = y

            self.transplant(self, curr_node, y)
            y.left = curr_node.left
            y.left.parent = y
            y.color = curr_node.color

        # 2 - Fix tree
        if original_color == Color.BLACK:
            self.fix_delete(node, x)

        return node
