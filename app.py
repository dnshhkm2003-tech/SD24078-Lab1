
import streamlit as st
from collections import deque

st.set_page_config(page_title="BFS and DFS", page_icon="🔎")

st.title("BSD3513: AI Search Algorithms")
st.write("Explore Breadth-First Search (BFS) and Depth-First Search (DFS).")

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

st.subheader("Directed Graph")
st.write("Starting node and connections:")
st.json(graph)

algorithm = st.selectbox(
    "Choose an algorithm",
    ["BFS", "DFS"]
)

start = st.selectbox(
    "Choose starting node",
    sorted(graph.keys())
)

if st.button("Run Search"):
    if algorithm == "BFS":
        result = bfs(graph, start)
    else:
        result = dfs(graph, start)

    st.subheader("Traversal Order")
    st.write(" → ".join(node for node, level in result))

    st.subheader("Node Levels")
    for node, level in result:
        st.write(f"Node {node}: Level {level}")

    st.subheader("Algorithm Complexity")
    st.write("Time Complexity: O(V + E)")
    st.write("Space Complexity: O(V)")

    st.success("Search completed successfully!")

st.caption("BSD3513 - Lab Report 1")
