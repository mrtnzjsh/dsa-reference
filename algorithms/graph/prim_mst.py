from typing import List, Tuple, Dict
import heapq


def prim_mst(edges: List[Tuple[int, int, int]], num_vertices: int, start_vertex: int = 0) -> Tuple[List[Tuple[int, int, int]], int]:
    """
    Prim's algorithm to find the minimum spanning tree.
    
    Args:
        edges: List of edges where each edge is (u, v, weight)
               represents undirected edge between u and v with given weight
        num_vertices: Total number of vertices in the graph
        start_vertex: Starting vertex (default is 0)
    
    Returns:
        Tuple of (mst_edges, total_weight)
    
    Example:
        >>> edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (2, 3, 5), (1, 3, 3)]
        >>> mst, total = prim_mst(edges, 4)
        >>> total
        6
    """
    # Build adjacency list
    adj = {i: [] for i in range(num_vertices)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Initialize data structures
    in_tree = [False] * num_vertices
    distance = [float('inf')] * num_vertices
    distance[start_vertex] = 0
    predecessor = [-1] * num_vertices
    
    # Priority queue: stores (distance, vertex)
    heap = [(0, start_vertex)]
    
    mst_edges = []
    total_weight = 0
    
    while heap and len(mst_edges) < num_vertices - 1:
        dist, u = heapq.heappop(heap)
        
        if in_tree[u]:
            continue
        
        in_tree[u] = True
        total_weight += dist
        
        if dist != 0:  # Not the start vertex
            mst_edges.append((predecessor[u], u, dist))
        
        for v, w in adj[u]:
            if not in_tree[v] and w < distance[v]:
                distance[v] = w
                predecessor[v] = u
                heapq.heappush(heap, (w, v))
    
    return mst_edges, total_weight


def prim_mst_with_structure(edges: List[Tuple[int, int, int]], num_vertices: int, start_vertex: int = 0):
    """
    Prim's algorithm that also returns the tree structure and total weight.
    
    Args:
        edges: List of edges where each edge is (u, v, weight)
        num_vertices: Total number of vertices in the graph
        start_vertex: Starting vertex (default is 0)
    
    Returns:
        Tuple of (mst_edges, total_weight, tree_structure)
        tree_structure: Adjacency list representation of the MST
    
    Example:
        >>> edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (2, 3, 5), (1, 3, 3)]
        >>> mst, total, tree = prim_mst_with_structure(edges, 4)
        >>> len(mst)
        3
        >>> total
        6
    """
    adj = {i: [] for i in range(num_vertices)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    in_tree = [False] * num_vertices
    distance = [float('inf')] * num_vertices
    distance[start_vertex] = 0
    predecessor = [-1] * num_vertices
    
    heap = [(0, start_vertex)]
    
    mst_edges = []
    total_weight = 0
    tree = {i: [] for i in range(num_vertices)}
    
    while heap and len(mst_edges) < num_vertices - 1:
        dist, u = heapq.heappop(heap)
        
        if in_tree[u]:
            continue
        
        in_tree[u] = True
        total_weight += dist
        
        if dist != 0:
            mst_edges.append((predecessor[u], u, dist))
            tree[predecessor[u]].append(u)
            tree[u].append(predecessor[u])
        
        for v, w in adj[u]:
            if not in_tree[v] and w < distance[v]:
                distance[v] = w
                predecessor[v] = u
                heapq.heappush(heap, (w, v))
    
    return mst_edges, total_weight, tree


if __name__ == "__main__":
    # Example usage
    edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (2, 3, 5), (1, 3, 3)]
    
    print("All edges:", edges)
    
    mst, total = prim_mst(edges, 4)
    
    print("\nMinimum Spanning Tree edges:")
    for u, v, w in mst:
        print(f"  {u} -- {v}: {w}")
    
    print(f"\nTotal MST weight: {total}")
    
    # Show tree structure
    mst, total, tree = prim_mst_with_structure(edges, 4)
    print("\nTree structure:")
    for u in sorted(tree):
        neighbors = sorted(tree[u])
        if neighbors:
            print(f"  {u} -> {neighbors}")
