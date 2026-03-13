"""
Prim's Minimum Spanning Tree Algorithm

This module implements Prim's algorithm to find the Minimum Spanning Tree (MST) 
of an undirected weighted graph using a min-heap priority queue. The algorithm 
starts from an arbitrary vertex and grows the MST one edge at a time by always 
adding the minimum weight edge that connects a vertex in the MST to a vertex 
outside the MST.

Algorithm Steps:
1. Initialize a min-heap with all vertices, setting the start vertex's key to 0
2. For each extracted vertex from the heap:
   a. Mark the vertex as being in the MST
   b. For each adjacent vertex not in the MST, update its key if a shorter edge 
      is found and update the parent pointer
   c. If a shorter edge is found, insert the vertex into the heap with the new key
3. Once all vertices are processed, reconstruct the MST edges from parent pointers

Space Complexity: O(V) for the key array, parent array, in_mst array, and heap 
                    containing all V vertices

Time Complexity: O(E log V) where V is the number of vertices and E is the 
                 number of edges, dominated by heap operations
"""

from dsa_reference.data_structures.trees.heaps.min_heap import MinHeap
 
def prim(graph: list[list[int]]) -> list[tuple[int, int]]:
    """
    Find the Minimum Spanning Tree using Prim's algorithm.
    
    Args:
        graph: Adjacency matrix representation where graph[u][v] contains the 
               weight of the edge between vertices u and v, and graph[u][u] 
               should be 0.
               
    Returns:
        List of tuples representing the edges of the MST, where each tuple 
        contains (parent, child) edges.
        
    Raises:
        ValueError: If the graph is empty or the graph has disconnected components.
        
    Visualization Example:
    ----------------------
    Consider this graph:
        0 ----(2)---- 1
        |      | (3)
        |      |
      (6)     | (5)
        |      |
        3 ----(7)---- 2
         (9)
            |
           (8)
            |
           4
    
    Step 1: Initial State
        Key: [0, ∞, ∞, ∞, ∞]
        Parent: [-1, ∞, ∞, ∞, ∞]
        In MST: [True, False, False, False, False]
        Heap: [(0,0), (∞,1), (∞,2), (∞,3), (∞,4)]
    
    Step 2: Extract vertex 0 (key=0), mark as MST
        In MST: [True, False, False, False, False]
        Heap: [(2,1), (∞,2), (∞,3), (∞,4)]
    
    Step 3: Relax edges from vertex 0
        Check vertex 1: graph[0][1]=2 < ∞ → parent[1]=0, key[1]=2, update heap
        Check vertex 3: graph[0][3]=6 < ∞ → parent[3]=0, key[3]=6, update heap
        In MST: [True, False, False, False, False]
        Key: [0, 2, ∞, 6, ∞]
        Parent: [-1, 0, ∞, 0, ∞]
        Heap: [(2,1), (∞,2), (6,3), (∞,4)]
    
    Step 4: Extract vertex 1 (key=2), mark as MST
        In MST: [True, True, False, False, False]
        Heap: [(5,2), (6,3), (∞,4)]
    
    Step 5: Relax edges from vertex 1
        Check vertex 2: graph[1][2]=3 < ∞ → parent[2]=1, key[2]=3, update heap
        Check vertex 3: graph[1][3]=5 < 6 → parent[3]=1, key[3]=5, update heap
        Check vertex 4: graph[1][4]=1 < ∞ → parent[4]=1, key[4]=1, update heap
        In MST: [True, True, False, False, False]
        Key: [0, 2, 3, 5, 1]
        Parent: [-1, 0, 1, 1, 1]
        Heap: [(1,4), (3,2), (5,3)]
    
    Step 6: Extract vertex 4 (key=1), mark as MST
        In MST: [True, True, False, False, True]
        Heap: [(3,2), (5,3)]
        No better edges found
    
    Step 7: Extract vertex 2 (key=3), mark as MST
        In MST: [True, True, True, False, True]
        Heap: [(5,3)]
        Check vertex 3: graph[2][3]=7 > 5, skip
    
    Step 8: Extract vertex 3 (key=5), mark as MST
        In MST: [True, True, True, True, True]
        Heap: []
    
    Step 9: Reconstruct MST edges
        Edges: [(0,1), (0,3), (1,2), (1,4)]
    """
    vertices = len(graph)

    if vertices == 0:
        return []

    key = [float('inf') for _ in range(vertices)]
    parent = [float('inf') for _ in range(vertices)]
    in_mst = [False for _ in range(vertices)]

    key[0] = 0
    parent[0] = -1

    pq = MinHeap()

    for v in range(vertices):
        pq.insert(key[v], v)

    while pq:
        curr_key, u = pq.extract_min()
        in_mst[u] = True

        for neighbor in range(vertices):
            if in_mst[neighbor] == False and graph[u][neighbor] < key[neighbor]:
                parent[neighbor] = u
                key[neighbor] = graph[u][neighbor]

                pq.update_key(neighbor, key[neighbor])

    mst_edges = []
    for i in range(1, vertices):
        mst_edges.append((parent[i], i))

    return mst_edges
