from typing import List

def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    """
    Computes the shortest paths between all pairs of vertices in a weighted graph.
    
    Args:
        graph (List[List[int]]): An adjacency matrix representing the graph where 
                                 graph[i][j] is the weight of the edge from i to j. 
                                 Use float('inf') for missing edges.
        
    Returns:
        List[List[int]]: A matrix containing the shortest distance between every pair of vertices.
    """
    V = len(graph)
    
    # Initialize the distance matrix as a copy of the input graph matrix
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    
    # k represents the intermediate vertex being considered
    for k in range(V):
        # i represents the source vertex
        for i in range(V):
            # j represents the destination vertex
            for j in range(V):
                # If vertex k is on the shortest path from i to j, update the value of dist[i][j]
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
    return dist

def optimal_bst(keys: List[int], freq: List[int]) -> int:
    """
    Calculates the minimum search cost of an Optimal Binary Search Tree (BST).
    
    Args:
        keys (List[int]): A sorted list of search keys.
        freq (List[int]): The corresponding frequencies of searches for each key.
        
    Returns:
        int: The minimum cost of the Optimal Binary Search Tree.
    """
    n = len(keys)
    if n == 0:
        return 0
        
    # cost[i][j] stores the optimal search cost of a BST containing keys from i to j
    cost = [[0] * n for _ in range(n)]
    
    # Base case: A tree with a single node has a cost equal to its frequency
    for i in range(n):
        cost[i][i] = freq[i]
        
    # L is the chain length of keys being considered (from 2 to n)
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = float('inf')
            
            # The cost of any subtree requires adding the sum of frequencies 
            # of all its keys because their depth increases by 1
            freq_sum = sum(freq[i:j + 1])
            
            # Try making every key in the range keys[i..j] the root
            for r in range(i, j + 1):
                # Cost of left subtree
                c_left = cost[i][r - 1] if r > i else 0
                # Cost of right subtree
                c_right = cost[r + 1][j] if r < j else 0
                
                # Total cost for choosing r as the root
                total_cost = c_left + c_right + freq_sum
                
                if total_cost < cost[i][j]:
                    cost[i][j] = total_cost
                    
    # The optimal cost for the entire tree containing all keys
    return cost[0][n - 1]

# Example Usage:
if __name__ == "__main__":
    INF = float('inf')
    
    # Floyd-Warshall Example
    # Adjacency matrix representation of a graph
    graph_matrix = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]
    
    print("Floyd-Warshall All-Pairs Shortest Path Matrix:")
    shortest_paths = floyd_warshall(graph_matrix)
    for row in shortest_paths:
        print(row)
        
    print("\n" + "-"*40 + "\n")
    
    # Optimal BST Example
    # Keys must be sorted for a valid BST
    bst_keys = [10, 12, 20]
    bst_freqs = [34, 8, 50]
    
    print(f"Keys: {bst_keys}")
    print(f"Frequencies: {bst_freqs}")
    optimal_cost = optimal_bst(bst_keys, bst_freqs)
    print(f"Minimum cost of Optimal Binary Search Tree: {optimal_cost}")