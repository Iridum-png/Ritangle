# A Star algorithm that needs to cross through every target node on a 28x28 grid
# I have a list of coordinates that I need to cross through
# I need to find the shortest path to cross through all of them

import heapq


class Node:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def distance_to_node(self, node):
        return ((self.x - node.x) ** 2 + (self.y - node.y) ** 2) ** 0.5
    
    def get_coordinates(self):
        return (self.x, self.y)
    
def create_nodes():
    coords = [[1,2], [1,27], [2,1], [2,27], [2,21], [2,17], [3,7], [3,10], [3,14], [3,23], [3,25], [3,26], [5,15], [5,22], [6,13], [6,23], [7,3], [7,18], [7,19], [7,26], [9,13], [9,22], [10,3], [10,25], [11,17], [11,18], [13,6], [13,9], [13,22], [13,23], [14,3], [14,23], [15,5], [15,22], [17,2], [17,11], [17,18], [17,21], [18,7], [18,11], [18,17], [18,19], [19,7], [19,18], [21,2], [21,17], [22,5], [22,9], [22,13], [22,15], [23,3], [23,6], [23,13], [23,14], [25,3], [25,10], [26,3], [26,7], [27,1], [27,2]]
    nodes = []

    for pair in coords:
        if pair[0] >= pair[1]:
            nodes.append(Node(pair[0], pair[1]))
    return nodes

nodes = create_nodes()

# Calculate the distance between each node
with open("nodes.txt", "w") as f:
    for i in range(len(nodes)):
        for j in range(i, len(nodes)):
            if i != j:
                f.write(f"g.add_edge({i}, {j}, {nodes[i].distance_to_node(nodes[j])})\n")