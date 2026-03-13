"""Bipartite Graph Checking

A graph is bipartite if its vertices can be partitioned into two disjoint sets U and V such that
every edge connects a vertex in U to a vertex in V. In other words, the graph has no odd-length cycles.

**Key Insight:**
A graph is bipartite if and only if it is 2-colorable, meaning we can assign one of two colors
to each vertex such that no edge connects vertices with the same color.

**Graph Theory Background:**
A graph G = (V, E) is bipartite if its vertices can be partitioned into two sets V1 and V2 such that:
- Every vertex in V1 is adjacent only to vertices in V2 (and vice versa)
- No edge exists within V1 or within V2

Equivalently, a graph is bipartite if and only if it contains no odd-length cycles.

**Mathematical Foundation:**
Let G = (V, E) be a graph.
G is bipartite if there exists a coloring function f: V → {0, 1} such that:
- For every edge (u, v) in E, f(u) ≠ f(v)

If such a function exists, the sets are:
- V0 = {v ∈ V | f(v) = 0}
- V1 = {v ∈ V | f(v) = 1}

**Algorithm Steps (BFS-based):**
1. Start with any vertex, assign it color 0
2. Use BFS/DFS traversal from that vertex
3. For each visited vertex v:
   - Assign the opposite color to its neighbors
   - If a neighbor already has the same color as v, the graph is NOT bipartite
4. If BFS/DFS completes without conflicts, the graph IS bipartite

**Example - Bipartite Graph:**

Graph with vertices {0, 1, 2, 3} and edges:
- (0, 1)
- (0, 3)
- (1, 2)
- (2, 3)

Coloring:
- Start with vertex 0: color 0
- Neighbors of 0 (1, 3): color 1
- Neighbors of 1 (0, 2): color 2 gets color 0
- Neighbors of 3 (0, 2): 2 already has color 0, no conflict

Final coloring: 0→0, 1→1, 2→0, 3→1
This is a valid 2-coloring.

**Example - Non-Bipartite Graph:**

Graph with vertices {0, 1, 2} and edges:
- (0, 1)
- (1, 2)
- (2, 0)

Coloring attempt:
- Start with vertex 0: color 0
- Neighbors of 0 (1): color 1
- Neighbors of 1 (2): color 0
- Neighbors of 2 (0): 0 already has color 0, CONFLICT!
- Graph is NOT bipartite (contains triangle cycle)

**Time Complexity:**
- O(V + E) where V is the number of vertices and E is the number of edges
- Single BFS/DFS traversal of the graph

**Space Complexity:**
- O(V) for the color array and visited array
- O(E) for the adjacency list

**Graph Properties:**
A graph is bipartite if and only if:
1. It has no odd-length cycles
2. It is 2-colorable
3. It is a chordal bipartite graph (special case)
4. Its chromatic number is at most 2

The **Three-cycle theorem**: A graph with n vertices is bipartite if and only if it has no cycles of odd length.

**Bipartiteness Tests:**
1. **Coloring test:** Attempt to 2-color the graph
2. **Odd cycle test:** Look for any cycle of odd length
3. **Bipartite matching test:** Use max matching algorithms
4. **Eigenvalue test:** Check spectral properties (advanced)

The coloring test is the most practical and efficient approach.

**Trade-offs:**
**vs. DFS-based Bipartite Check:**
- BFS: Better for finding connected components, more intuitive implementation
- DFS: Simpler code, but BFS is equally efficient

**vs. Bipartite Matching:**
- Bipartite matching: Can find maximum matching, more information
- Simple bipartite check: Faster, simpler, sufficient for bipartiteness test

**vs. Graph Partitioning:**
- Bipartite check: Binary partition only
- Graph partitioning: Can partition into k sets

**Advantages:**
- Simple and efficient implementation
- Detects non-bipartite graphs (conflicts)
- O(V + E) time complexity
- Works for disconnected graphs

**Disadvantages:**
- Only tests bipartiteness, not for more general partitions
- Doesn't provide the partition sets (can be modified)
- Not suitable for finding maximum bipartite matching

**Applications:**
- Graph coloring problems
- Scheduling problems (assigning tasks to time slots)
- Bipartite matching and assignment problems
- Odd cycle detection in graphs
- Social network analysis (community detection)
- DNA sequence matching
- Circuit design and logic gates
- Conflict detection in games (chess queens, knights)
"""

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
                    return False, color
    
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
