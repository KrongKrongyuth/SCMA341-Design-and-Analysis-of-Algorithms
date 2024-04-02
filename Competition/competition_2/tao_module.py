"""
Compettion 2: Connected component algorithm.

Group member
    1. Krong        Krongyuth           6405009 (Submitter)
    2. Nattawat     Trisatheanpisan     6405025
    3. Shothibutr   Tansiri             6405203
    4. Phumioat     kamthong            6405310

Instructions
    •Find connected component in an image.
    •Given an array of integers (any size), find all connected components
    (pixels with the same value as the adjacent pixel).
    •Return list of arrays that separate each component apart in its own array.
    •Make it runs as fast as possible.

    •Submit in MS teams before 23.59 of April 2nd.
    •Speed test in class of April 4th

Module owner: Tao
"""

def dfs(grid, row, col, component, visited, target):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or visited[row][col] or grid[row][col] != target:
        return
    visited[row][col] = True
    component.append((row, col))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    for dr, dc in directions:
        dfs(grid, row + dr, col + dc, component, visited, target)

def find_connected_components(grid):
    if not grid:
        return []
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    components = []
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                component = []
                dfs(grid, i, j, component, visited, grid[i][j])
                if component:  # Only append non-empty components
                    components.append((grid[i][j], component))
    return components

def print_grid(grid):
    for row in grid:
        print(row)

def create_component_grid(component, number, size):
    component_grid = [['None'] * size for _ in range(size)]
    for row, col in component:
        component_grid[row][col] = number
    return component_grid



def find_connected(grid):
    print("Connected Components:")
    connected_components = find_connected_components(grid)
    for component in connected_components:
        number, indices = component
        component_grid = create_component_grid(indices, number, len(grid))
        print("Number:", number)
        print_grid(component_grid)
        print()

# How to use
# You need to use function call find_connected(input_grid) to get the answer
# Ex. find_connected(example_grid)
