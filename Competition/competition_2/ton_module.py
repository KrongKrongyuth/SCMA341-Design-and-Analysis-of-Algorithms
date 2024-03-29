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

Module owner: Ton
"""

def find_connected(graph:list, current_index:list = [0,0], footprint:list = [], handle:str = ""):
    GRAPH_ROW, GRAPH_COL = len(graph), len(graph[0])
    RESULT = [[None for _ in range(GRAPH_COL)] for _ in range(GRAPH_ROW)]

    moving_direction = [(-1,  0),   # Up
                        ( 1,  0),   # Down
                        ( 0, -1),   # Left
                        ( 0,  1)]   # Right
    bound_condition = (0 <= current_index[0] < GRAPH_ROW) and (0 <= current_index[1] < GRAPH_COL)

    # Recursion Algorithm
    # print(graph[current_index[0]][current_index[1]])
    if bound_condition:
        ########## BASED CASE ##########
        component = graph[current_index[0]][current_index[1]]
        
        if component == handle:
            pass
        # print(component, previous, current_index[0], current_index[1])
        ########## BASED CASE ##########

        # print(list(map(lambda x, y: x + y, current_index, moving_direction[0])),
            #   list(map(lambda x, y: x + y, current_index, moving_direction[1])),
            #   list(map(lambda x, y: x + y, current_index, moving_direction[2])),
            #   list(map(lambda x, y: x + y, current_index, moving_direction[3])),
            #   current_index,
            #   moving_direction[0],
            #   sep = "\t")

        ########## MOVE SET (4 Direction) ##########
        # up = find_connected(graph, list(map(lambda x, y: x + y, current_index, moving_direction[0])))
        # down = find_connected(graph, list(map(lambda x, y: x + y, current_index, moving_direction[1])))
        # left = find_connected(graph, list(map(lambda x, y: x + y, current_index, moving_direction[2])))
        # right = find_connected(graph, list(map(lambda x, y: x + y, current_index, moving_direction[3])))
        ########## MOVE SET (4 Direction) ##########

    # Iterative Algorithm
    # while bound_condition:
    #     # Algorithm
    #     break
    # return RESULT
