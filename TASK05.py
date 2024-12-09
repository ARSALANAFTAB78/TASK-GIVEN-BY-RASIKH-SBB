class Node:
    """
    Represents a node in the graph.
    """
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor):
        """
        Add a neighboring node to the current node.
        """
        self.neighbors.append(neighbor)

def dfs(start_node):
    """
    Perform DFS using a stack.
    :param start_node: The starting Node object.
    :return: List of nodes in DFS order.
    """
    visited = set()  
    result = []      
    stack = [start_node] 

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            result.append(current_node.value)

            for neighbor in reversed(current_node.neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result

if __name__ == "__main__":
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')
    node_e = Node('E')
    node_f = Node('F')

    node_a.add_neighbor(node_b)
    node_a.add_neighbor(node_c)
    node_b.add_neighbor(node_d)
    node_b.add_neighbor(node_e)
    node_c.add_neighbor(node_f)
    node_e.add_neighbor(node_f)

    dfs_order = dfs(node_a)
    print("DFS Traversal Order:", dfs_order)