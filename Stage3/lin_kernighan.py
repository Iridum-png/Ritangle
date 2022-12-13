import numpy as np

def lin_kernighan(distances):
    # Initialize the current tour with a random permutation of the nodes
    current_tour = list(range(len(distances)))
    np.random.shuffle(current_tour)
    
    # Initialize the best tour with the current tour
    best_tour = current_tour
    
    # Loop until no improvements are found
    while True:
        # Find the sub-tour in the current tour to modify
        sub_tour = find_sub_tour(current_tour)
        
        # Find the best possible modification to the sub-tour
        modified_sub_tour = find_best_modification(sub_tour, distances)
        
        # Replace the sub-tour with the modified sub-tour in the current tour
        current_tour = replace_sub_tour(current_tour, sub_tour, modified_sub_tour)
        
        # Check if the modified tour is better than the best tour
        if tour_length(current_tour, distances) < tour_length(best_tour, distances):
            # Update the best tour
            best_tour = current_tour
        else:
            # No more improvements can be found, return the best tour
            return best_tour
	    
def find_sub_tour(tour):
    # Randomly select two nodes from the tour
    node1, node2 = np.random.choice(tour, 2)
    
    # Find the sub-tour by starting at node1 and following the tour until node2 is reached
    sub_tour = []
    for i in range(len(tour)):
        sub_tour.append(tour[i])
        if tour[i] == node2:
            break
    return sub_tour
    
def find_best_modification(sub_tour, distances):
    # Initialize the best modification to the sub-tour with the original sub-tour
    best_modification = sub_tour
    
    # Loop over the possible modifications to the sub-tour
    for i in range(1, len(sub_tour) - 1):
        for j in range(i + 1, len(sub_tour)):
            # Create a new sub-tour by reversing the section between i and j in the original sub-tour
            new_sub_tour = sub_tour[:i] + list(reversed(sub_tour[i:j])) + sub_tour[j:]
            
            # Check if the new sub-tour is better than the best modification
            if tour_length(new_sub_tour, distances) < tour_length(best_modification, distances):
                # Update the best modification
                best_modification = new_sub_tour
		
    return best_modification

def replace_sub_tour(tour, sub_tour, modified_sub_tour):
    # Find the start and end indices of the sub-tour in the original tour
    start_index = tour.index(sub_tour[0])
    end_index = start_index + len(sub_tour)
    
    # Create a new tour by replacing the sub-tour with the modified sub-tour
    new_tour = tour[:start_index] + modified_sub_tour + tour[end_index:]
    
    return new_tour

def tour_length(tour, distances):
    # Initialize the length of the tour with the distance from the last node to the first node
    length = distances[tour[-1]][tour[0]]
    
    # Loop over the nodes in the tour and add the distance from each node to the next node to the length
    for i in range(len(tour) - 1):
        length += distances[tour[i]][tour[i + 1]]
    
    return length

def open_file():
    with open(r'C:\Users\ed9ba\Documents\Coding\Python\Ritangle\Stage 3\graph.txt', 'r') as f:
        distances = f.readlines()

    for i, subarray in enumerate(distances):
        distances[i] = subarray.replace(" \n", "")
        distances[i] = distances[i].split(" ")
        
    # Convert all values in the array to floats
    for i, subarray in enumerate(distances):
        for j, value in enumerate(subarray):
            distances[i][j] = float(value)
            
    return distances



def calc_distance(distances, best_tour):
    total_distance = 0

    for i in range(len(best_tour) - 1):
        total_distance += distances[best_tour[i] - 1][best_tour[i + 1] - 1]
    return total_distance

def get_best():
    best_tour = lin_kernighan(distances)
    while True:
        best_tour = lin_kernighan(distances)
        if best_tour[0] == 1 and best_tour[-1] == 58:
            print(best_tour)
            print(len(set(best_tour)))
            return best_tour

distances = open_file()

possible = []

# best_tour = [1, 4, 15, 9, 17, 38, 56, 57, 35, 27, 53, 3, 7, 11, 6, 46, 59, 54, 10, 18, 49, 30, 40, 36, 23, 39, 22, 55, 19, 32, 51, 44, 29, 42, 50, 26, 31, 25, 45, 21, 43, 33, 12, 2, 0, 41, 20, 5, 13, 24, 37, 47, 48, 52, 8, 14, 34, 28, 16, 58]
for i in range(10):
    best_tour = get_best()

    total_distance = calc_distance(distances, best_tour)
        
    print(total_distance)
    possible.append(total_distance)
print(min(possible))