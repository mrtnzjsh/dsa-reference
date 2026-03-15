# Breadth-First Search (BFS) Algorithm

## Overview

Breadth-First Search (BFS) is a graph traversal algorithm that starts from a source vertex and explores all vertices at the present depth prior to moving on to the vertices at the next depth level. It uses a queue data structure to keep track of vertices to visit next, ensuring that nodes are visited in a level-order manner.

## Algorithm Steps

### Recursive BFS Steps

1. Check if the level queue is empty - if yes, return
2. Iterate through all vertices in the current level (current queue size)
3. Pop each vertex from the front of the queue
4. Process the vertex (e.g., print its value)
5. For each unvisited neighbor:
   - Mark neighbor as visited
   - Add neighbor to the back of the queue
6. Recursively call BFS to process the next level

### Iterative BFS Steps

1. Initialize a queue with the starting vertex
2. Initialize a visited structure (boolean array or set)
3. Mark the starting vertex as visited
4. While the queue is not empty:
   - Dequeue the front vertex from the queue
   - Process the vertex
   - For each unvisited neighbor:
     - Mark neighbor as visited
     - Enqueue neighbor

## Input

- **graph**: An adjacency list representation of a graph as a list of lists, where each index represents a vertex and the value at that index is a list of its neighbors
- **vertex**: The starting vertex for the BFS traversal

## Output

The recursive version modifies the visited list in-place
The iterative version prints visited vertices and their values

## Example

**Bipartite Graph:** Edges = [(0, 1), (0, 3), (1, 2), (2, 3)], Vertices = 4

**Step-by-Step (Starting from vertex 0):**
- Start with vertex 0: print 0
- Neighbors of 0 (1, 2): mark as visited, enqueue
- Neighbors of 1 (0, 3): 0 already visited, 3 marked as visited, enqueue
- Neighbors of 2 (0, 3): both already visited
- Neighbors of 3 (1, 2): both already visited
- Output: 0 1 2 3

**Non-Bipartite Graph:** Edges = [(0, 1), (1, 2), (2, 0)], Vertices = 3

**Step-by-Step (Starting from vertex 0):**
- Start with vertex 0: print 0
- Neighbors of 0 (1): mark as visited, enqueue
- Neighbors of 1 (2): mark as visited, enqueue
- Neighbors of 2 (0): 0 already visited
- Output: 0 1 2

**Step-by--step example for bfs_recursive:**

1. Call bfs_recursive(graph, [0], [False, False, False, False])
2. level_queue is not empty
3. Iteration: Process vertex 0
   - Pop left: vertex = 0
   - Print 0
   - Neighbors of 0: [1, 2]
   - For neighbor 1: visited[1] = False → level_queue.append(1)
   - For neighbor 2: visited[2] = False → level_queue.append(2)
4. level_queue is now [1, 2]
5. Recursively call bfs_recursive(graph, [1, 2], visited)
6. Iteration: Process first vertex (original 0's neighbor)
   - Pop left: vertex = 1
   - Print 1
   - Neighbors of 1: [0, 3]
   - For neighbor 0: visited[0] = True → skip
   - For neighbor 3: visited[3] = False → level_queue.append(3)
7. level_queue is now [2, 3]
8. Iteration: Process second vertex (original 0's neighbor)
   - Pop left: vertex = 2
   - Print 2
   - Neighbors of 2: [0, 3]
   - For neighbor 0: visited[0] = True → skip
   - For neighbor 3: visited[3] = True → skip
9. level_queue is now [3]
10. Recursively call bfs_recursive(graph, [3], visited)
11. level_queue is now empty → return

## Complexity Analysis

**Time Complexity:** O(V + E) where V is the number of vertices and E is the number of edges
- Each vertex is visited exactly once
- Each edge is examined at most twice (once from each endpoint)
- Total: O(V + E) time complexity

**Space Complexity:** O(V)
- BFS uses O(V) space for the queue
- Queue can contain up to V elements in worst case (when the graph is fully connected)
- The visited array or set also uses O(V) space
- Total space complexity: O(V)

## Notes

BFS is ideal for finding the shortest path in an unweighted graph, as it explores all nodes at distance k before any nodes at distance k+1. For weighted graphs where edge weights are known, Dijkstra's algorithm should be used instead. BFS also distinguishes between breadth-first search on trees (where each node has a unique parent) and graphs (where nodes can have multiple parents). The recursive implementation uses a level-based queue approach, processing all nodes at the current level before moving to the next level. For very deep graphs, the iterative implementation is preferred to avoid potential stack overflow issues.

### Applications
- Shortest path finding in unweighted graphs
- Level-order traversal of trees
- Finding connected components
- Bipartite graph checking
- Social network analysis (distance between users)
- Web crawlers
