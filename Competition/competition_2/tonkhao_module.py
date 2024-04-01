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

Module owner: Tonkhao
"""
def find_connected(Graph):
    Group_id = {}
    Ans=[]
    for i,v in enumerate(Graph):
        for j,k in enumerate(Graph[i]):
            if Graph[i][j] in Group_id:
                Group_id[Graph[i][j]].append([i,j])
            else:
                Group_id[Graph[i][j]] = [[i,j]]

    for i in Group_id:
        Group=[[None]*len(Graph) for i in range(len(Graph[0]))]
        for j in Group_id[i]:
            Group[j[0]][j[1]] = i
        Ans.append(Group)
    return(Ans)
        


# G=[[1,2,2,2,1],
#    [1,3,3,2,1],
#    [1,1,3,2,1],
#    [3,3,3,2,1],
#    [3,3,3,1,1]]

# print(find_connected(G))