from collections import deque


def solution(data):
    def bfs_shortest_path(graph, start, end):
        visited = set()
        queue = deque([(start, 0)])  # (current node, distance)

        while queue:
            current, distance = queue.popleft()
            if current == end:
                return distance

            if current not in visited:
                visited.add(current)
                for neighbor in graph.get(current, []):
                    queue.append((neighbor, distance + 1))

        return -1  # Path not found

    graph = data["graph"]
    start = data["start"]
    end = data["end"]
    return bfs_shortest_path(graph, start, end)
