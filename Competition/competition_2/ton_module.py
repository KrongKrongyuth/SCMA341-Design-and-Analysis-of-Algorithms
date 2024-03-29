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

    def find_connected(self, graph:list, current_index:list = [0,0], footprint:list = [], handle:str = ""):

        bound_condition = (0 <= current_index[0] < self.GRAPH_ROW) and (0 <= current_index[1] < self.GRAPH_COL) and (current_index not in footprint)
        # print(bound_condition)

        if bound_condition:
            ########## Recursion Algorithm ##########

            ########## BASED CASE ##########
            component = graph[current_index[0]][current_index[1]]
            print(component, current_index)
            print(footprint, len(footprint))
            if handle == "":
                handle = component
            
            if component == handle:
                self.RESULT[current_index[0]][current_index[1]] = handle
                footprint.append(current_index)
                # return True
            elif component != handle:
                """
                PUT SOME CODE HERE
                """
                footprint.append(current_index)
                return False
            ########## BASED CASE ##########

            ########## MOVE SET (4 Direction) ##########
            up = self.find_connected(graph, list(map(lambda x, y: x + y, current_index, self.direction[0])))
            down = self.find_connected(graph, list(map(lambda x, y: x + y, current_index, self.direction[1])))
            left = self.find_connected(graph, list(map(lambda x, y: x + y, current_index, self.direction[2])))
            right = self.find_connected(graph, list(map(lambda x, y: x + y, current_index, self.direction[3])))
            ########## MOVE SET (4 Direction) ##########

        # Iterative Algorithm
        # while bound_condition:
        #     # Algorithm
        #     break
        # return RESULT
        else:
            return False
        return self.RESULT