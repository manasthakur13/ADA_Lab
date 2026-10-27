from typing import List

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Solves the 0/1 Knapsack problem using a 1D Dynamic Programming approach.
    
    Args:
        weights (List[int]): The weights of the available items.
        values (List[int]): The values of the available items.
        capacity (int): The maximum weight capacity of the knapsack.
        
    Returns:
        int: The maximum value that can be accommodated within the given capacity.
    """
    # Initialize a 1D DP array of size (capacity + 1) with zeros.
    # dp[w] stores the maximum value achievable with a knapsack capacity of w.
    dp = [0] * (capacity + 1)
    
    # Iterate through each item's weight and value
    for i in range(len(weights)):
        weight = weights[i]
        value = values[i]
        
        # Traverse capacities backwards from total capacity down to the current item's weight.
        # Traversing backwards prevents counting an item multiple times, preserving the 0/1 constraint.
        for w in range(capacity, weight - 1, -1):
            # Update the DP table by choosing the maximum between not taking the item 
            # (dp[w]) and taking the item (dp[w - weight] + value).
            dp[w] = max(dp[w], dp[w - weight] + value)
            
    # The last element in the array represents the max value for the full capacity
    return dp[capacity]

# Example Usage:
if __name__ == "__main__":
    item_weights = [10, 20, 30]
    item_values = [60, 100, 120]
    max_capacity = 50
    
    max_value = knapsack_01(item_weights, item_values, max_capacity)
    print(f"Maximum value in 0/1 Knapsack: {max_value}")