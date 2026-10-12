import random
from typing import List, Tuple

def partition(nums: List[int], left: int, right: int) -> int:
    """Standard Lomuto partition scheme."""
    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i

def randomized_partition(nums: List[int], left: int, right: int) -> int:
    """Picks a random pivot to ensure O(N) average time complexity."""
    rand_pivot_idx = random.randint(left, right)
    # Swap random pivot to the end
    nums[rand_pivot_idx], nums[right] = nums[right], nums[rand_pivot_idx]
    return partition(nums, left, right)

def quickselect(nums: List[int], left: int, right: int, target_index: int) -> int:
    """
    Randomized Quickselect algorithm. 
    Finds the element at target_index in its sorted position in O(N) average time.
    """
    if left == right:
        return nums[left]
        
    pivot_index = randomized_partition(nums, left, right)
    
    if target_index == pivot_index:
        return nums[target_index]
    elif target_index < pivot_index:
        return quickselect(nums, left, pivot_index - 1, target_index)
    else:
        return quickselect(nums, pivot_index + 1, right, target_index)

def findKthSmallest(nums: List[int], k: int) -> int:
    """The k-th smallest element is at index k-1 in a sorted array."""
    if not 1 <= k <= len(nums):
        raise ValueError("k is out of bounds")
    return quickselect(nums, 0, len(nums) - 1, k - 1)

def findKthLargest(nums: List[int], k: int) -> int:
    """The k-th largest element is at index len(nums)-k in a sorted array."""
    if not 1 <= k <= len(nums):
        raise ValueError("k is out of bounds")
    return quickselect(nums, 0, len(nums) - 1, len(nums) - k)

def findMinMax(nums: List[int]) -> Tuple[int, int]:
    """
    Tournament method (Divide and Conquer) for Min-Max.
    Optimal for ADA labs: Takes ~3N/2 comparisons instead of 2N.
    """
    def get_min_max(left: int, right: int) -> Tuple[int, int]:
        # Base case: 1 element
        if left == right:
            return nums[left], nums[left]
            
        # Base case: 2 elements
        if right == left + 1:
            if nums[left] < nums[right]:
                return nums[left], nums[right]
            else:
                return nums[right], nums[left]
                
        # Recursive case
        mid = (left + right) // 2
        min1, max1 = get_min_max(left, mid)
        min2, max2 = get_min_max(mid + 1, right)
        
        return min(min1, min2), max(max1, max2)

    if not nums:
        raise ValueError("List cannot be empty")
    return get_min_max(0, len(nums) - 1)

if __name__ == "__main__":
    # Test array (will be modified in-place by quickselect)
    arr = [12, 3, 5, 7, 4, 19, 26, 21]
    k = 3
    
    print(f"Original Array elements: {arr}")
    
    # We pass a copy to avoid sorting the array prematurely for subsequent tests
    kth_smallest = findKthSmallest(arr.copy(), k)
    print(f"The {k}rd smallest element is: {kth_smallest}")
    
    kth_largest = findKthLargest(arr.copy(), k)
    print(f"The {k}rd largest element is: {kth_largest}")
    
    min_val, max_val = findMinMax(arr)
    print(f"Minimum: {min_val}, Maximum: {max_val}")