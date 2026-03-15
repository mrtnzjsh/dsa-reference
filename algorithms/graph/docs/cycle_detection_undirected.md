# Cycle Detection in Undirected Graphs

## Overview

This module implements cycle detection algorithms for undirected graphs using both DFS and BFS traversal methods. The core insight is that a graph contains a cycle if and only if there exists a back edge during the traversal, where an edge connects a vertex to an ancestor that is not its parent.

## Algorithm Steps

### DFS-Based Cycle Detection

1. Build an adjacency list representation of the graph
2. Initialize visited array and parent array
3. Start DFS from each unvisited vertex
4. When exploring neighbors of current vertex u:
   - If neighbor v is not visited, recursively explore from v
   - If neighbor v is visited and v != parent[u], a cycle is found
5. Reconstruct the cycle path when detected
6. Continue until all vertices are visited

### BFS-Based Cycle Detection

1. Build an adjacency list representation of the graph
2. Initialize visited array, parent array, and queue
3. Start BFS from each unvisited vertex
4. When processing vertex u:
   - For each neighbor v:
     - If v is not visited, mark as visited, set parent, enqueue
     - If v is visited and not parent of u, a cycle is detected
5. Reconstruct the cycle path when detected
6. Continue until all vertices are processed

## Input

- `edges`: List of undirected edges, each represented as a tuple (u, v)
- `num_vertices`: Total number of vertices in the graph
- Vertices are typically numbered from 0 to num_vertices - 1

## Output

For both DFS and BFS functions:
- Tuple containing:
  - `has_cycle`: Boolean indicating if a cycle was found
  - `cycle_path`: List of vertices forming the detected cycle (empty if no cycle)

## Example

### Graph with Cycle

```python
edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
num_vertices = 4
has_cycle, cycle = has_cycle_undirected(edges, num_vertices)
```

Output:
```
has_cycle: True
cycle: [0, 1, 2] or [0, 2, 1]
```

### Step-by-Step DFS Execution

Graph: 0 — 1 — 2 — 0 (triangle)

1. Start DFS from vertex 0:
   - Visit 0, parent[0] = -1
2. Visit neighbor 1 from 0:
   - parent[1] = 0
3. Visit neighbor 2 from 1:
   - parent[2] = 1
4. From vertex 2, check neighbor 0:
   - 0 is already visited
   - parent[2] = 1 != 0 → cycle detected
   - Cycle path: [0, 1, 2]

### Acyclic Graph (Tree)

```python
edges = [(0, 1), (1, 2), (2, 3)]
num_vertices = 4
```

Output:
```
has_cycle: False
cycle: []
```

## Complexity Analysis

### Time Complexity: O(V + E)

- DFS/BFS visits each vertex once: O(V)
- Processes each edge twice (undirected graph): O(E)
- Total: O(V + E)

### Space Complexity: O(V + E)

- Visited array: O(V)
- Parent array: O(V)
- Adjacency list: O(E)
- Recursion stack: O(V)

## Notes

**Key Properties:**
- A graph is a tree if it's connected, undirected, and acyclic (|E| = |V| - 1)
- A graph is a forest if it's undirected and acyclic (may be disconnected)
- Only back edges in undirected graphs create cycles
- DFS tree edges and back edges determine cycles

**Cycle Detection Insight:**
- In undirected graphs, edges can only be tree edges (in DFS tree) or back edges
- A back edge (u, v) where v is an ancestor of u creates a cycle
- The edge (u, v) when combined with tree edges from ancestor to u forms a cycle

**Applications:**
- Graph validation and redundancy checking
- Circuit design and loop detection
- Social network analysis
- Path planning algorithms
- Conflict detection systems
- DNA sequence analysis

**Trade-offs:**
- DFS vs BFS: DFS finds cycles with backtracking, BFS provides breadth-first exploration
- Simple cycle detection vs. finding all cycles: Detecting all cycles is NP-hard in general
- Connected vs. disconnected graphs: Handle by iterating through all vertices

**Implementation Considerations:**
- Use parent array to avoid false cycle detection for the edge to parent
- Reconstruct cycle path by following parent pointers from one vertex back to the other
- For disconnected graphs, start DFS/BFS from each unvisited vertex
