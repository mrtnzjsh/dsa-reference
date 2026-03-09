from typing import Any, Optional

class Node:
    """Represents a node in the max heap tree structure.

    Attributes:
        value: The value stored in this node
    """
    def __init__(self, value: Any) -> None:
        """Initialize a new node with the given value.

        Args:
            value: The value to store in this node
        """
        self.value = value


class MaxHeap:
    """A max-heap data structure that maintains the maximum element at the root.

    A max-heap is a complete binary tree where each parent node is greater than
    or equal to its children. This property allows for O(1) access to the
    maximum element and O(log n) insertion and extraction operations.
    """

    def __init__(self) -> None:
        """Initialize an empty max heap.

        Creates an empty list to represent the heap array structure,
        which supports O(1) access to elements by index.
        """
        self.heap = []

    def insert(self, value: Any) -> None:
        """Insert a new value into the max heap while maintaining heap property.

        Algorithm:
            1. Append the new value at the end of the array (which is O(1))
            2. Bubble up the new node to its correct position
               - Calculate parent index: parent_index = (index - 1) // 2
               - Compare with parent: if new value > parent value
               - Swap positions and repeat until root is reached or parent is smaller
            3. Total time complexity: O(log n) - height of tree

        Args:
            value: The value to insert into the heap
        """
        self.heap.append(Node(value))
        index = len(self.heap) - 1

        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index].value <= self.heap[parent_index].value:
                break
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def extract_max(self) -> Optional[Any]:
        """Remove and return the maximum element from the heap.

        Algorithm:
            1. Check if heap is empty, return None if so (O(1))
            2. Store the root value (the maximum element)
            3. Move the last element to the root position
            4. Remove the last element from the array (O(1))
            5. Call heapify_down on the root to restore heap property
               - Compare root with its children
               - Swap with the larger child if child is larger
               - Recursively repeat until heap property is restored
            6. Return the stored maximum value

        Time Complexity: O(log n) - because heapify_down traverses at most
                         one level per recursion
        Space Complexity: O(log n) for recursion stack

        Returns:
            The maximum value in the heap, or None if the heap is empty
        """
        if len(self.heap) == 0:
            return None

        max_element = self.heap[0].value
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        self.heapify_down(0)
        return max_element

    def heapify_down(index) -> None:
        """Restore the max-heap property starting from a given index.

        This algorithm ensures that the subtree rooted at the given index
        satisfies the max-heap property: parent >= children.

        Algorithm:
            1. Store current index and calculate children indices
               - Left child: 2 * index + 1
               - Right child: 2 * index + 2
            2. Find the largest among current node and its children
            3. If current node is already the largest, heap property is satisfied
            4. Otherwise, swap current node with the larger child
            5. Recursively apply heapify_down to the child's position

        This "bubble down" approach ensures the largest element
        in the affected subtree eventually moves to the top.

        Time Complexity: O(log n) - traverses at most one level per recursion
        Space Complexity: O(log n) for recursion stack

        Args:
            index: The index to start heapifying from (typically 0 for root)
        """
        n = len(self.heap)
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self.heap[left].value > self.heap[largest].value:
            largest = left

        if right < n and self.heap[right].value > self.heap[largest].value:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def peek() -> Optional[Any]:
        """Return the maximum element without removing it.

        Algorithm:
            1. Check if heap is empty
            2. Return the root element value if heap is not empty
            3. The root element is always the maximum in a max-heap

        Time Complexity: O(1) - direct array access
        Space Complexity: O(1)

        Returns:
            The maximum value in the heap, or None if the heap is empty
        """
        if len(self.heap) > 0:
            return self.heap[0].value
        return None
