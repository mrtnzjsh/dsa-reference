
from typing import List, Tuple, Dict, Set
from collections import deque


def is_bipartite(edges: List[Tuple[int, int]], num_vertices: int) -> Tuple[bool, Dict[int, int]]:
    """
    Check if a graph is bipartite using BFS-based 2-coloring.

    Args:
        edges: List of edges where each edge is (u, v)
               represents undirected edge between u and v
        num_vertices: Total number of vertices in the graph

    Returns:
        Tuple of (is_bipartite, coloring)
        is_bipartite: True if graph is bipartite, False otherwise
        coloring: Dictionary mapping vertex to its color (0 or 1)

    Example:
        >>> edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
        >>> is_bipartite(edges, 4)
        (True, {0: 0, 1: 1, 2: 0, 3: 1})
    """
    # Build adjacency list
    adj = {i: [] for i in range(num_vertices)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Initialize color array (0 = uncolored, 1 = color 0, -1 = color 1)
    color = [0] * num_vertices

    # Check each connected component
    for start in range(num_vertices):
        if color[start] != 0:
            continue

        # Start BFS from this vertex
        queue = deque([start])
        color[start] = 1

        while queue:
            u = queue.popleft()

            for v in adj[u]:
                if color[v] == 0:
                    # Assign opposite color to neighbor
                    color[v] = -color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    # Conflict found - not bipartite
                    return False, {i: 1 if color[i] > 0 else 0 for i in range(num_vertices)}

    # All vertices colored without conflicts
    # Convert 1/-1 to 0/1 for the result
    final_coloring = {i: 1 if color[i] > 0 else 0 for i in range(num_vertices)}
    return True, final_coloring


def find_odd_cycle(edges: List[Tuple[int, int]], num_vertices: int) -> List[int]:
    """
    Find an odd cycle in a non-bipartite graph.

    Args:
        edges: List of edges where each edge is (u, v)
        num_vertices: Total number of vertices in the graph

    Returns:
        List of vertices forming an odd cycle, or empty list if bipartite

    Example:
        >>> edges = [(0, 1), (1, 2), (2, 0)]  # Triangle
        >>> find_odd_cycle(edges, 3)
        [0, 1, 2]
    """
    adj = {i: [] for i in range(num_vertices)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Check each connected component
    for start in range(num_vertices):
        color = {start: 0}
        parent = {start: -1}
        queue = deque([start])

        while queue:
            u = queue.popleft()

            for v in adj[u]:
                if v not in color:
                    color[v] = -color[u]
                    parent[v] = u
                    queue.append(v)
                elif color[v] == color[u]:
                    # Found odd cycle - reconstruct it
                    cycle = []
                    cur = u
                    while cur != v:
                        cycle.append(cur)
                        cur = parent[cur]
                    cycle.append(v)
                    cycle.append(u)  # Complete the cycle
                    return cycle

    return []  # No odd cycle found (graph is bipartite)


if __name__ == "__main__":
    # Example 1: Bipartite graph
    bipartite_edges = [(0, 1), (0, 3), (1, 2), (2, 3)]
    num_vertices = 4

    is_bip, coloring = is_bipartite(bipartite_edges, num_vertices)

    print("Bipartite edges:", bipartite_edges)
    print("Is bipartite:", is_bip)
    print("Coloring:", coloring)
    print()

    # Example 2: Non-bipartite graph (triangle)
    non_bipartite_edges = [(0, 1), (1, 2), (2, 0)]
    num_vertices = 3

    is_bip, coloring = is_bipartite(non_bipartite_edges, num_vertices)

    print("Non-bipartite edges:", non_bipartite_edges)
    print("Is bipartite:", is_bip)
    print("Coloring:", coloring)

    # Find the odd cycle
    odd_cycle = find_odd_cycle(non_bipartite_edges, num_vertices)
    if odd_cycle:
        print(f"Odd cycle found: {odd_cycle}")
