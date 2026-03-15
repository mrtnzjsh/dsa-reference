# Prim's Minimum Spanning Tree Algorithm

# This module implements Prim's algorithm to find the Minimum Spanning Tree (MST) 
# of an undirected weighted graph using a min-heap priority queue. The algorithm 
# starts from an arbitrary vertex and grows the MST one edge at a time by always 
# adding the minimum weight edge that connects a vertex in the MST to a vertex 
# outside the MST

# Algorithm Steps:
# 1. Initialize a min-heap with all vertices, setting the start vertex's key to 0
# 2. For each extracted vertex from the heap:
#    a. Mark the vertex as being in the MST
#    b. For each adjacent vertex not in the MST, update its key if a shorter edge 
#       is found and update the parent pointer
#    c. If a shorter edge is found, insert the vertex into the heap with the new key
# 3. Once all vertices are processed, reconstruct the MST edges from parent pointers

# Space Complexity: O(V) for the key array, parent array, in_mst array, and heap 
#                   containing all V vertices

# Time Complexity: O(E log V) where V is the number of vertices and E is the 
#                  number of edges, dominated by heap operations

from dsa_reference.data_structures.trees.heaps.min_heap import MinHeap
 
def prim(graph: list[list[int]]) -> list[tuple[int, int]]:
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
