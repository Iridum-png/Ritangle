import math

def held_karp(distances):
  # Create a dictionary to store the minimum distance to each subproblem
  min_distances = {}
  
  # Define a helper function to calculate the minimum distance to each subproblem
  def get_min_distance(visited, last):
    # Create a tuple representing the subproblem
    subproblem = (visited, last)
    
    # If the subproblem has already been solved, return the stored solution
    if subproblem in min_distances:
      return min_distances[subproblem]
    
    # If all the cities have been visited, return the distance to return to the starting city
    if visited == (1 << len(distances)) - 1:
      return distances[last][0]
    
    # Set the minimum distance to a large number
    min_distance = math.inf
    
    # Iterate over the cities
    for city in range(len(distances)):
      # Skip the city if it has already been visited
      if visited & (1 << city):
        continue
      
      # Calculate the minimum distance to the subproblem by visiting the current city
      distance = distances[last][city] + get_min_distance(visited | (1 << city), city)
      
      # Update the minimum distance if necessary
      min_distance = min(min_distance, distance)
    
    # Store the minimum distance to the subproblem and return it
    min_distances[subproblem] = min_distance
    return min_distance
  
  # Return the minimum distance to the original problem by starting at city 0
  return get_min_distance(1, 0)

def open_file():
    with open(r'C:\Users\ed9ba\Documents\Coding\Python\Ritangle\Stage3\graph.txt', 'r') as f:
        distances = f.readlines()

    for i, subarray in enumerate(distances):
        distances[i] = subarray.replace(" \n", "")
        distances[i] = distances[i].split(" ")
        
    # Convert all values in the array to floats
    for i, subarray in enumerate(distances):
        for j, value in enumerate(subarray):
            distances[i][j] = float(value)
            
    return distances

distances = open_file()

best = held_karp(distances)

print(best)