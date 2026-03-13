"""Cycle Detection in Undirected Graphs

A cycle in a graph is a path that starts and ends at the same vertex, without traversing
any edge more than once. In an undirected graph, a cycle is particularly important as it
indicates redundancy and can be used for optimization.

**Key Insight:**
A graph contains a cycle if and only if there exists a back edge during DFS traversal.
Specifically, if we find an edge (u, v) where u is already visited and v is visited
and v is not the parent of u in the DFS tree, then we've found a cycle.

**Graph Theory Background:**
A graph G = (V, E) contains a cycle if and only if there exists a path in E that starts
and ends at the same vertex, without repeating edges.

In an undirected graph, a cycle of length k connects k distinct vertices with k edges,
forming a closed loop. The smallest cycle in an undirected graph is a triangle (3 vertices,
3 edges).

**Mathematical Foundation:**
Let G = (V, E) be an undirected graph.
G contains a cycle if and only if:
∃ a path P = v₀, v₁, ..., vₖ such that:
- v₀ = vₖ (start equals end)
- All vᵢ are distinct for i < k
- All edges (vᵢ, vᵢ₊₁) are in E

**Algorithm Steps (DFS-based):**
1. Start DFS from an arbitrary vertex
2. For each visited vertex, record its parent (the vertex from which it was discovered)
3. When exploring neighbors of current vertex u:
   - If neighbor v is visited and v != parent[u], we found a cycle
   - If neighbor v is not visited, recursively explore from v
4. Continue until all vertices are visited or a cycle is found
5. A graph has a cycle if and only if the DFS process finds at least one back edge

**Example - Cycle Detection:**

Graph with vertices {0, 1, 2, 3} and edges:
- (0, 1)
- (1, 2)
- (2, 0) ← This creates a triangle
- (2, 3)

DFS from vertex 0:
1. Visit 0, parent[0] = -1
2. Visit neighbor 1, parent[1] = 0
3. Visit neighbor 2, parent[2] = 1
4. From 2, check neighbor 0: already visited and 0 != parent[2] (parent[2] = 1)
   → Cycle found: 0 → 1 → 2 → 0

**Example - Acyclic Graph:**

Graph with vertices {0, 1, 2, 3} and edges:
- (0, 1)
- (1, 2)
- (2, 3)

DFS from vertex 0:
1. Visit 0, parent[0] = -1
2. Visit neighbor 1, parent[1] = 0
3. Visit neighbor 2, parent[2] = 1
4. From 2, visit neighbor 3, parent[3] = 2
5. All neighbors checked, no back edges
   → No cycle found

**Time Complexity:**
- O(V + E) where V is the number of vertices and E is the number of edges
- Single DFS traversal of the graph

**Space Complexity:**
- O(V) for visited array and parent array
- O(E) for the adjacency list

**Graph Properties:**
A graph is:
- **Tree** if it's connected, undirected, and acyclic (|E| = |V| - 1)
- **Forest** if it's undirected and acyclic (may be disconnected)
- **Cyclic** if it contains at least one cycle

**Cycle Classification:**
1. **Simple cycles:** No vertex repeated (except start/end)
2. **Complex cycles:** Some vertex repeated
3. **Shortest cycle:** Minimum number of edges in any cycle
4. **Longest cycle:** Maximum number of edges in any cycle
5. **Fundamental cycles:** Cycles formed by adding one edge to a spanning tree

**DFS Tree vs. Original Graph:**
In DFS of an undirected graph:
- **Tree edges:** edges in the DFS tree (spanning forest)
- **Back edges:** edges connecting a vertex to an ancestor (creates cycle)
- **Cross edges:** (not present in undirected graphs)
- **Forward edges:** (not present in undirected graphs)

Only back edges create cycles in undirected graphs.

**Path vs. Cycle:**
A **path** is a sequence of edges where no vertex is repeated.
A **cycle** is a path that starts and ends at the same vertex.
The difference is: a cycle must have the same start and end vertex.

**Trade-offs:**
**vs. BFS-based Cycle Detection:**
- DFS: Easier to find the actual cycle path, recursive
- BFS: Similar complexity, may find different cycles, more iterative

**vs. Union-Find for Cycle Detection:**
- Union-Find: Detects if graph contains a cycle during edge addition
- DFS: Can find the actual cycle path, works on static graphs

**vs. Graph Traversal for All Components:**
- DFS: O(V + E), single traversal
- Multiple traversals: Same complexity, just multiple starting points

**Advantages:**
- Simple and efficient implementation
- Can detect cycles without storing all edge information
- O(V + E) time complexity
- Works for disconnected graphs
- Can find actual cycle paths

**Disadvantages:**
- Only detects cycles, doesn't provide cycle structure details
- Might find different cycles depending on starting vertex
- Not suitable for finding all cycles efficiently

**Applications:**
- Graph validation (ensuring no redundant connections)
- Circuit design (checking for loops)
- Graph compression and optimization
- Conflict detection in games
- Path planning and navigation
- Social network analysis (identifying redundant connections)
- DNA sequence analysis

**Connected vs. Disconnected Graphs:**
For disconnected graphs, run DFS from each unvisited vertex.
A graph is acyclic (a forest) if and only if every connected component is a tree.

**Finding All Cycles:**
The simple DFS approach only finds one cycle. Finding ALL cycles is:
- NP-hard problem in general
- Can be found by checking back edges in DFS, but exponential complexity
- Practical solutions use specific algorithms for small graphs

**Example - Finding Cycle Path:**

Graph: 0 → 1 → 2 → 3 → 4 → 2

DFS from 0:
1. Visit 0, parent = -1
2. Visit 1, parent = 0
3. Visit 2, parent = 1
4. Visit 3, parent = 2
5. Visit 4, parent = 3
6. From 4, neighbor 2: already visited and parent[4] = 3 != 2
   → Found cycle path: 2 → 1 → 0 → 3 → 4 → 2
   → Simplified: 2 → 1 → 0 → 3 → 4 → 2
   → Or: 0 → 1 → 2 → 4 → 3 → 2
   → Any of these forms a cycle

**Implementation Notes:**
- Use parent array to avoid detecting the edge back to the parent as a cycle
- For multiple connected components, iterate through all vertices
- The graph is a tree if it's connected and has no cycles (|E| = |V| - 1)
"""

from typing import List, Tuple, Dict
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
