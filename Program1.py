from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        # Standard mid calculation to avoid overflow in fixed-width languages
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1


def myPow(x: float, n: int) -> float:
    # Handle negative powers: x^(-n) = (1/x)^n
    if n < 0:
        x = 1.0 / x
        n = -n
        
    result = 1.0
    current_product = x
    
    # Binary exponentiation (O(log n))
    while n > 0:
        if n % 2 == 1:
            result *= current_product
        
        current_product *= current_product
        n //= 2
        
    return result


if __name__ == "__main__":
    # Test search
    print(search([-1, 0, 3, 5, 9, 12], 9))  # 4
    print(search([-1, 0, 3, 5, 9, 12], 2))  # -1

    # Test myPow
    print(myPow(2.0, 10))   # 1024.0
    print(myPow(2.0, -2))   # 0.25