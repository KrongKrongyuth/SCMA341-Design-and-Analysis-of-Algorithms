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

# grid2 = [
#     [1, 2, 2, 2, 1],
#     [1, 3, 3, 2, 1],
#     [1, 1, 3, 2, 1],
#     [3, 3, 3, 2, 1],
#     [3, 3, 3, 1, 1]
# ]





# find_connected(grid2)

