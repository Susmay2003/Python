# Graph defined as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Breadth-First Search (BFS)
def bfs(graph, start_node):
    visited = []            # List to store visited nodes
    queue = [start_node]    # Manual queue using list

    print("BFS Traversal:")
    while len(queue) > 0:
        current_node = queue[0]
        del queue[0]  # Remove front (FIFO)

        if current_node not in visited:
            print(current_node, end=' ')
            visited.append(current_node)

            # Add unvisited neighbors to the queue
            for neighbor in graph[current_node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    print()

# Depth-First Search (DFS)
def dfs(graph, start_node):
    visited = []           # List to store visited nodes
    stack = [start_node]   # Manual stack using list

    print("DFS Traversal:")
    while len(stack) > 0:
        current_node = stack[-1]
        stack.pop()  # Remove from end (LIFO)

        if current_node not in visited:
            print(current_node, end=' ')
            visited.append(current_node)

            # Add neighbors in reverse order to maintain correct DFS order
            neighbors = graph[current_node]
            for i in range(len(neighbors) - 1, -1, -1):
                if neighbors[i] not in visited and neighbors[i] not in stack:
                    stack.append(neighbors[i])
    print()

# Run the search algorithms
bfs(graph, 'A')
dfs(graph, 'A')
