from typing import List, Tuple
from collections import deque


def has_cycle_undirected(edges: List[Tuple[int, int]], num_vertices: int) -> Tuple[bool, List[int]]:
    """
    Detect if an undirected graph contains a cycle using DFS.
    
    Args:
        edges: List of edges where each edge is (u, v)
               represents undirected edge between u and v
        num_vertices: Total number of vertices in the graph
    
    Returns:
        Tuple of (has_cycle, cycle_path)
        has_cycle: True if graph contains a cycle, False otherwise
        cycle_path: List of vertices forming a cycle, or empty list if no cycle
    
    Example:
        >>> edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
        >>> has_cycle, cycle = has_cycle_undirected(edges, 4)
        >>> has_cycle
        True
        >>> len(cycle) >= 3
        True
    """
    # Build adjacency list
    adj = {i: [] for i in range(num_vertices)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Arrays to track visited status and parent
    visited = [False] * num_vertices
    parent = [-1] * num_vertices
    cycle_path = []
    
    def dfs(u: int, start_node: int):
        """DFS function to find cycle."""
        nonlocal cycle_path
        visited[u] = True
        parent[u] = start_node
        
        for v in adj[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif parent[u] != v:
                # Found a cycle: v is already visited and not the parent
                # Reconstruct the cycle path
                cycle_path = [v]
                cur = u
                while cur != v:
                    cycle_path.append(cur)
                    cur = parent[cur]
                cycle_path.append(v)  # Complete the cycle
                return True
        
        return False
    
    # Check each connected component
    for start in range(num_vertices):
        if not visited[start]:
            if dfs(start, start):
                return True, cycle_path
    
    return False, cycle_path


def has_cycle_undirected_bfs(edges: List[Tuple[int, int]], num_vertices: int) -> Tuple[bool, List[int]]:
    """
    Detect if an undirected graph contains a cycle using BFS.
    
    Args:
        edges: List of edges where each edge is (u, v)
        num_vertices: Total number of vertices in the graph
    
    Returns:
        Tuple of (has_cycle, cycle_path)
    
    Example:
        >>> edges = [(0, 1), (1, 2), (2, 0)]
        >>> has_cycle, cycle = has_cycle_undirected_bfs(edges, 3)
        >>> has_cycle
        True
    """
    adj = {i: [] for i in range(num_vertices)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * num_vertices
    parent = [-1] * num_vertices
    cycle_path = []
    
    for start in range(num_vertices):
        if visited[start]:
            continue
        
        queue = deque([start])
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v and parent[v] != u:
                    # Found a back edge
                    cycle_path = [v]
                    cur = u
                    while cur != v:
                        cycle_path.append(cur)
                        cur = parent[cur]
                    cycle_path.append(v)
                    return True, cycle_path
    
    return False, cycle_path


if __name__ == "__main__":
    # Example 1: Graph with cycle
    cyclic_edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
    num_vertices = 4
    
    has_cycle, cycle = has_cycle_undirected(cyclic_edges, num_vertices)
    
    print("Cyclic edges:", cyclic_edges)
    print("Has cycle:", has_cycle)
    if has_cycle:
        print(f"Cycle found: {cycle}")
    print()
    
    # Example 2: Acyclic graph (tree)
    acyclic_edges = [(0, 1), (1, 2), (2, 3)]
    num_vertices = 4
    
    has_cycle, cycle = has_cycle_undirected(acyclic_edges, num_vertices)
    
    print("Acyclic edges:", acyclic_edges)
    print("Has cycle:", has_cycle)
    if not has_cycle:
        print("Graph is a tree")
