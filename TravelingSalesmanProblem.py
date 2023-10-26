'''
Question:
Given a list of cities and the distances between each pair of cities, 
what is the shortest possible route that visits each city exactly once and returns to the original city?

Solution:
There are many ways to approach the TSP, from exact algorithms like dynamic programming and branch-and-bound to heuristics and metaheuristics 
like the nearest neighbor algorithm, genetic algorithms, and simulated annealing.

Here, for simplicity's sake, I'll present a solution using the nearest neighbor algorithm. The nearest neighbor algorithm 
isn't always optimal, but it provides a feasible solution to the problem.
'''


def nearest_neighbor(cities, distance_matrix):
    current_city = 0  # Starting from the first city
    path = [current_city]

    unvisited_cities = set(range(len(cities))) - {current_city}

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: distance_matrix[current_city][city])
        path.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city

    path.append(path[0])  # return to the starting city
    return path


cities = ["A", "B", "C", "D"]
# Example distance matrix for 4 cities. distance_matrix[i][j] is the distance from city i to city j.
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path = nearest_neighbor(cities, distance_matrix)
print("Path:", " -> ".join(cities[i] for i in path))
