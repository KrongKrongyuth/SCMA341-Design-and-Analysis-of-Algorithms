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
        self.family = {}

    def find_connected(self, current_index:list = [0,0], FirstRound:bool = True) -> str:
        """
        This function will find the connected component in graph and print out the result.
        This algorithm is based on recursion structure.

        Args:
            current_index (list, optional): The place where the algorithm place. Defaults to [0,0].
            FirstRound (bool, optional): Detemine is the firstround or not?. Defaults to True.

        Returns:
            str: "Algorithm Finished"
        """
        ########## Recursive Algorithm ##########
        component = self.graph[current_index[0]][current_index[1]]
        if FirstRound:
            self.family[component] = current_index
        
        ########## MOVE ##########
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
                next_component = self.graph[next_index[0]][next_index[1]]
                if (self.family) and (next_component == list(self.family.keys())[0]):
                    possible_move.append(next_index)
                    self.find_connected(current_index = next_index, FirstRound = False)
                elif (self.family) and (next_component != list(self.family.keys())[0]) and (next_component not in self.family.keys()):
                    self.family[next_component] = next_index # We need to add same element
        ########## MOVE ##########
        
        ########## BASED CASE ##########
        if (not possible_move) and (self.family):
            self.family.pop(list(self.family.keys())[0])
            print(f"{self.RESULT}\n")
            self.RESULT = [[None for _ in range(self.GRAPH_COL)] for _ in range(self.GRAPH_ROW)]
        if not self.family:
            return "Algorithm Finished"
        ########## BASED CASE ##########
        ########## Recursive Algorithm ##########

    def find_connected(self, start_index = [0,0]):
        ########## Iterative Algorithm ##########
        component = self.graph[start_index[0]][start_index[1]]
        family = {component: start_index}
        family_keys = list(family.keys())
        
        for handle in family_keys:
            next_move = [family[handle]]
            footprint = [family[handle]]
            self.RESULT[family[handle][0]][family[handle][1]] = handle
            for move in next_move:
                current_index = move
                footprint.append(current_index)
                for direction in self.direction:
                    next_index = [current_index[0] + direction[0], current_index[1] + direction[1]]
                    if 0 <= next_index[0] < self.GRAPH_ROW and 0 <= next_index[1] < self.GRAPH_COL and next_index not in footprint:
                        next_component = self.graph[next_index[0]][next_index[1]]
                        if next_component == handle:
                            next_move.append(next_index)
                            self.RESULT[next_index[0]][next_index[1]] = next_component
                        elif (next_component != handle) and (next_component not in family.keys()):
                            family[next_component] = next_index
                            family_keys.append(next_component)
                        elif (next_component != handle) and (next_component in family.keys()):
                            """
                            PUT SOME CODE HERE
                            """
            print(self.RESULT)
            self.RESULT = [[None for _ in range(self.GRAPH_COL)] for _ in range(self.GRAPH_ROW)]

        return "\nAlgorithm Finished"
        ########## Iterative Algorithm ##########
