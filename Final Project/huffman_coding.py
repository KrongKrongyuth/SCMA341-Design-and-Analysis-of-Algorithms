import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    freq_counter = Counter(data)
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_counter.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)

        merged_freq = left_node.freq + right_node.freq
        merged_node = HuffmanNode(None, merged_freq)
        merged_node.left = left_node
        merged_node.right = right_node

        heapq.heappush(priority_queue, merged_node)

    return heapq.heappop(priority_queue)

def build_huffman_codes(node, current_code, huffman_codes):
    if node.char:
        huffman_codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + "0", huffman_codes)
    build_huffman_codes(node.right, current_code + "1", huffman_codes)

def compress(data):
    huffman_tree = build_huffman_tree(data)
    huffman_codes = {}
    build_huffman_codes(huffman_tree, "", huffman_codes)

    compressed_data = ""
    for char in data:
        compressed_data += huffman_codes[char]

    return compressed_data

def decompress(compressed_data, huffman_tree):
    decompressed_data = ""
    current_node = huffman_tree

    for bit in compressed_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decompressed_data += current_node.char
            current_node = huffman_tree

    return decompressed_data

# Example usage
data = "Hello world!"
compressed_data = compress(data)
print("Compressed data:", compressed_data)

decompressed_data = decompress(compressed_data, build_huffman_tree(data))
print("Decompressed data:", decompressed_data)
