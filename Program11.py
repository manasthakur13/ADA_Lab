from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    """
    Calculates the length of the longest strictly increasing subsequence in an array.
    
    Args:
        nums (List[int]): An array of integers.
        
    Returns:
        int: The length of the longest strictly increasing subsequence.
    """
    if not nums:
        return 0
        
    n = len(nums)
    
    # Initialize a DP array where dp[i] represents the length of the longest 
    # increasing subsequence that ends with nums[i].
    # Every element is a valid subsequence of length 1 by itself.
    dp = [1] * n
    
    # Iterate through the array to build the DP table bottom-up
    for i in range(1, n):
        # Check all previous elements before the current element nums[i]
        for j in range(i):
            # If the previous element is strictly smaller, we can append nums[i]
            # to the subsequence ending at nums[j]
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    # The result is the maximum value found in the DP array
    return max(dp)

# Example Usage:
if __name__ == "__main__":
    test_nums = [10, 9, 2, 5, 3, 7, 101, 18]
    
    lis_length = lengthOfLIS(test_nums)
    print(f"Array: {test_nums}")
    print(f"Length of Longest Increasing Subsequence: {lis_length}")