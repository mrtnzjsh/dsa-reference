# Dijkstra's Shortest Path Algorithm Implementation

# This module implements Dijkstra's algorithm to find the shortest paths from a source node
# to all other nodes in a weighted graph using a MinHeap priority queue for efficient
# distance tracking and node selection

# Algorithm Steps:
#     1. Initialize all distances to infinity except the source node (distance = 0)
#     2. Create a min-heap priority queue and insert the source node with distance 0
#     3. While the priority queue is not empty:
#        a. Extract the node with the minimum distance from the queue
#        b. Skip if this node has already been visited (to avoid reprocessing)
#        c. Mark the current node as visited
#        d. For each neighbor of the current node:
#           i. Calculate alternative distance (current distance + edge weight)
#           ii. If alternative distance is less than recorded distance:
#               - Update the distance to the alternative distance
#               - Insert the neighbor with new distance into the priority queue
#     4. Return the final distance array containing shortest distances from source

from dsa_reference.data_structures.trees.heaps import MinHeap

def djikstra(graph: dict[int, list[tuple[int, int]]], source: int) -> list[int]:
    dist = [float('inf') for _ in range(len(graph))]
    dist[source] = 0
    visited = [False for _ in range(len(graph))]

    pq = MinHeap()
    pq.insert((0, source))

    while pq:
        current_dist, vertex = pq.extract_min()
        if visited[vertex]:
            continue
        visited[vertex] = True

        for neighbor, cost in graph[vertex]:
            if not visited[neighbor]:
                alt_dist = dist[vertex] + cost
                if alt_dist < dist[vertex]:
                    dist[vertex] = alt_dist
                    pq.insert((dist[vertex], cost))

    return dist
