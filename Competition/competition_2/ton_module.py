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

class ConnectedComponent():
    def __init__(self, graph:list) -> None:
        self.graph = graph
        self.GRAPH_ROW, self.GRAPH_COL = len(graph), len(graph[0])
        self.RESULT = [[None for _ in range(self.GRAPH_COL)] for _ in range(self.GRAPH_ROW)]
        self.direction = [
                        (-1,  0),   # Up
                        ( 1,  0),   # Down
                        ( 0, -1),   # Left
                        ( 0,  1)    # Right
                        ]
        self.footprint = []
        self.family = [self.graph[0][0]]

    def find_connected(self, current_index:list = [0,0]):
        ########## Recursion Algorithm ##########
        component = self.graph[current_index[0]][current_index[1]]
        print(component)

        ########## BASED CASE ##########
        """
        PUT SOME CODE HERE
        STOP WHEN ALL PATH RETURN FALSE
        """
        ########## BASED CASE ##########
        
        ########## MOVE ##########
        if component == self.family[0]:
            self.footprint.append(current_index)
            self.RESULT[current_index[0]][current_index[1]] = component
            possible_move = []
            for direction in self.direction:
                filter_index =  list (
                                filter  (
                                    lambda x: 0 <= x[0] < self.GRAPH_ROW and 0 <= x[1] < self.GRAPH_COL and x not in self.footprint,
                                    [list(map(lambda x, y: x + y, current_index, direction))]
                                        )
                                    )
                if filter_index:
                    next_index = filter_index[0]
                    print(next_index)
                    possible_move.append(next_index)
                    next_componet = self.graph[next_index[0]][next_index[1]]
                    if next_componet == self.family[0]:
                        return self.find_connected(current_index = next_index)    # Fix this line
            return self.RESULT
        elif component != self.family[0]:
            self.footprint.append(current_index)
            if component not in self.family:
                self.family.append(component)
            return False
        ########## MOVE ##########
        ########## Recursion Algorithm ##########
        
        # ########## MOVE SET (4 Direction) ##########
        # up = self.find_connected(self.graph, list(map(lambda x, y: x + y, current_index, self.direction[0])), True)
        # down = self.find_connected(self.graph, list(map(lambda x, y: x + y, current_index, self.direction[1])), True)
        # left = self.find_connected(self.graph, list(map(lambda x, y: x + y, current_index, self.direction[2])), True)
        # right = self.find_connected(self.graph, list(map(lambda x, y: x + y, current_index, self.direction[3])), True)
        # ########## MOVE SET (4 Direction) ##########

        # Iterative Algorithm
        # while bound_condition:
        #     # Algorithm
        #     break
        # return RESULT
        # return self.RESULT