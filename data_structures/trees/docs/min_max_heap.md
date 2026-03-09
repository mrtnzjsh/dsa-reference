# Min-Max Heap

A min-max heap is a double-ended priority queue data structure that extends the concept of a binary heap by supporting both minimum and maximum element retrieval in O(1) time. Unlike a standard binary heap that only supports extracting the minimum or maximum, a min-max heap can efficiently retrieve and remove both extremes.

## Why Min-Max Heaps

Standard binary heaps are either a min-heap (supporting minimum extraction) or a max-heap (supporting maximum extraction). Min-max heaps address the limitation by providing both extremes simultaneously while maintaining the O(log n) time complexity for insertions and deletions. This is particularly useful in applications that need to access the best and worst elements frequently.

## Key Properties

### Min-Max Heap Property
A min-max heap is a complete binary tree where nodes at even depths (root at depth 0) are "min nodes" and nodes at odd depths are "max nodes":
- **Min nodes** (at even depths) have smaller values than all their descendants
- **Max nodes** (at odd depths) have larger values than all their descendants
- Each node is either a min node or a max node based on its depth

### Structure
- **Complete binary tree**: No gaps in the binary representation
- **Double-ended**: Can efficiently retrieve both min and max
- **Height**: O(log n) for n elements
- **Memory**: Uses O(n) space

## Operations

### Basic Operations
- **FindMin()**: O(1) - retrieve the minimum element
- **FindMax()**: O(1) - retrieve the maximum element
- **DeleteMin()**: O(log n) - remove and return the minimum element
- **DeleteMax()**: O(log n) - remove and return the maximum element
- **Insert()**: O(log n) - add a new element

### Advanced Operations
- **DeleteElement()**: O(log n) - remove any element
- **FindKth()**: O(log n) - find the k-th smallest or largest element
- **Replace()**: O(log n) - replace an element and return it

## Comparison: Min-Max Heap vs Binary Heap

### Standard Binary Heap

**Min-Heap:**
- Only supports minimum extraction
- Uses min heap property: parent ≤ child
- Simpler structure and implementation
- Commonly used in priority queues

**Max-Heap:**
- Only supports maximum extraction
- Uses max heap property: parent ≥ child
- Simple structure and implementation
- Used when maximum priority is needed

### Min-Max Heap

**Bidirectional:**
- Supports both minimum and maximum extraction
- Uses alternating min/max properties
- More complex structure
- Better for applications needing both extremes

### Performance Characteristics

**Min-Heap:**
- FindMin: O(1)
- Insert: O(log n)
- ExtractMin: O(log n)
- Memory: O(n)
- Simpler implementation

**Max-Heap:**
- FindMax: O(1)
- Insert: O(log n)
- ExtractMax: O(log n)
- Memory: O(n)
- Simple implementation

**Min-Max Heap:**
- FindMin: O(1)
- FindMax: O(1)
- Insert: O(log n)
- DeleteMin: O(log n)
- DeleteMax: O(log n)
- Memory: O(n)
- More complex implementation

## Implementation Differences

### Node Structure

**Min-Heap/Max-Heap:**
```javascript
class Node {
  value: T;
  left: Node | null;
  right: Node | null;
}
```

**Min-Max Heap:**
```javascript
class MinMaxNode {
  value: T;
  left: MinMaxNode | null;
  right: MinMaxNode | null;
  minHeapProperty: boolean; // true for min nodes, false for max nodes
}
```

### Rebalancing Logic

**Min-Heap/Max-Heap:**
1. After insertion, move element up the tree until min/max property is satisfied
2. After deletion, move last element down to restore order
3. Simple bubbling algorithm

**Min-Max Heap:**
1. After insertion, move element up while maintaining min-max property
2. After deletion, move last element down while checking both min and max levels
3. Requires checking both parent and grandparent positions
4. More complex bubbling algorithm

## When to Use Each

### Min-Heap
- When you only need minimum extraction
- Standard priority queue implementations
- Best when implementation complexity needs to be minimized
- Most common use case for binary heaps

### Max-Heap
- When you only need maximum extraction
- When you need to track top elements efficiently
- Useful in scheduling algorithms
- Alternative to sorting for getting top k elements

### Min-Max Heap
- When you need both min and max frequently
- Applications requiring dual-ended priority queues
- Situations where performance for both extremes matters
- When you need to quickly access and remove both best and worst elements

## Common Applications

### Min-Heap Applications
- Priority queues in operating systems
- Dijkstra's shortest path algorithm
- Graph algorithms
- Huffman coding
- Event simulation
- Task scheduling

### Max-Heap Applications
- Finding top k elements
- Selection algorithms
- Task prioritization
- Merge k sorted lists
- Priority scheduling

### Min-Max Heap Applications
- Bounded priority queues (keeping track of both min and max)
- Games (tracking best and worst scores)
- Statistical applications (finding extremes)
- Real-time monitoring systems
- Data analytics (quick access to outliers)

## Trade-offs Summary

| Feature | Min-Heap | Max-Heap | Min-Max Heap |
|---------|----------|----------|--------------|
| Extremes | Only min | Only max | Both min & max |
| Implementation Complexity | Low | Low | High |
| Memory Overhead | O(n) | O(n) | O(n) |
| FindMin/Max | O(1) | O(1) | O(1) each |
| Insert/Delete | O(log n) | O(log n) | O(log n) |
| Use Case Simplicity | High | High | Low |

## Modern Use Cases

### Popular Min-Heap Implementations
- Python's `heapq` module (standard library)
- Java's `PriorityQueue` (min-heap by default)
- C++ `std::priority_queue` (max-heap by default)
- C++ `std::priority_queue` (min-heap with comparator)
- JavaScript `PriorityQueue` (modern browsers)

### Popular Max-Heap Implementations
- Java's `PriorityQueue` with reverse comparator
- C++ `std::priority_queue` (default)
- Python `heapq` with negative values
- Data structures in competitive programming

### Min-Max Heap Implementations
- Less common in standard libraries
- Used in specific research applications
- Custom implementations for game development
- Specialized data structures for analytics

## Implementation Details

### Tree Representation
Min-max heaps can be represented using:
- **Array representation**: Most common, uses index calculations
  - For node at index i:
    - Left child at 2i
    - Right child at 2i + 1
    - Parent at floor(i/2)
  - Min nodes at even indices, max nodes at odd indices
- **Node-based representation**: More flexible but uses more memory
  - Each node stores its type (min or max)
  - Allows for more complex operations

### Index-Based Operations
The array representation provides efficient operations:
- `parent(i) = floor(i/2)`
- `leftChild(i) = 2i`
- `rightChild(i) = 2i + 1`
- `isMinNode(i) = (i % 2 == 0)`
- `isMaxNode(i) = (i % 2 == 1)`

## Algorithm Characteristics

### Insertion Algorithm
1. Add new element at the end of the array
2. Compare with parent:
   - If at min level and greater than parent, swap
   - If at max level and less than parent, swap
3. If swapped, compare with grandparent:
   - If still out of order, swap and continue up
4. Continue until order is restored or reach root

### Deletion Algorithm
1. Remove the root element (min or max)
2. Move last element to the root position
3. Move element down through the tree:
   - At each level, check if it should go further down
   - Compare with appropriate children based on level
   - Swap if necessary
4. Repeat until element finds its correct position

## Complexity Analysis

### Space Complexity
- **O(n)**: All operations use O(1) extra space

### Time Complexity
- **FindMin/FindMax**: O(1)
- **Insert**: O(log n)
- **DeleteMin/DeleteMax**: O(log n)
- **DeleteElement**: O(log n)
- **FindKth**: O(log n)

### Practical Performance
- Min-max heaps have slightly higher constant factors due to complex comparisons
- For applications needing only one extreme, standard heaps are faster
- For dual-ended needs, min-max heaps are optimal

## Historical Context

Min-max heaps were introduced as an evolution of binary heaps to address the limitation of having to choose between min and max priorities. The concept builds on the foundation of binary heaps but adds complexity to handle both ends of the priority spectrum efficiently.

The min-max heap structure demonstrates how simple data structures can be enhanced to support more complex operations while maintaining performance guarantees. This pattern of extending basic structures for specialized applications continues to be important in computer science.

## Future Directions

Modern research on min-max heaps focuses on:
- Concurrent implementations
- Memory-efficient variants
- Parallel processing optimizations
- Integration with other data structures
- Applications in distributed systems

The continued relevance of min-max heaps shows how theoretical data structures continue to find practical applications in modern computing scenarios.