"""Kruskal's Minimum Spanning Tree Algorithm

Kruskal's algorithm is a greedy algorithm for finding a minimum spanning tree (MST) of a connected,
undirected graph. The minimum spanning tree is a subset of the edges that connects all the vertices
without any cycles and with the minimum possible total edge weight.

**Key Insight:**
Kruskal's algorithm builds the MST by iteratively adding the smallest edge that doesn't create a cycle.
It uses a Union-Find data structure to efficiently check if adding an edge would create a cycle.
The algorithm is greedy because it always picks the locally optimal choice (smallest edge) at each step.

**Graph Theory Background:**
A **spanning tree** of a connected, undirected graph G = (V, E) is a subset of edges T ⊆ E such that:
1. T contains all vertices of V (T spans all vertices)
2. T is a tree (acyclic and connected)
3. |T| = |V| - 1

A **minimum spanning tree (MST)** is a spanning tree with the minimum possible sum of edge weights.

**Mathematical Foundation:**
Let G = (V, E) be a connected undirected graph with weighted edges.
Define MST as T ⊆ E such that:
- T spans all vertices in V
- T is a tree
- Sum of weights in T is minimized

**Algorithm Steps:**
1. Sort all edges in non-decreasing order of weight
2. Initialize empty set for MST edges
3. For each edge (u, v, w) in sorted order:
   If u and v are in different sets (not already connected):
     Add edge (u, v) to MST
     Union the sets containing u and v
4. Result is the MST

**Example - MST in a 4-vertex Graph:**

Graph edges with weights:
- (0, 1, 4)
- (0, 2, 2)
- (1, 2, 1)
- (2, 3, 5)
- (1, 3, 3)

Sorted edges by weight: [(1, 2, 1), (0, 2, 2), (1, 3, 3), (0, 1, 4), (2, 3, 5)]

Step 1: Add (1, 2, 1)
- Sets: {0}, {1, 2}, {3}
- MST: [(1, 2, 1)]

Step 2: Add (0, 2, 2)
- Sets: {0, 1, 2}, {3}
- MST: [(1, 2, 1), (0, 2, 2)]

Step 3: Add (1, 3, 3)
- Sets: {0, 1, 2, 3}
- MST: [(1, 2, 1), (0, 2, 2), (1, 3, 3)]

Step 4: Skip (0, 1, 4) - 0 and 1 are already connected

Step 5: Skip (2, 3, 5) - 2 and 3 are already connected

Final MST: [(1, 2, 1), (0, 2, 2), (1, 3, 3)]
Total weight: 1 + 2 + 3 = 6

Alternative MST (same weight): [(0, 2, 2), (1, 2, 1), (1, 3, 3)]

**Time Complexity:**
- Sort edges: O(E log E) or O(E log V) since E ≤ V²
- Union-Find operations: O(E α(V)) where α is the inverse Ackermann function
- Total: O(E log E) = O(E log V)

**Space Complexity:**
- O(V) for the Union-Find structure
- O(E) for storing the sorted edges

**Trade-offs:**
**vs. Prim's Algorithm:**
- Kruskal: O(E log V), edge-centric, requires sorting, good for sparse graphs
- Prim: O(E log V) with binary heap, vertex-centric, good for dense graphs
- Both are optimal, choice depends on graph structure

**vs. Borůvka's Algorithm:**
- Kruskal: Simpler implementation, O(E log V)
- Borůvka: O(E log V) with better constants, parallelizable, handles disconnected components

**Advantages:**
- Simple to implement
- Efficient for sparse graphs
- Handles disconnected graphs (finds minimum spanning forest)
- Works well with Union-Find

**Disadvantages:**
- Requires sorting of all edges
- Not as cache-friendly as Prim's
- Doesn't directly give the actual tree structure

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

An edge is "light" if it is the minimum weight edge crossing some cut.

**Cut Property:**
Let (S, V-S) be any cut (partition of vertices into two sets).
Let e be the minimum weight edge crossing this cut.
Then e is part of some MST.

This is the key property that makes Kruskal's greedy algorithm correct.

**Cycle Property:**
Let C be any cycle in G.
Let e be the maximum weight edge in C.
Then e is not in any MST.

**Applications:**
- Network design and routing (minimum cable length for connecting nodes)
- Approximation algorithms for NP-hard problems (metric TSP)
- Image segmentation and clustering
- DNA sequence alignment
- Design of electrical power grids
"""

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
