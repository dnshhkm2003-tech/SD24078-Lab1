
from collections import deque

graph = {
    "A": ["B", "D"],
    "B": ["C", "E", "G"],
    "C": ["A"],
    "D": ["C"],
    "E": ["H"],
    "F": [],
    "G": ["F"],
    "H": ["F", "G"]
}

def bfs(graph, start):
    visited = {start}
    queue = deque([(start, 0)])
    result = []

    while queue:
        node, level = queue.popleft()
        result.append((node, level))

        for neighbour in sorted(graph[node]):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, level + 1))

    return result

def dfs(graph, start):
    visited = set()
    result = []

    def visit(node, level):
        visited.add(node)
        result.append((node, level))

        for neighbour in sorted(graph[node]):
            if neighbour not in visited:
                visit(neighbour, level + 1)

    visit(start, 0)
    return result

print("BFS:", bfs(graph, "A"))
print("DFS:", dfs(graph, "A"))
