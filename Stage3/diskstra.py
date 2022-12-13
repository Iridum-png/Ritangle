from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

g = Graph(60)

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

with open(r"C:\Users\ed9ba\Documents\Coding\Python\Ritangle\Stage 3\graph.json", "r") as f:
    graph = eval(f.read())

for node in graph.keys():
    for target in graph[node].keys():
        g.add_edge(node, target, graph[node][target])

open("Stage 3\graph.txt", "w").close()

for node in range(len(graph)):
    D = dijkstra(node)
    curr_node = []
    for vertex in range(len(D)):
        if vertex == node:
            curr_node.append(0)
            continue
        curr_node.append(D[vertex])
    with open("Stage 3\graph.txt", "a") as f:
        for i in range(len(curr_node)):
            f.write(str(curr_node[i]) + " ")
        f.write("\n")
