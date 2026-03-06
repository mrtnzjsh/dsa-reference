# PriorityStack

A Priority Stack is a stack where each element has an associated priority. When
elements are pushed onto the stack, they are ordered based on their priorities.
Higher-priority elements are processed before lower-priority ones.

## Time Complexity Differences

- Push - O(n) vs O(1) for standard stack, due to having to insert in stack based
  on priority.

## Priority Stack In Algorithms

- A simpler implementation than a min-heap or balanced tree.

### Trade-offs

- Insertion is O(n) vs O(_log_ n) for a min-heap or balanced tree.
