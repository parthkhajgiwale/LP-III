import heapq
from collections import Counter, defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for priority queue ordering
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # Calculate the frequency of each character in the text
    frequency = Counter(text)
    
    # Create a priority queue (min-heap) from the frequency dictionary
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Build the Huffman tree
    while len(heap) > 1:
        # Pop two nodes with the smallest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Merge nodes and push the combined node back into the heap
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    # The remaining node is the root of the Huffman tree
    return heap[0]

def build_codes(node, prefix="", code_map={}):
    if node is not None:
        # It's a leaf node; store the character and its code
        if node.char is not None:
            code_map[node.char] = prefix
        else:
            # Traverse left and right with added prefix
            build_codes(node.left, prefix + "0", code_map)
            build_codes(node.right, prefix + "1", code_map)
    return code_map

def huffman_encoding(text):
    if not text:
        return "", {}
    
    # Build Huffman Tree
    root = build_huffman_tree(text)
    
    # Generate the Huffman codes
    code_map = build_codes(root)
    
    # Encode the text
    encoded_text = ''.join(code_map[char] for char in text)
    return encoded_text, code_map

def huffman_decoding(encoded_text, code_map):
    # Reverse the code map to get character by code
    reverse_code_map = {v: k for k, v in code_map.items()}
    
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        # Decode character if code matches
        if current_code in reverse_code_map:
            decoded_text += reverse_code_map[current_code]
            current_code = ""
    return decoded_text

# Example Usage
if __name__ == "__main__":
    # Get user input for encoding
    text = input("Enter the text to encode: ")

    # Encoding
    encoded_text, code_map = huffman_encoding(text)
    print("\nEncoded Text:", encoded_text)
    print("Huffman Codes:", code_map)

    # Decoding
    decoded_text = huffman_decoding(encoded_text, code_map)
    print("\nDecoded Text:", decoded_text)
