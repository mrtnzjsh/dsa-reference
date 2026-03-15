
from typing import List, Tuple
from algorithms.graph.union_find import UnionFind


def kruskal(edges: List[Tuple[int, int, int]], num_vertices: int) -> List[Tuple[int, int, int]]:
    """
    Kruskal's algorithm to find the minimum spanning tree.

    Args:
        edges: List of edges where each edge is (u, v, weight)
               represents undirected edge between u and v with given weight
        num_vertices: Total number of vertices in the graph

    Returns:
        List of edges in the minimum spanning tree

    Example:
        >>> edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (2, 3, 5), (1, 3, 3)]
        >>> mst = kruskal(edges, 4)
        >>> total_weight = sum(w for _, _, w in mst)
        >>> total_weight
        6
    """
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])

    # Initialize Union-Find structure
    uf = UnionFind(num_vertices)

    # Build MST
    mst = []
    total_weight = 0

    for u, v, weight in sorted_edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

            # Early termination if we have V-1 edges
            if len(mst) == num_vertices - 1:
                break

    return mst


def kruskal_with_tree_structure(edges: List[Tuple[int, int, int]], num_vertices: int):
    """
    Kruskal's algorithm that also returns the tree structure.

    Args:
        edges: List of edges where each edge is (u, v, weight)
        num_vertices: Total number of vertices in the graph

    Returns:
        Tuple of (mst_edges, total_weight, tree_structure)
        tree_structure: Adjacency list representation of the MST

    Example:
        >>> edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (2, 3, 5), (1, 3, 3)]
        >>> mst, total, tree = kruskal_with_tree_structure(edges, 4)
        >>> len(mst)
        3
        >>> total
        6
    """
    sorted_edges = sorted(edges, key=lambda x: x[2])
    uf = UnionFind(num_vertices)

    mst = []
    total_weight = 0
    tree = {i: [] for i in range(num_vertices)}

    for u, v, weight in sorted_edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            tree[u].append(v)
            tree[v].append(u)

            if len(mst) == num_vertices - 1:
                break

    return mst, total_weight, tree


if __name__ == "__main__":
    # Example usage
    edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (2, 3, 5), (1, 3, 3)]

    print("All edges:", edges)

    mst = kruskal(edges, 4)
    total_weight = sum(w for _, _, w in mst)

    print("\nMinimum Spanning Tree edges:")
    for u, v, w in mst:
        print(f"  {u} -- {v}: {w}")

    print(f"\nTotal MST weight: {total_weight}")

    # Show tree structure
    mst, total_weight, tree = kruskal_with_tree_structure(edges, 4)
    print("\nTree structure:")
    for u in sorted(tree):
        neighbors = sorted(tree[u])
        print(f"  {u} -> {neighbors}")
