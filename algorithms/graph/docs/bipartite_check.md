# Bipartite Check Algorithm

## Overview

A graph is bipartite if its vertices can be partitioned into two disjoint sets U and V such that every edge connects a vertex in U to a vertex in V. In other words, the graph has no odd-length cycles.

**Key Insight:** A graph is bipartite if and only if it is 2-colorable, meaning we can assign one of two colors to each vertex such that no edge connects vertices with the same color.

## Algorithm Steps

1. Build adjacency list representation of the graph
2. Initialize color array (0 = uncolored, 1 = color 0, -1 = color 1)
3. For each connected component:
   - Start BFS from an uncolored vertex, assign it color 1
   - For each vertex in the queue:
     - For each neighbor:
       - If neighbor is uncolored, assign opposite color and enqueue
       - If neighbor has same color as current vertex, return False (not bipartite)
4. If BFS completes without conflicts, return True (graph is bipartite)

## Input

- edges: List of edges where each edge is (u, v)
- num_vertices: Total number of vertices in the graph

## Output

- Tuple of (is_bipartite, coloring)
- is_bipartite: True if graph is bipartite, False otherwise
- coloring: Dictionary mapping vertex to its color (0 or 1)

## Example

**Bipartite Graph:** Edges = [(0, 1), (0, 3), (1, 2), (2, 3)], Vertices = 4

**Step-by-Step:**
- Start with vertex 0: color 1
- Neighbors of 0 (1, 3): color -1
- Neighbors of 1 (2): color 1
- Neighbors of 3 (2): neighbor already has color 1, no conflict
- Final coloring: {0: 0, 1: 1, 2: 0, 3: 1}
- Result: True (graph is bipartite)

**Non-Bipartite Graph:** Edges = [(0, 1), (1, 2), (2, 0)], Vertices = 3

**Step-by-Step:**
- Start with vertex 0: color 1
- Neighbors of 0 (1): color -1
- Neighbors of 1 (2): color 1
- Neighbors of 2 (0): neighbor has same color 1, CONFLICT!
- Result: False (graph is not bipartite - contains triangle)

## Complexity Analysis

**Time Complexity:**
- O(V + E) where V is the number of vertices and E is the number of edges
- Single BFS/DFS traversal of the graph

**Space Complexity:**
- O(V) for the color array and visited array
- O(E) for the adjacency list

## Notes

A graph is bipartite if and only if:
1. It has no odd-length cycles
2. It is 2-colorable
3. Its chromatic number is at most 2

The coloring test is the most practical and efficient approach for checking bipartiteness.

### Applications
- Graph coloring problems
- Scheduling problems (assigning tasks to time slots)
- Bipartite matching and assignment problems
- DNA sequence matching
- Circuit design and logic gates
- Conflict detection in games
