from typing import Any

from dsa_reference.trees.binary_tree_node import BinaryTree, TreeNode
from dsa_reference.stacks.stack import Stack

"""
In-order traversal - Recursive

1. Begin at root
2. If root is not None:
  - Call with root.left
  - Print value
  - Call with root.right
"""

def recursive_in_order_traversal(root: TreeNode, traversal: list[Any]) -> None:
    if root is not None:
        recursive_in_order_traversal(root.left)

        traversal.append(root.value)

        recursive_in_order_traversal(root.right)

"""
Post-order traversal - Recursive

1. Begin at root
2. If root is not None:
  - Call with root.left
  - Call with root.right
  - Print value
"""

def recursive_post_order_traversal(root: TreeNode, traversal: list[Any]) -> None:
    if root is not None:
        recursive_post_order_traversal(root.left)
        recursive_post_order_traversal(root.right)
        traversal.append(root.value)


"""
In-order traversal - Iterative

1. Initiate empty stack
2. Set root to new variable
3. Start while loop with current not being none and stack not being empty
4. Start while loop nested with current not being none as condition
  - put value on stack
  - iterate to the left
5. in outer loop:
  - pop top of stack
  - process node
  - iterate to the right
"""

def iterative_in_order_traversal(root: TreeNode, traversal: list[Any]) -> None:
    if root is None:
        return

    stack = Stack()
    curr = root

    while curr is not None and not stack.is_empty():
        while curr is not None:
            stack.push(curr)
            curr = curr.left

        value = curr.pop()
        traversal.append(value)
        curr = curr.right


"""
Post-order traversal - Iterative

1. 2 empty stacks
2. push root onto stack1
3. while loop on stack1 while not empty:
  - pop from stack1
  - push onto stack2
  - check left node, push onto stack1
  - check right node, push onto stack2
4. while loop on stack2 while not empty:
  - pop from stack2
  - process node
"""

def iterative_post_order_traversal(root: TreeNode, traversal: list[Any]) -> None:
    if root is None:
        return

    stack1, stack2 = Stack(), Stack()
    stack1.push(root)

    while not stack1.is_empty():
        curr = stack1.pop()
        stack2.push(curr)

        if curr.left is not None:
            stack1.push(curr.left)
        if curr.right is not None:
            stack2.push(curr.right)

    while not stack2.is_empty():
        curr = stack2.pop()
        traversal.append(curr)
