def bfs(graph, start):
    """
    Perform BFS on a graph without using a queue or Node structure.
    :param graph: Dictionary representing the adjacency list of the graph.
    :param start: Starting node for BFS.
    :return: List of nodes in BFS order.
    """
    visited = [] 
    result = []   

    frontier = [start]  
    while frontier:
        current = frontier[0]
        frontier = frontier[1:] 

        if current not in visited:
            visited.append(current)
            result.append(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    frontier.append(neighbor)

    return result

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    bfs_order = bfs(graph, start_node)
    print("BFS Traversal Order:", bfs_order)