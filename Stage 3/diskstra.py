from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

g = Graph(3)

def dijkstra(start_vertex, graph=g):
    graph.visited = []
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        dist, current_vertex = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                # print(current_vertex, neighbor, graph.edges[current_vertex][neighbor])
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

graph = {0: {1: 10, 2: 20},
         1: {0: 10, 2: 30},
         2: {0: 20, 1: 30}
    }

for node in graph.keys():
    for target in graph[node].keys():
        g.add_edge(node, target, graph[node][target])

for node in range(len(graph)):
    D = dijkstra(node)
    for vertex in range(len(D)):
        if vertex == node:
            continue
        print(f"Distance from vertex {node} to vertex {vertex} is {D[vertex]}")