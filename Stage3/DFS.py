
def shortestPathLength(graph: list[list[int]]) -> int:
    length = len(graph)
    result = 0
    visited_node = []
    queue = []  

    for i in range(length):
        visited_node.append(set([1<<i]))
        queue.append([i,1<<i])

    while queue:
        result = result + 1
        new_queue = []
        for node, value in queue:
            for neigbour_node in graph[node]:
                mid_node = (1<<neigbour_node)|value
                if mid_node not in visited_node[neigbour_node]:
                    if mid_node+1 == 1<<length:
                        return result

                    visited_node[neigbour_node].add(mid_node)
                    new_queue.append([neigbour_node, mid_node])
        queue = new_queue
    return 0

coords = [[1,2], [1,27], [2,1], [2,27], [2,21], [2,17], [3,7], [3,10], [3,14], [3,23], [3,25], [3,26], [5,15], [5,22], [6,13], [6,23], [7,3], [7,18], [7,19], [7,26], [9,13], [9,22], [10,3], [10,25], [11,17], [11,18], [13,6], [13,9], [13,22], [13,23], [14,3], [14,23], [15,5], [15,22], [17,2], [17,11], [17,18], [17,21], [18,7], [18,11], [18,17], [18,19], [19,7], [19,18], [21,2], [21,17], [22,5], [22,9], [22,13], [22,15], [23,3], [23,6], [23,13], [23,14], [25,3], [25,10], [26,3], [26,7], [27,1], [27,2]]
unweighted = []

for i in range(30):
    unweighted.append([])
    for j in range(30):
        if i != j:
            unweighted[i].append(j)

print(shortestPathLength(unweighted))