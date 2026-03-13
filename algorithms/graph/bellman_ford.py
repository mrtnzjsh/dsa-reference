"""Bellman-Ford Algorithm

The Bellman-Ford algorithm computes the shortest paths from a single source vertex to all other vertices in a weighted graph.
Unlike Dijkstra's algorithm, it can handle graphs with negative edge weights (but no negative cycles).

**Key Insight:**
After i iterations of relaxing all edges, we have found the shortest paths using at most i edges.
With n vertices, the shortest path cannot have more than n-1 edges (otherwise there's a cycle).
After n-1 iterations, we're guaranteed to have the optimal shortest paths.
If after n-1 iterations we can still relax an edge, there's a negative cycle.

**Mathematical Foundation:**
Let dist[v] represent the shortest distance from source s to vertex v.
Initialize: dist[s] = 0, dist[others] = infinity.
Relax edge (u, v): if dist[u] + weight(u,v) < dist[v], then dist[v] = dist[u] + weight(u,v)

**Algorithm Steps:**
1. Initialize distances: dist[s] = 0, dist[others] = infinity
2. For i from 1 to n-1:
   For each edge (u, v) in edges:
     If dist[u] + weight(u,v) < dist[v]:
       dist[v] = dist[u] + weight(u,v)
3. Check for negative cycles:
   For each edge (u, v):
     If dist[u] + weight(u,v) < dist[v]:
       Negative cycle detected

**Example - Shortest Path in a 4-vertex Graph with Negative Weights:**

Graph edges:
- s → 1 (2)
- s → 2 (4)
- 1 → 2 (-3)
- 2 → 3 (2)

Initial distances: dist[s]=0, dist[1]=∞, dist[2]=∞, dist[3]=∞

After iteration 1 (relax all edges):
- Relax (s,1): dist[1] = 0 + 2 = 2
- Relax (s,2): dist[2] = 0 + 4 = 4
- Relax (1,2): dist[2] = min(4, 2 + (-3)) = -1
- Relax (2,3): dist[3] = min(∞, -1 + 2) = 1

After iteration 2 (relax all edges again):
- Relax (s,1): dist[1] = min(2, 0 + 2) = 2
- Relax (s,2): dist[2] = min(-1, 0 + 4) = -1
- Relax (1,2): dist[2] = min(-1, 2 + (-3)) = -1
- Relax (2,3): dist[3] = min(1, -1 + 2) = 1

After iteration 3 (same as iteration 2 - no change)

Final shortest distances:
- s → s: 0
- s → 1: 2 (s → 1)
- s → 2: -1 (s → 1 → 2)
- s → 3: 1 (s → 1 → 2 → 3)

**Time Complexity:**
- O(VE) where V is the number of vertices and E is the number of edges
- One loop over all edges (n-1 times)

**Space Complexity:**
- O(V) for distance array
- O(E) for storing edge list if edges aren't pre-stored

**Negative Cycle Detection:**
If after n-1 iterations, we can still relax an edge (dist[u] + weight(u,v) < dist[v]), then there's a negative cycle.
To find which vertices are affected, after detecting the cycle, continue relaxing for one more iteration.
Any vertex whose distance is updated lies on a negative cycle.

**Trade-offs:**
**vs. Dijkstra's Algorithm:**
- Dijkstra: O(E log V) for single source, requires non-negative weights
- Bellman-Ford: O(VE) for single source, handles negative weights, detects negative cycles

**vs. Johnson's Algorithm:**
- Johnson: O(VE + V² log V) for all pairs, handles negative weights, more efficient than Floyd-Warshall
- Bellman-Ford: O(VE) for single source, simpler, handles negative weights

**Advantages:**
- Handles negative edge weights (unlike Dijkstra)
- Detects negative cycles
- Simple implementation
- Doesn't require a priority queue

**Disadvantages:**
- O(VE) complexity - slower than Dijkstra for typical sparse graphs
- Single source only (computes all pairs with repetition)
- Not suitable for large sparse graphs

**Applications:**
- Finding shortest paths in graphs with negative weights
- Detecting negative cycles in currency arbitrage problems
- Credit card minimum payments
- Network routing protocols
- Circuit design and optimization

**Comparison with Dijkstra:**

If all edge weights are non-negative:
- Use Dijkstra for O(E log V) performance
- Bellman-Ford is slower at O(VE)

With negative weights:
- Use Bellman-Ford (Dijkstra fails)
- O(VE) vs O(VE log V) for Johnson's algorithm
"""

from typing import List, Tuple


def bellman_ford(edges: List[Tuple[int, int, int]], num_vertices: int, source: int) -> Tuple[List[int], List[Tuple[int, int]]]:
    """
    Bellman-Ford algorithm for single-source shortest paths with negative weights.
    
    Args:
        edges: List of edges where each edge is (u, v, weight)
               represents directed edge from u to v with given weight
        num_vertices: Total number of vertices in the graph
        source: Source vertex (0-indexed)
    
    Returns:
        Tuple of (distance_array, negative_cycles)
        distance_array contains shortest distances from source
        negative_cycles is a list of vertices affected by negative cycles
    
    Example:
        >>> edges = [(0, 1, 2), (0, 2, 4), (1, 2, -3), (2, 3, 2)]
        >>> dist, cycles = bellman_ford(edges, 4, 0)
        >>> dist
        [0, 2, -1, 1]
        >>> cycles
        []
    """
    # Initialize distance array
    dist = [float('inf')] * num_vertices
    dist[source] = 0
    
    # Relax all edges (n-1) times
    for _ in range(num_vertices - 1):
        updated = False
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                updated = True
        if not updated:
            break
    
    # Check for negative cycles
    negative_cycles = []
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            negative_cycles.append(v)
    
    return dist, negative_cycles


if __name__ == "__main__":
    # Example usage
    edges = [(0, 1, 2), (0, 2, 4), (1, 2, -3), (2, 3, 2)]
    num_vertices = 4
    source = 0
    
    dist, cycles = bellman_ford(edges, num_vertices, source)
    
    print("Shortest distances from source 0:")
    for i in range(num_vertices):
        print(f"  Vertex {i}: {dist[i] if dist[i] != float('inf') else '∞'}")
    
    if cycles:
        print(f"\nNegative cycle detected at vertices: {cycles}")
    else:
        print("\nNo negative cycles detected")
