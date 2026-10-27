from typing import List

class TSPSolver:
    """
    Class to solve the Traveling Salesperson Problem (TSP).
    Finds the minimum cost to visit all nodes exactly once and return to the starting node.
    """
    
    def solve_tsp(self, dist_matrix: List[List[int]]) -> int:
        """
        Calculates the minimum tour cost using Dynamic Programming and Bitmasking (Held-Karp algorithm).
        
        Args:
            dist_matrix (List[List[int]]): An adjacency matrix representing distances between cities,
                                           where dist_matrix[i][j] is the distance from city i to city j.
                                           
        Returns:
            int: The minimum cost of the TSP tour.
        """
        n = len(dist_matrix)
        if n == 0:
            return 0
        if n == 1:
            return dist_matrix[0][0]
            
        # ALL_VISITED is a bitmask where all 'n' bits are set to 1.
        # For example, if n=4, ALL_VISITED = (1 << 4) - 1 = 15 (binary 1111).
        ALL_VISITED = (1 << n) - 1
        
        # memoization table: dictionary mapping (visited_mask, current_city) to min_cost
        memo = {}

        def tsp(mask: int, pos: int) -> int:
            """
            Recursive helper function to find the minimum cost path.
            
            Args:
                mask (int): Bitmask representing the set of visited cities.
                pos (int): The current city we are at.
            """
            # Base case: if all cities have been visited, return the cost to go back to the start (city 0)
            if mask == ALL_VISITED:
                return dist_matrix[pos][0]
            
            # Check if this state has already been computed to avoid redundant calculations
            if (mask, pos) in memo:
                return memo[(mask, pos)]
            
            min_cost = float('inf')
            
            # Try visiting every other city
            for city in range(n):
                # Check if the 'city' is unvisited in the current mask
                # (mask & (1 << city)) extracts the bit corresponding to 'city'
                if (mask & (1 << city)) == 0:
                    # Mark the new city as visited
                    new_mask = mask | (1 << city)
                    
                    # Calculate cost of this choice and recurse
                    cost = dist_matrix[pos][city] + tsp(new_mask, city)
                    min_cost = min(min_cost, cost)
            
            # Store the computed minimum cost for this state and return it
            memo[(mask, pos)] = min_cost
            return min_cost

        # Start the tour at city 0, so the 0th bit is set to 1 (mask = 1)
        return tsp(1, 0)


# Example Usage:
if __name__ == "__main__":
    # Example adjacency matrix representing distances between 4 cities
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    solver = TSPSolver()
    min_tour_cost = solver.solve_tsp(distance_matrix)
    
    print("Distance Matrix:")
    for row in distance_matrix:
        print(row)
        
    print(f"\nMinimum TSP Tour Cost: {min_tour_cost}")