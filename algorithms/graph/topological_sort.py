"""
Topological Sort Algorithm

This module implements Kahn's algorithm for topological sorting of a directed
acyclic graph (DAG). Topological sorting orders the vertices of a directed graph
such that for every directed edge u → v, vertex u comes before vertex v in the
ordering. This is particularly useful for scheduling tasks with dependencies.

Algorithm Steps:
1. Calculate the in-degree of each vertex (number of incoming edges)
2. Initialize a queue with all vertices having zero in-degree
3. While the queue is not empty:
   a. Dequeue a vertex u and add it to the result
   b. For each neighbor v of u:
      i. Decrement the in-degree of v
      ii. If the in-degree becomes zero, enqueue v
4. If the number of vertices in the result equals the total vertices, 
   the graph is a DAG and the result contains a valid topological order
   Otherwise, the graph contains a cycle

Space Complexity: O(V) for the in-degree array and queue

Time Complexity: O(V + E) where V is the number of vertices and E is the number
                  of edges. We process each vertex and edge exactly once.

Kahn's Algorithm Visualization:
-------------------------------
Consider this DAG:
    A → B → D
    ↓   ↓
    C → E

Edge list: [(A,B), (A,C), (B,D), (C,E)]

Step 1: Calculate In-Degrees
    A: 0 (no incoming edges)
    B: 1 (from A)
    C: 1 (from A)
    D: 1 (from B)
    E: 1 (from C)
    
    In-Degree: [A:0, B:1, C:1, D:1, E:1]

Step 2: Initialize Queue with zero in-degree vertices
    Queue: [A]
    Result: []

Step 3: Extract vertex A from queue
    Queue: []
    Result: [A]
    Update in-degrees for neighbors of A:
        - For B: in-degree[1] = 0, enqueue B
        - For C: in-degree[2] = 0, enqueue C
    In-Degree: [A:0, B:0, C:0, D:1, E:1]
    Queue: [B, C]

Step 4: Extract vertex B from queue
    Queue: [C]
    Result: [A, B]
    Update in-degrees for neighbors of B:
        - For D: in-degree[3] = 0, enqueue D
    In-Degree: [A:0, B:0, C:0, D:0, E:1]
    Queue: [C, D]

Step 5: Extract vertex C from queue
    Queue: [D]
    Result: [A, B, C]
    Update in-degrees for neighbors of C:
        - For E: in-degree[4] = 0, enqueue E
    In-Degree: [A:0, B:0, C:0, D:0, E:0]
    Queue: [D, E]

Step 6: Extract vertex D from queue
    Queue: [E]
    Result: [A, B, C, D]
    No neighbors to process

Step 7: Extract vertex E from queue
    Queue: []
    Result: [A, B, C, D, E]
    No neighbors to process

Step 8: Check completion
    Result length (5) equals vertices (5) ✓
    No cycle detected

Final Topological Order: [A, B, C, D, E]

Cycle Detection Example:
-------------------------
Consider this cyclic graph:
    A → B → C → A

Step 1: Calculate In-Degrees
    A: 1 (from C)
    B: 1 (from A)
    C: 1 (from B)

Step 2: Initialize Queue
    Queue: [] (no vertices with zero in-degree)
    Result: []

Step 3: Extract from queue
    Queue is empty, loop ends immediately

Step 4: Check completion
    Result length (0) equals vertices (3) ✗
    Raises: Exception("Graph contains a cycle")
"""


from queue import Queue

def topological_sort(graph: dict[int, list[int]]):
    v = len(graph)
    in_degree = [0 for _ in range(v)]

    for vertex, neighbors in graph.items():
        in_degree[vertex] += len(neighbors)

    queue = Queue()
    for v in graph:
        if in_degree[v] == 0:
            queue.enqueue(v)

    result = []
    while queue:
        u = queue.dequeue()
        result.add(u)

        for neighbor in graph[u]:
            in_degree[v] -= 1

            if in_degree[v] == 0:
                queue.enqueue(v)

    if len(result) != v:
        raise Exception("Graph contains a cycle")

    return result

