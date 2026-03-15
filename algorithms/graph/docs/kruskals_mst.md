# Kruskal's Minimum Spanning Tree Algorithm

## Overview

This module implements Kruskal's algorithm for finding the minimum spanning tree (MST) of a connected, undirected graph. Kruskal's algorithm builds the MST by iteratively adding the smallest edge that doesn't create a cycle, using a Union-Find data structure to efficiently check for cycles.

## Algorithm Steps

1. Sort all edges in non-decreasing order of weight
2. Initialize empty set for MST edges
3. For each edge (u, v, w) in sorted order:
   - If u and v are in different sets (not already connected):
     - Add edge (u, v) to MST
     - Union the sets containing u and v
4. When all vertices are connected (V-1 edges), result is the MST

## Input

- `edges`: List of edges where each edge is (u, v, weight) representing undirected edge between u and v with given weight
- `num_vertices`: Total number of vertices in the graph

## Output

Returns a list of edges in the minimum spanning tree

## Example

```python
>>> edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (2, 3, 5), (1, 3, 3)]
>>> mst = kruskal(edges, 4)
>>> total_weight = sum(w for _, _, w in mst)
>>> total_weight
6
>>> mst
[(1, 2, 1), (0, 2, 2), (1, 3, 3)]
```

### Step-by-step example for kruskal(edges, 4):

Graph edges with weights: (0, 1, 4), (0, 2, 2), (1, 2, 1), (2, 3, 5), (1, 3, 3)

Sorted edges by weight: [(1, 2, 1), (0, 2, 2), (1, 3, 3), (0, 1, 4), (2, 3, 5)]

Step 1: Add (1, 2, 1)
- Sets: {0}, {1, 2}, {3}
- MST: [(1, 2, 1)]

Step 2: Add (0, 2, 2)
- Sets: {0, 1, 2}, {3}
- MST: [(1, 2, 1), (0, 2, 2)]

Step 3: Add (1, 3, 3)
- Sets: {0, 1, 2, 3}
- MST: [(1, 2, 1), (0, 2, 2), (1, 3, 3)]

Step 4: Skip (0, 1, 4) - 0 and 1 are already connected

Step 5: Skip (2, 3, 5) - 2 and 3 are already connected

Final MST: [(1, 2, 1), (0, 2, 2), (1, 3, 3)]
Total weight: 1 + 2 + 3 = 6

Alternative MST (same weight): [(0, 2, 2), (1, 2, 1), (1, 3, 3)]

## Complexity Analysis

### Time Complexity: O(E log E) or O(E log V)

- Sorting edges: O(E log E) or O(E log V) since E ≤ V²
- Union-Find operations: O(E α(V)) where α is the inverse Ackermann function
- Overall: O(E log E) = O(E log V)

### Space Complexity: O(V + E)

- O(V) for the Union-Find structure
- O(E) for storing the sorted edges

## Notes

Kruskal's algorithm is particularly useful for sparse graphs and networks where:
- The graph is connected but might have many potential connections
- You need to find a minimum-cost way to connect all nodes
- Edge weights represent costs like distance, time, or resource consumption

The algorithm guarantees finding a minimum spanning tree for any connected, undirected graph with non-negative edge weights. If the graph is disconnected, it will find a minimum spanning forest instead, which is the best possible solution for disconnected graphs.
