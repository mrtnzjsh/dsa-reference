"""Floyd-Warshall Algorithm

The Floyd-Warshall algorithm computes the shortest paths between all pairs of vertices in a weighted graph.
This all-pairs shortest path algorithm works with both positive and negative edge weights (but no negative cycles).

**Key Insight:**
The algorithm builds a solution incrementally by considering each vertex as an intermediate node.
For any pair of vertices (u, v), the shortest path either:
- Doesn't use vertex k as an intermediate node (already computed)
- Uses vertex k as an intermediate node, so the path is: u → ... → k → ... → v

**Mathematical Foundation:**
Let dist[i][j] represent the shortest distance from vertex i to vertex j.
Initialize: dist[i][j] = weight(i,j) for all edges (i,j), else infinity.
Recurse: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

**Algorithm Steps:**
1. Initialize a distance matrix dist where dist[i][j] contains the weight of edge (i,j)
2. For each vertex k from 0 to n-1 (intermediate vertex):
   For each pair (i, j) where i != j:
     dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
3. The final dist matrix contains all shortest path distances

**Example - Finding Shortest Path in a 4-vertex Graph:**

Graph edges: 
- 0 → 1 (4)
- 1 → 2 (1)
- 0 → 2 (2)
- 2 → 3 (5)
- 1 → 3 (3)

Initial distance matrix:
```
     0   1   2   3
   +---+---+---+---+
0 | 0 | 4 | 2 | ∞ |
   +---+---+---+---+
1 | ∞ | 0 | 1 | 3 |
   +---+---+---+---+
2 | ∞ | ∞ | 0 | 5 |
   +---+---+---+---+
3 | ∞ | ∞ | ∞ | 0 |
   +---+---+---+---+
```

After k=0 (intermediate vertex 0):
```
     0   1   2   3
   +---+---+---+---+
0 | 0 | 4 | 2 | 7 |
   +---+---+---+---+
1 | ∞ | 0 | 1 | 3 |
   +---+---+---+---+
2 | ∞ | ∞ | 0 | 5 |
   +---+---+---+---+
3 | ∞ | ∞ | ∞ | 0 |
   +---+---+---+---+
```
New path: 1 → 0 → 3 = 4 + ∞ = ∞ (no change)

After k=1 (intermediate vertex 1):
```
     0   1   2   3
   +---+---+---+---+
0 | 0 | 4 | 2 | 5 |
   +---+---+---+---+
1 | ∞ | 0 | 1 | 3 |
   +---+---+---+---+
2 | ∞ | ∞ | 0 | 5 |
   +---+---+---+---+
3 | ∞ | ∞ | ∞ | 0 |
   +---+---+---+---+
```
New path: 0 → 1 → 3 = 4 + 3 = 7 (no improvement over 7)
No change to path from 2 to anywhere

After k=2 (intermediate vertex 2):
```
     0   1   2   3
   +---+---+---+---+
0 | 0 | 4 | 2 | 7 |
   +---+---+---+---+
1 | ∞ | 0 | 1 | 4 |
   +---+---+---+---+
2 | ∞ | ∞ | 0 | 5 |
   +---+---+---+---+
3 | ∞ | ∞ | ∞ | 0 |
   +---+---+---+---+
```
New path: 1 → 2 → 3 = 1 + 5 = 6 (no improvement over 3)
No change to path from 0 to 3

After k=3 (intermediate vertex 3):
```
     0   1   2   3
   +---+---+---+---+
0 | 0 | 4 | 2 | 7 |
   +---+---+---+---+
1 | ∞ | 0 | 1 | 4 |
   +---+---+---+---+
2 | ∞ | ∞ | 0 | 5 |
   +---+---+---+---+
3 | ∞ | ∞ | ∞ | 0 |
   +---+---+---+---+
```
No improvement possible

Final shortest paths:
- 0 → 1: 4
- 0 → 2: 2 (direct edge)
- 0 → 3: 7 (0 → 1 → 3)
- 1 → 2: 1
- 1 → 3: 4 (1 → 2 → 3)
- 2 → 3: 5

**Time Complexity:**
- O(n³) where n is the number of vertices
- Three nested loops: O(k) × O(n) × O(n)

**Space Complexity:**
- O(n²) for the distance matrix

**Negative Cycles:**
If dist[i][j] < dist[i][k] + dist[k][j] after the algorithm completes, there exists a negative cycle reachable from i and j. To detect negative cycles, after the algorithm, check if dist[i][j] < 0 for any edge (i,j).

**Trade-offs:**
**vs. Dijkstra's Algorithm:**
- Dijkstra: O(E log V) for single source, doesn't handle negative weights
- Floyd-Warshall: O(V³) for all pairs, handles negative weights, handles negative cycles

**vs. Johnson's Algorithm:**
- Johnson: O(V² log V + VE) for all pairs with positive weights only
- Floyd-Warshall: Simpler implementation, O(V³), handles negative weights

**Advantages:**
- Computes all-pairs shortest paths in one pass
- Handles negative edge weights (but not negative cycles)
- Simple implementation

**Disadvantages:**
- O(V³) complexity - slow for very large graphs
- Only provides shortest paths, not the actual paths (can be modified to track predecessors)
- Space O(V²) - large matrices for sparse graphs
- Not suitable for sparse graphs

**Applications:**
- Finding shortest paths in all pairs in dense graphs
- All-pairs shortest path problems in fixed-size graphs
- Transitive closure computation (graph reachability)
- Network analysis and routing protocols
"""

from typing import List, Tuple

def floyd_warshall(graph: List[List[int]], INF: int = float('inf')) -> Tuple[List[List[int]], List[List[int]]]:
    """
    Floyd-Warshall algorithm for all-pairs shortest paths.
    
    Args:
        graph: Adjacency matrix where graph[i][j] is the weight of edge from i to j.
               0 represents self-loops, and INF for no edge.
        INF: Infinity value for no path
    
    Returns:
        Tuple of (distance_matrix, predecessor_matrix)
        distance_matrix contains shortest distances between all pairs
        predecessor_matrix can be used to reconstruct paths
    
    Example:
        >>> graph = [
        ...     [0, 4, 2, INF],
        ...     [INF, 0, 1, 3],
        ...     [INF, INF, 0, 5],
        ...     [INF, INF, INF, 0]
        ... ]
        >>> dist, pred = floyd_warshall(graph)
        >>> dist
        [[0, 4, 2, 7], [inf, 0, 1, 4], [inf, inf, 0, 5], [inf, inf, inf, 0]]
    """
    n = len(graph)
    
    # Initialize distance matrix
    dist = [row[:] for row in graph]
    
    # Initialize predecessor matrix (for path reconstruction)
    pred = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != INF:
                pred[i][j] = i
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    
    # Check for negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            print(f"Warning: Negative cycle detected from vertex {i}")
    
    return dist, pred


def get_path(pred: List[List[int]], u: int, v: int) -> List[int]:
    """
    Reconstruct the shortest path from u to v using predecessor matrix.
    
    Args:
        pred: Predecessor matrix from Floyd-Warshall
        u: Source vertex
        v: Destination vertex
    
    Returns:
        List of vertices representing the shortest path from u to v
    
    Example:
        >>> dist, pred = floyd_warshall(graph)
        >>> get_path(pred, 0, 3)
        [0, 1, 3]
    """
    path = []
    current = v
    
    while current != -1:
        path.append(current)
        if current == u:
            break
        current = pred[u][current]
    
    if path[-1] != u:
        return []  # No path exists
    
    return path[::-1]  # Reverse to get correct order


if __name__ == "__main__":
    # Example usage
    graph = [
        [0, 4, 2, float('inf')],
        [float('inf'), 0, 1, 3],
        [float('inf'), float('inf'), 0, 5],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    
    dist, pred = floyd_warshall(graph)
    
    print("Shortest distances:")
    for i in range(len(dist)):
        for j in range(len(dist)):
            print(f"  {i} → {j}: {dist[i][j] if dist[i][j] != float('inf') else '∞EOF