class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0 
        self.h = 0 
        self.f = 0 

    def __eq__(self, other):
        return self.position == other.position

def a_star_algorithm(start, end, grid):
    """
    :param start: Tuple of start coordinates (row, col)
    :param end: Tuple of end coordinates (row, col)
    :param grid: 2D list representing the grid (0 = walkable, 1 = obstacle)
    :return: Shortest path as a list of tuples or None if no path exists
    """
    open_list = []
    closed_list = []

    start_node = Node(start)
    end_node = Node(end)
    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1] 
        neighbors = [
            (0, -1),
            (0, 1), 
            (-1, 0), 
            (1, 0)  
        ]

        for neighbor in neighbors:
            neighbor_pos = (
                current_node.position[0] + neighbor[0],
                current_node.position[1] + neighbor[1]
            )

            if (
                0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0
            ):
                neighbor_node = Node(neighbor_pos, current_node)

                if neighbor_node in closed_list:
                    continue

                neighbor_node.g = current_node.g + 1
                neighbor_node.h = abs(neighbor_pos[0] - end_node.position[0]) + abs(neighbor_pos[1] - end_node.position[1])  # Manhattan distance
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if any(open_node for open_node in open_list if neighbor_node == open_node and neighbor_node.g >= open_node.g):
                    continue

                open_list.append(neighbor_node)

    return None 

if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ] 

    start = (0, 0) 
    end = (4, 4)  

    path = a_star_algorithm(start, end, grid)

    if path:
        print("Shortest Path:", path)
    else:
        print("No path found.")