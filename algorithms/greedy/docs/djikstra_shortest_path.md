"""Dijkstra's Shortest Path Algorithm Implementation

This module implements Dijkstra's algorithm to find the shortest paths from a source node
to all other nodes in a weighted graph using a MinHeap priority queue for efficient
distance tracking and node selection.

Algorithm Steps:
    1. Initialize all distances to infinity except the source node (distance = 0)
    2. Create a min-heap priority queue and insert the source node with distance 0
    3. While the priority queue is not empty:
       a. Extract the node with the minimum distance from the queue
       b. Skip if this node has already been visited (to avoid reprocessing)
       c. Mark the current node as visited
       d. For each neighbor of the current node:
          i. Calculate alternative distance (current distance + edge weight)
          ii. If alternative distance is less than recorded distance:
              - Update the distance to the alternative distance
              - Insert the neighbor with new distance into the priority queue
    4. Return the final distance array containing shortest distances from source

Graph Format:
    The graph is expected as a dictionary where:
    - Keys: vertex indices (integers)
    - Values: list of tuples (neighbor, weight) representing edges

Complexity Analysis:
    Time Complexity: O((V + E) log V)
    - V = number of vertices in the graph
    - E = number of edges in the graph
    - Initialization: O(V) for distance and visited arrays
    - Main loop: Each vertex is processed once (V times)
      - Extract min from heap: O(log V)
      - For each vertex, iterate through all edges: O(E) total
    - Priority queue operations: O(log V) per insertion and extraction

    Space Complexity: O(V)
    - Distance array: O(V)
    - Visited array: O(V)
    - Priority queue: O(V) in worst case (all nodes in heap)
"""
