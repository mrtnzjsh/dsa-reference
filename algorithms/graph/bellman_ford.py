# Bellman-Ford Algorithm

# The Bellman-Ford algorithm computes the shortest paths from a single source vertex to all other vertices in a weighted graph.
# Unlike Dijkstra's algorithm, it can handle graphs with negative edge weights (but no negative cycles)

# **Key Insight:**
# After i iterations of relaxing all edges, we have found the shortest paths using at most i edges.
# With n vertices, the shortest path cannot have more than n-1 edges (otherwise there's a cycle).
# After n-1 iterations, we're guaranteed to have the optimal shortest paths.
# If after n-1 iterations we can still relax an edge, there's a negative cycle.

# **Mathematical Foundation:**
# Let dist[v] represent the shortest distance from source s to vertex v.
# Initialize: dist[s] = 0, dist[others] = infinity.
# Relax edge (u, v): if dist[u] + weight(u,v) < dist[v], then dist[v] = dist[u] + weight(u,v)

# **Algorithm Steps:**
# 1. Initialize distances: dist[s] = 0, dist[others] = infinity
# 2. For i from 1 to n-1:
#    For each edge (u, v) in edges:
#      If dist[u] + weight(u,v) < dist[v]:
#        dist[v] = dist[u] + weight(u,v)
# 3. Check for negative cycles:
#    For each edge (u, v):
#      If dist[u] + weight(u,v) < dist[v]:
#        Negative cycle detected

# **Time Complexity:**
# - O(VE) where V is the number of vertices and E is the number of edges
# - One loop over all edges (n-1 times)

# **Space Complexity:**
# - O(V) for distance array
# - O(E) for storing edge list if edges aren't pre-stored

# **Negative Cycle Detection:**
# If after n-1 iterations, we can still relax an edge (dist[u] + weight(u,v) < dist[v]), then there's a negative cycle.
# To find which vertices are affected, after detecting the cycle, continue relaxing for one more iteration.
# Any vertex whose distance is updated lies on a negative cycle.

from typing import List, Tuple


def bellman_ford(edges: List[Tuple[int, int, int]], num_vertices: int, source: int) -> Tuple[List[int], List[Tuple[int, int]]]:
    """Bellman-Ford algorithm for single-source shortest paths with negative weights.

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
