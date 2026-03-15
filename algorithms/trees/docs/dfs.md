# Depth-First Search Algorithm

## Overview

This module implements the Depth-First Search (DFS) algorithm for traversing and searching graphs. DFS explores as far as possible along each branch before backtracking, visiting each node exactly once. The module provides both recursive and iterative implementations of DFS, each using different data structures for tracking visited nodes.

## Algorithm Steps

### Recursive DFS Steps
1. Mark the current vertex as visited
2. Process the vertex (e.g., print its value)
3. For each unvisited neighbor: recursively call DFS with the neighbor

### Iterative DFS Steps
1. Create a stack data structure
2. Initialize a visited structure (set or list)
3. Push the starting vertex onto the stack
4. While the stack is not empty:
   - Pop the top vertex from the stack
   - Process the vertex
   - For each unvisited neighbor:
     - Mark neighbor as visited
     - Push neighbor onto the stack

## Input

- `graph`: An adjacency list representation of a graph as a list of lists, where each index represents a vertex and the value at that index is a list of its neighbors
- `vertex`: The starting vertex for the DFS traversal

## Output

The recursive version modifies the visited list in-place
The iterative version prints visited vertices and their values

## Example

```python
>>> graph = [
...     [1, 2],    # Vertex 0 is connected to vertices 1 and 2
...     [0, 3],    # Vertex 1 is connected to vertices 0 and 3
...     [0, 3],    # Vertex 2 is connected to vertices 0 and 3
...     [1, 2]     # Vertex 3 is connected to vertices 1 and 2
... ]
>>> visited = []
>>> dfs_recursive(graph, 0, visited)
0
1
3
2

>>> visited = []
>>> dfs_recursive(graph, 1, visited)
1
0
2
3

>>> visited = [False] * len(graph)
>>> dfs_iterative(graph, 0)
0
1
3
2

>>> visited = [False] * len(graph)
>>> dfs_iterative(graph, 2)
2
3
1
0
```

### Step-by-step example for dfs_recursive(graph, 0, visited)

1. Call dfs_recursive(graph, 0, visited)
2. visited.append(0) → visited = [0]
3. Print graph[0] → 0
4. Iterate neighbors of vertex 0: [1, 2]
5. For neighbor 1: 1 not in visited → recursive call dfs_recursive(graph, 1, visited)
   - visited.append(1) → visited = [0, 1]
   - Print graph[1] → 1
   - Iterate neighbors of vertex 1: [0, 3]
   - For neighbor 0: 0 in visited → skip
   - For neighbor 3: 3 not in visited → recursive call dfs_recursive(graph, 3, visited)
      - visited.append(3) → visited = [0, 1, 3]
      - Print graph[3] → 3
      - Iterate neighbors of vertex 3: [1, 2]
      - For neighbor 1: 1 in visited → skip
      - For neighbor 2: 2 not in visited → recursive call dfs_recursive(graph, 2, visited)
         - visited.append(2) → visited = [0, 1, 3, 2]
         - Print graph[2] → 2
         - Iterate neighbors of vertex 2: [0, 3]
         - For neighbor 0: 0 in visited → skip
         - For neighbor 3: 3 in visited → skip
         - Return from dfs_recursive(graph, 2, visited)
      - Return from dfs_recursive(graph, 3, visited)
   - Return from dfs_recursive(graph, 1, visited)
6. For neighbor 2: 2 not in visited → recursive call dfs_recursive(graph, 2, visited)
   - visited = [0, 1, 3, 2] (already has 2)
   - Skip all neighbors (already visited)
   - Return
7. Return from dfs_recursive(graph, 0, visited)

## Complexity Analysis

### Time Complexity: O(V + E)

- V: Number of vertices in the graph
- E: Number of edges in the graph
- Each vertex is visited exactly once
- Each edge is examined at most twice (once from each endpoint)
- The recursive version has O(V) space complexity due to call stack
- The iterative version has O(V) space complexity due to stack

### Space Complexity: O(V)

- Recursive DFS: O(V) for call stack + O(V) for visited set = O(V)
- Iterative DFS: O(V) for explicit stack + O(V) for visited set = O(V)
- Both use the same amount of memory for tracking visited nodes

## Notes

DFS is an 'unweighted' graph algorithm - it does not consider edge weights.
It explores all edges reachable from the source vertex before backtracking.
For weighted graphs or when shortest paths are needed, use Breadth-First Search (BFS)
or Dijkstra's algorithm. The recursive implementation can cause stack overflow
for very deep graphs (like those with V > 1000), in which case the iterative
implementation is preferred. The choice between set and list for visited tracking
should be based on the graph characteristics and performance requirements.

## Data Structure Considerations

### Using set() for visited tracking
**Pros:**
- O(1) average time complexity for contains operation
- Handles arbitrary integer values (no indexing required)
- No memory overhead for unused indices (sparse graphs)
- Ideal for graphs with non-contiguous vertex values
- Naturally handles duplicate detection

**Cons:**
- Higher memory overhead for hash table structure
- Slightly slower constant factors for simple cases
- Extra import if not already available
- Less intuitive for graph algorithms that need indexed access

**Recommendation:** Use set() for most general-purpose graph algorithms

### Using list[bool] for visited tracking
**Pros:**
- Lower memory overhead (simple boolean array)
- O(1) time complexity for contains operation (direct indexing)
- No hash table overhead
- Better performance for graphs with dense vertex values
- More memory-efficient for large graphs with many vertices

**Cons:**
- Requires O(n) space even for sparse graphs
- Less flexible with non-contiguous vertex values
- Cannot handle duplicate vertex values efficiently

**Recommendation:** Use list[bool] when vertex values are contiguous integers starting from 0, graph is dense (many vertices), memory efficiency is critical, or performance tests show list[bool] is faster
