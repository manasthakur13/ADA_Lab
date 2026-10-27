import random
from typing import Optional

def strStr(haystack: str, needle: str) -> int:
    """
    Finds the first occurrence of the string 'needle' in 'haystack' 
    using the Knuth-Morris-Pratt (KMP) string matching algorithm.
    
    Args:
        haystack (str): The text string to search within.
        needle (str): The pattern string to search for.
        
    Returns:
        int: The starting index of the first occurrence, or -1 if not found.
    """
    if not needle:
        return 0
        
    m, n = len(haystack), len(needle)
    
    # Step 1: Compute the Longest Prefix Suffix (LPS) array for the needle
    # lps[i] stores the length of the longest proper prefix which is also a suffix in needle[0..i]
    lps = [0] * n
    prev_lps, i = 0, 1
    
    while i < n:
        if needle[i] == needle[prev_lps]:
            lps[i] = prev_lps + 1
            prev_lps += 1
            i += 1
        elif prev_lps == 0:
            lps[i] = 0
            i += 1
        else:
            prev_lps = lps[prev_lps - 1]
            
    # Step 2: Use the LPS array to match the pattern in the haystack
    i = 0  # pointer for haystack
    j = 0  # pointer for needle
    
    while i < m:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                # Fall back using the LPS array to avoid redundant comparisons
                j = lps[j - 1]
                
        # If the entire needle is matched, return the starting index
        if j == n:
            return i - n
            
    return -1


class Randomizer:
    """
    A class to sample a random element from a continuous stream of data 
    with uniform probability using Reservoir Sampling.
    """
    def __init__(self):
        self.count = 0
        self.sampled_element: Optional[int] = None

    def process(self, value: int):
        """
        Processes a new incoming value from the stream and probabilistically 
        updates the chosen random sample.
        
        Args:
            value (int): The next element in the data stream.
        """
        self.count += 1
        
        # Keep the new value with a probability of 1/count.
        # This guarantees that at any point, every processed element 
        # has an equal probability (1/N) of being the chosen sample.
        if random.randint(1, self.count) == 1:
            self.sampled_element = value

    def getRandom(self) -> int:
        """
        Returns the currently sampled element from the stream.
        
        Returns:
            int: The randomly sampled element.
        """
        if self.count == 0:
            raise ValueError("No stream data has been processed yet.")
        return self.sampled_element


# Example Usage:
if __name__ == "__main__":
    # 1. KMP strStr Example
    text = "abxabcabcaby"
    pattern = "abcaby"
    index = strStr(text, pattern)
    
    print(f"Haystack: '{text}'")
    print(f"Needle: '{pattern}'")
    print(f"Pattern found at index: {index}")
    
    print("\n" + "-"*30 + "\n")
    
    # 2. Stream Sampling Example
    sampler = Randomizer()
    stream_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    print(f"Simulating a data stream: {stream_data}")
    
    # Process stream elements one by one
    for val in stream_data:
        sampler.process(val)
        
    # Get a uniformly random element from the stream processed so far
    print(f"Randomly sampled element from the stream: {sampler.getRandom()}")