def solution(data):
    def has_cycle(graph):
        visited = set()
        rec_stack = set()

        for node in graph:
            if node not in visited:
                if dfs(graph, node, visited, rec_stack):
                    return True

        return False

    def dfs(graph, current, visited, rec_stack):
        if current not in visited:
            visited.add(current)
            rec_stack.add(current)

            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    if dfs(graph, neighbor, visited, rec_stack):
                        return True
                elif neighbor in rec_stack:
                    return True

        rec_stack.remove(current)
        return False

    return has_cycle(data["graph"])
