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
"""
