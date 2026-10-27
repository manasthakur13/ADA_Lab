import heapq
from typing import Dict, Optional

class Node:
    """Class to represent a node in the Huffman Tree."""
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

    def __lt__(self, other: 'Node'):
        """Less-than operator to allow heapq to compare nodes based on frequency."""
        return self.freq < other.freq

class HuffmanCoder:
    """Class to construct a Huffman Tree and generate binary character encodings."""
    def __init__(self):
        self.root: Optional[Node] = None
        self.codes: Dict[str, str] = {}

    def build_tree(self, frequencies: Dict[str, int]) -> Node:
        """
        Builds the Huffman tree from character frequencies using a min-heap 
        and returns the root node.
        """
        if not frequencies:
            raise ValueError("Frequency dictionary cannot be empty.")

        # Create a min-heap queue of leaf nodes
        heap = [Node(char, freq) for char, freq in frequencies.items()]
        heapq.heapify(heap)

        # Merge nodes until only the root remains
        while len(heap) > 1:
            left_node = heapq.heappop(heap)
            right_node = heapq.heappop(heap)

            # Create an internal node with the combined frequency of its children
            merged_node = Node(None, left_node.freq + right_node.freq)
            merged_node.left = left_node
            merged_node.right = right_node

            heapq.heappush(heap, merged_node)

        self.root = heap[0]
        return self.root

    def generate_codes(self) -> Dict[str, str]:
        """
        Traverses the constructed Huffman tree to generate binary encoding mappings.
        """
        if not self.root:
            return {}
        
        self.codes = {}
        # Edge case: If there is only one distinct character
        if self.root.left is None and self.root.right is None:
            self.codes[self.root.char] = "0"
        else:
            self._traverse_and_assign(self.root, "")
            
        return self.codes

    def _traverse_and_assign(self, node: Optional[Node], current_code: str):
        """Recursive helper function to assign '0' to left branches and '1' to right branches."""
        if node is None:
            return

        # If it's a leaf node, record the assigned binary code
        if node.char is not None:
            self.codes[node.char] = current_code
            return

        # Traverse left with '0' and right with '1'
        self._traverse_and_assign(node.left, current_code + "0")
        self._traverse_and_assign(node.right, current_code + "1")


# Example Usage:
if __name__ == "__main__":
    frequencies = {
        'A': 5,
        'B': 9,
        'C': 12,
        'D': 13,
        'E': 16,
        'F': 45
    }

    coder = HuffmanCoder()
    
    # Build the tree and get the root node
    root_node = coder.build_tree(frequencies)
    print(f"Tree built successfully. Root frequency total: {root_node.freq}")

    # Generate and print the binary encoding mappings
    huffman_codes = coder.generate_codes()
    print("\nGenerated Huffman Codes:")
    for char, code in sorted(huffman_codes.items()):
        print(f"Character '{char}': {code}")