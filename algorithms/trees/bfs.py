from collections import deque


def bfs_recursive(graph: list[list[int]], level_queue: deque, visited: list[bool]) -> None:

    if not level_queue:
        return

    for _ in range(len(level_queue)):
        vertex = level_queue.popleft()

        # Process node
        print(vertex)

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                level_queue.append(neighbor)
    bfs_recursive(graph, level_queue, visited)


def bfs_iterative(graph: list[list[int]], vertex: int) -> None:
    queue = deque([])

    queue.append(vertex)
    visited = [False for _ in range(len(graph))]
    visited[vertex] = True

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()

            # Process node
            print(curr)

            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
