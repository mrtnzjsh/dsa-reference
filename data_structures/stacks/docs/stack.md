# Stack

A stack is a linear data structure that follows the Last In First Out (LIFO)
principle, meaning the last element added to the stack will be the first one to
be removed. Stacks traditionally have either an array or linked list underlying
data structure

## Time Complexities

### Array-Based Stack

- Push: O(1) - Adding an element to the end of the array is generally a
  constant-time operation.
- Pop: O(1) - Removing the last element from the array is also a constant-time
  operation.
- Peek/Top: O(1) - Accessing the last element is a constant-time operation.
- IsEmpty: O(1) - Checking if the array is empty involves checking its length.
- Size: O(1) - Returning the length of the array is a constant-time operation.

### Linked List-Based Stack

- Push: O(1) - Adding a new node at the head of the linked list is a
  constant-time operation.
- Pop: O(1) - Removing the node at the head of the linked list is also a
  constant-time operation.
- Peek/Top: O(1) - Accessing the node at the head is a constant-time operation.
- IsEmpty: O(1) - Checking if the head pointer is null (indicating an empty
  stack) is a constant-time operation.
- Size: O(n) - Counting the number of nodes in the linked list requires
  traversing the entire list, making this operation linear in terms of the
  number of elements.

## Stacks In Applications

- Function Call Management: Manages function calls in programming languages,
  where the return address is stored on the stack.
- Undo Mechanisms: Often used in text editors to implement undo functionality.

## Stacks In Algorithms

- Expression Evaluation: Used in evaluating expressions, especially in
  converting infix to postfix notation and then evaluating the postfix
  expression.
- Backtracking Algorithms: Useful in algorithms like depth-first search (DFS)
  for exploring paths in graphs or mazes.
- Balancing Parentheses: Checks for balanced parentheses in expressions.
