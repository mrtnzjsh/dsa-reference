"""Prim's Minimum Spanning Tree Algorithm

Prim's algorithm is a greedy algorithm for finding a minimum spanning tree (MST) of a connected,
undirected graph. It grows a single tree from an arbitrary starting vertex by repeatedly adding
the smallest edge that connects a vertex in the tree to a vertex outside the tree.

**Key Insight:**
Prim's algorithm builds the MST by maintaining a set of vertices included in the tree (called
the "tree set") and a set of vertices not yet included (called the "non-tree set").
At each step, it selects the smallest edge that connects a tree vertex to a non-tree vertex.
This edge is guaranteed to be part of some MST, making the algorithm greedy and correct.

**Graph Theory Background:**
A minimum spanning tree (MST) of a connected, undirected graph G = (V, E) with weighted edges
is a spanning tree T ⊆ E such that:
1. T contains all vertices of V (T spans all vertices)
2. T is a tree (acyclic and connected)
3. Sum of weights in T is minimized

**Mathematical Foundation:**
Let G = (V, E) be a connected undirected graph with weighted edges.
Define MST as T ⊆ E such that:
- T spans all vertices in V
- T is a tree
- Sum of weights in T is minimized

**Algorithm Steps (Using Binary Heap):**
1. Start from any vertex (let's say vertex 0)
2. Initialize an empty set "in_tree" to track vertices in MST
3. Initialize an empty set "non_tree" to track vertices not in MST
4. Initialize distance array with infinity, distance[0] = 0
5. While in_tree doesn't contain all vertices:
   - Select the vertex u in non_tree with minimum distance
   - Add u to in_tree, remove from non_tree
   - For each neighbor v of u:
     If v is not in in_tree and distance[v] > weight(u, v):
       distance[v] = weight(u, v)
       predecessor[v] = u
6. Result is the MST

**Example - MST in a 4-vertex Graph:**

Graph edges with weights:
- (0, 1, 4)
- (0, 2, 2)
- (1, 2, 1)
- (2, 3, 5)
- (1, 3, 3)

Initialize: in_tree = {0}, non_tree = {1, 2, 3}, distance = [0, ∞, ∞, ∞]

Step 1: Find vertex with min distance in non_tree
- Vertex 0 has distance 0 (in tree)

Step 2: Add vertex 0 to tree
- in_tree = {0}, non_tree = {1, 2, 3}
- Update distances from neighbors of 0:
  - distance[1] = min(∞, 4) = 4
  - distance[2] = min(∞, 2) = 2
- distance = [0, 4, 2, ∞]

Step 3: Find vertex with min distance in non_tree
- Vertex 2 has distance 2 (smallest)

Step 4: Add vertex 2 to tree
- in_tree = {0, 2}, non_tree = {1, 3}
- Update distances from neighbors of 2:
  - distance[1] = min(4, 1) = 1 (edge (2,1) is weight 1)
  - distance[3] = min(∞, 5) = 5
- distance = [0, 4, 2, ∞]

Step 5: Find vertex with min distance in non_tree
- Vertex 1 has distance 1 (smallest)

Step 6: Add vertex 1 to tree
- in_tree = {0, 2, 1}, non_tree = {3}
- Update distances from neighbors of 1:
  - distance[3] = min(5, 3) = 3
- distance = [0, 4, 2, 3]

Step 7: Find vertex with min distance in non_tree
- Vertex 3 has distance 3 (only one left)

Step 8: Add vertex 3 to tree
- in_tree = {0, 2, 1, 3}, non_tree = {}
- Update distances from neighbors of 3:
  - distance[1] = min(3, 3) = 3 (no improvement)

Final MST edges (using predecessor array):
- Edge (0, 2) with weight 2
- Edge (2, 1) with weight 1
- Edge (1, 3) with weight 3

Total weight: 2 + 1 + 3 = 6

**Time Complexity (Using Binary Heap):**
- O(E log V) per iteration where E is number of edges and V is number of vertices
- Overall: O(E log V)

**Time Complexity (Using Fibonacci Heap):**
- O(E + V log V)
- More efficient but more complex implementation

**Space Complexity:**
- O(V) for the priority queue
- O(V) for the distance and predecessor arrays

**Trade-offs:**
**vs. Kruskal's Algorithm:**
- Kruskal: O(E log E), edge-centric, good for sparse graphs
- Prim: O(E log V), vertex-centric, better for dense graphs
- Both are optimal and correct

**vs. Borůvka's Algorithm:**
- Prim: Simple implementation, O(E log V)
- Borůvka: More efficient for very large graphs, parallelizable

**vs. Dijkstra's Algorithm:**
- Dijkstra: Shortest path from single source
- Prim: Minimum spanning tree from single source
- Similar implementation approach

**Advantages:**
- Efficient for dense graphs (E ≈ V²)
- Works well with adjacency lists
- Doesn't require sorting of all edges
- Can be easily implemented with priority queues

**Disadvantages:**
- O(E log V) complexity for sparse graphs
- Requires priority queue implementation
- Not as cache-friendly as some alternatives

**Graph Properties:**
If all edge weights are distinct:
- Exactly one unique MST exists

If some edge weights are equal:
- Multiple MSTs may exist

The total weight of any MST in a connected graph with distinct weights is the same.

**Weight Properties:**
Let T be any MST of G.
For any edge e in G:
- If e is in T: e is a light edge crossing some cut
- If e is not in T: e is a heavy edge (not in some MST)

The **Cut Property** is the key to understanding Prim's algorithm:
Let (S, V-S) be any cut (partition of vertices into two sets).
Let e be the minimum weight edge crossing this cut.
Then e is part of some MST.

This property explains why the greedy choice (minimum weight edge to non-tree vertex)
is always safe.

**Applications:**
- Network design and routing (minimum cable length for connecting nodes)
- Approximation algorithms for NP-hard problems (metric TSP)
- Image segmentation and clustering
- DNA sequence alignment
- Design of electrical power grids
"""

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
