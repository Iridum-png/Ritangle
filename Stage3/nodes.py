from math import tan, pi

class Node:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.c = 734 - (x ** 2 + y ** 2)
        self.height = 0.1875 * self.c
        self.data = []

    def distance_to_node(self, node):
        return ((self.x - node.x) ** 2 + (self.y - node.y) ** 2) ** 0.5

    def get_coordinates(self):
        return (self.x, self.y)

    def closest_coord(self):
        mindist = float("inf")
        data = [0, 0, 0, 0, 0]
        for x in range(1, 29):
            for y in range(1, 29):
                dist = self.distance_to_node(Node(x, y))
                if dist < mindist and Node(x, y).distance_to_node(Node(0, 0)) >= 28:
                    data[0] = self.x
                    data[1] = self.y
                    data[2] = x
                    data[3] = y
                    data[4] = dist
                    mindist = dist
        self.data = data
        return data

    def angle(self):
        target, height = self.data[4], self.height
        for angle in range(90, 0, -1):
            if abs(height / tan_degrees(angle)) >= target:
                # print(angle, height, target)
                return angle

def create_nodes():
    coords = [[1,2], [1,27], [2,1], [2,27], [2,21], [2,17], [3,7], [3,10], [3,14], [3,23], [3,25], [3,26], [5,15], [5,22], [6,13], [6,23], [7,3], [7,18], [7,19], [7,26], [9,13], [9,22], [10,3], [10,25], [11,17], [11,18], [13,6], [13,9], [13,22], [13,23], [14,3], [14,23], [15,5], [15,22], [17,2], [17,11], [17,18], [17,21], [18,7], [18,11], [18,17], [18,19], [19,7], [19,18], [21,2], [21,17], [22,5], [22,9], [22,13], [22,15], [23,3], [23,6], [23,13], [23,14], [25,3], [25,10], [26,3], [26,7], [27,1], [27,2]]
    nodes = []

    for pair in coords:
        if pair[0] >= pair[1]:
            nodes.append(Node(pair[0], pair[1]))
    return nodes, coords

def tan_degrees(degrees):
    return tan(degrees * pi / 180)

nodes, coords = create_nodes()
node = Node(22, 15)
print(node.closest_coord())
print(node.angle())