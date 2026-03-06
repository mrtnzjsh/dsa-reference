# Linked List

A linked list is a linear data structure consisting of nodes, where each node
contains data and a reference (or link) to the next node in the sequence. Unlike
arrays, linked lists do not require contiguous memory locations, which makes
them flexible in terms of memory allocation and insertion/deletion operations.

## Implementations

- Singly Linked List: Each node has a data field and a next pointer.
- Doubly Linked List: Each node has a data field, a next pointer, and a previous
  pointer.
- Circular Linked List: Similar to a singly linked list, but the last node's
  next pointer points back to the first node.

## Time Complexities

### Single Linked List

- Insertion:
  - At the Beginning: O(1) - Only involves updating the head pointer.
  - At the End: O(n) - Requires traversal from the head to the end of the list.
  - After a Given Node: O(1) - Assuming the given node is known, only involves
    updating pointers.

- Deletion:
  - Delete the First Node: O(1) - Only involves updating the head pointer.
  - Delete the Last Node: O(n) - Requires traversal from the head to the
    second-to-last node.
  - Delete a Given Node: O(n) - Requires traversal to find the node and update
    pointers.

- Traversal: O(n) - Iterates through all nodes in the list.

- Search: O(n) - Searches through all nodes until the desired value is found.

- Reverse: O(n) - Iterates through all nodes to reverse the links.

- Sort: O(n^2) - Common sorting algorithms like bubble sort or insertion sort
  are used.

### Double Linked List

- Insertion:
  - At the Beginning: O(1) - Only involves updating pointers.
  - At the End: O(1) - Only involves updating pointers.
  - After a Given Node: O(1) - Assuming the given node is known, only involves
    updating pointers.

- Deletion:
  - Delete the First Node: O(1) - Only involves updating pointers.
  - Delete the Last Node: O(1) - Only involves updating pointers.
  - Delete a Given Node: O(1) - Assuming the given node is known, only involves
    updating pointers.

- Traversal: O(n) - Iterates through all nodes in the list.

- Search: O(n) - Searches through all nodes until the desired value is found.

- Reverse: O(n) - Iterates through all nodes to reverse the links.

- Sort: O(n^2) - Common sorting algorithms like bubble sort or insertion sort
  are used.

### Circular Linked List

- Insertion:
  - At the Beginning: O(1) - Only involves updating pointers.
  - At the End: O(1) - Only involves updating pointers.
  - After a Given Node: O(1) - Assuming the given node is known, only involves
    updating pointers.

- Deletion:
  - Delete the First Node: O(1) - Only involves updating pointers.
  - Delete the Last Node: O(n) - Requires traversal to find the node before the
    last node.
  - Delete a Given Node: O(n) - Requires traversal to find the node and update
    pointers.

- Traversal: O(n) - Iterates through all nodes in the list.

- Search: O(n) - Searches through all nodes until the desired value is found.

- Reverse: O(n) - Iterates through all nodes to reverse the links.

- Sort: O(n^2) - Common sorting algorithms like bubble sort or insertion sort
  are used.

## Base Operation Explanation

### Single Linked List

- Append:

1. Create the new node from input.
2. Check if the current head of the linked list is `None`. If it is, the request
   is the first node. If it is not, assign the head of the existing list to a
   new variable.
3. Iterate over the list until you reach the last node.
4. Link the new node to the new_variable.

- Prepend

1. Create the new node from input.
2. Set the new node's head to next.
3. set head to new node.

- Delete

1. Save head to new variable
2. if the new variable isn't None and it matches what is to be deleted, set head
   to the new variable's next. Set new variable to none and return.
3. Create new node for `prev` and set to None.
4. Iterate over original new node while it doesn't, set prev_node to original
   new var, then set original new var to its next.
5. If you get to where new variable is None, you have reached the end of the LL
   and not found the value. return.
6. Set `prev`'s next to original new variable's next.
7. Set original new var to none.

## Linked List In Applications

- Memory Allocation: Efficient in managing memory allocation and deallocation.
- Dynamic Data Structures: Suitable for applications where the size of the data
  structure changes frequently.

## Linked List In algorithms

- Implementing Other Data Structures: Used to implement other data structures
  like stacks, queues, and hash tables.
- Polynomial Representation: Useful for representing polynomials where
  coefficients and exponents are stored in nodes.

## Definitions

- Polynomial - a mathematical expression consisting of variables (also called
  indeterminates), coefficients, and exponents, which are combined using only
  addition, subtraction, multiplication, and non-negative integer exponents.
  - e.g. 3x^2 - 5x + 7
