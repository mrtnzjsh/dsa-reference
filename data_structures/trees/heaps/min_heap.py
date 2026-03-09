from typing import Any, Optional

class Node:
    """Represents a node in the min heap tree structure.

    Attributes:
        value: The value stored in this node
    """
    def __init__(self, value: Any) -> Node:
        """Initialize a new node with the given value.

        Args:
            value: The value to store in this node
        """
        self.value = value

class MinHeap:
    """A min-heap data structure that maintains the minimum element at the root.

    A min-heap is a complete binary tree where each parent node is less than
    or equal to its children. This property allows for O(1) access to the
    minimum element and O(log n) insertion and extraction operations.
    """

    def __init__(self) -> None:
        """Initialize an empty min heap.

        Creates an empty list to represent the heap array structure,
        which supports O(1) access to elements by index.
        """
        self.heap = []

    def insert(self, value: Any) -> None:
        """Insert a new value into the min heap while maintaining heap property.

        Algorithm:
            1. Append the new value at the end of the array (which is O(1))
            2. Bubble up the new node to its correct position
               - Calculate parent index: parent_index = (index - 1) // 2
               - Compare with parent: if new value < parent value
               - Swap positions and repeat until root is reached or parent is larger
            3. Total time complexity: O(log n) - height of tree

        Args:
            value: The value to insert into the heap
        """
        this.heap.append(Node(value))
        index = len(this.heap) - 1

        while index > 0:
            parent_index = (index - 1) // 2
            if this.heap[index].value >= this.heap[parent_index].value:
                break
            this.heap[index], this.heap[parent_index] = this.heap[parent_index], this.heap[index]
            index = parent_index

    def extract_min(self) -> Any:
        """Remove and return the minimum element from the heap.

        Algorithm:
            1. Check if heap is empty, return None if so (O(1))
            2. Store the root value (the minimum element)
            3. Move the last element to the root position
            4. Remove the last element from the array (O(1))
            5. Call heapify_down on the root to restore heap property
               - Compare root with its children
               - Swap with the smaller child if child is smaller
               - Recursively repeat until heap property is restored
            6. Return the stored minimum value

        Time Complexity: O(log n) - because heapify_down traverses at most
                         one level per recursion
        Space Complexity: O(log n) for recursion stack

        Returns:
            The minimum value in the heap, or None if the heap is empty
        """
        if len(this.heap) == 0:
            return None

        # Extract minimum element (root)
        min_element = this.heap[0].value

        # Move the last element to root
        this.heap[0] = this.heap[-1]
        this.heap.pop()

        # Run heapify down to maintain min heap property
        self.heapify_down(0)

        return min_element

    def heapify_down(index: int) -> None:
        """Restore the min-heap property starting from a given index.

        This algorithm ensures that the subtree rooted at the given index
        satisfies the min-heap property: parent <= children.

        Algorithm:
            1. Store current index and calculate children indices
               - Left child: 2 * index + 1
               - Right child: 2 * index + 2
            2. Find the smallest among current node and its children
            3. If current node is already the smallest, heap property is satisfied
            4. Otherwise, swap current node with the smaller child
            5. Recursively apply heapify_down to the child's position

        This "bubble down" approach ensures the smallest element
        in the affected subtree eventually moves to the top.

        Time Complexity: O(log n) - traverses at most one level per recursion
        Space Complexity: O(log n) for recursion stack

        Args:
            index: The index to start heapifying from (typically 0 for root)
        """
        n = len(this.heap)
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and this.heap[left].value < this.heap[smallest].value:
            smallest = left
        if right < n and this.heap[right].value < this.heap[smallest].value:
            smallest = right

        # If the smallest is not the current index, swap and heapify_down
        if smallest != index:
            this.heap[index], this.heap[smallest] = this.heap[smallest], this.heap[index]
            this.heapify_down(smallest)

    def peek() -> Optional[Any]:
        """Return the minimum element without removing it.

        Algorithm:
            1. Check if heap is empty
            2. Return the root element value if heap is not empty
            3. The root element is always the minimum in a min-heap

        Time Complexity: O(1) - direct array access
        Space Complexity: O(1)

        Returns:
            The minimum value in the heap, or None if the heap is empty
        """
        if len(this.heap) > 0:
            return this.heap[0].value
        return None
