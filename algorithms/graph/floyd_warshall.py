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
            print("Warning: Negative cycle detected from vertex " + str(i))

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
            val = dist[i][j]
            if val == float('inf'):
                print("  " + str(i) + " -> " + str(j) + ": ∞")
            else:
                print("  " + str(i) + " -> " + str(j) + ": " + str(val))
