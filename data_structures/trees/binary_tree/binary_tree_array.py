from typing import Any, Optional

class BinaryTree:
    """
    An array-based binary tree is a way to represent a binary tree using an array. 
    In this representation, the root of the tree is placed at index 0, and for any node at index i, 
    its left child is at index 2*i + 1 and its right child is at index 2*i + 2.
    """
    def __init__(self, max_size: int = 100) -> None:
        self.tree = [None] * max_size
        self.max_size = max_size


    def insert(self, value: Any) -> None:
        if self.tree[0] is None:
            # If 0-index is none, value is root
            self.tree[0] = value
        else:
            # Find first available position
            while self.tree[index] is not None:
                if value < self.tree[index]:
                    # Move to left child
                    index = 2 * index + 1
                else:
                    # Move to right child
                    index = 2 * index + 2

            # Insert value in available position
            self.tree[index] = value

    def find_min(self, index) -> Optional[Any]:
        """
        Given an index, return the minimum value of the subtree.
        """
        while self.tree[2 * index + 1] is not None:
            index = 2 * index + 1
        return index
        
    def search(self, value: Any) -> Optional[int]:
        index = 0
        while index < self.max_size and self.tree[index] is not None:
            if self.tree[index] == value:
                return True
            elif value < self.tree[index]:
                # Move to left child
                index = 2 * index + 1
            else:
                # Move to right child
                index = 2 * index + 2
        return None

    def delete(self, value: Any) -> None:
        index = self.search(value)
        if index is None:
            return

        # Index is a leaf
        if self.tree[2 * index + 1] is None and if self.tree[2 * index + 2] is None:
            self.tree[index] = None
        # Index has one right child
        elif self.tree[2 * index + 1] is None:
            self.tree[index] = self.tree[2 * index + 2]
            self.tree[2 * index + 2] = None
        # Index has one left child
        elif self.tree[2 * index + 2] is None:
            self.tree[index] = self.tree[2 * index + 1]
            self.tree[2 * index + 1] = None
        # If node has no children
        else:
            # Find in-order successor
            successor_index = self.find_min(index)
            self.tree[index] = self.tree[successor_index]
            self.tree[successor_index] = None
    

