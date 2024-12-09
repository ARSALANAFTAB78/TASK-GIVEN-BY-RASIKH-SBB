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


class Queue:
    """
    Simple Queue implementation using a list.
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0


def bfs(start_node):
    """
    Perform BFS starting from the given node.
    :param start_node: The starting Node object.
    :return: List of nodes in BFS order.
    """
    visited = set()  
    result = []     
    queue = Queue()  

    queue.enqueue(start_node)
    visited.add(start_node)

    while not queue.is_empty():
        current_node = queue.dequeue()
        result.append(current_node.value)

        for neighbor in current_node.neighbors:
            if neighbor not in visited:
                queue.enqueue(neighbor)
                visited.add(neighbor)

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

    bfs_order = bfs(node_a)
    print("BFS Traversal Order:", bfs_order)