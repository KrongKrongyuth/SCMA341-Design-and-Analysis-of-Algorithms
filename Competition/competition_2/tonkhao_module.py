def find_connected(Graph):
    max_val = max(map(max, Graph))
    equivalent = {}
    Group_id = {}
    Ans = []
    Group = [None] * (len(Graph) * len(Graph[0]))  # Use 1D list for Group ID
    visited = set()  # Use set for visited values

    for i, row in enumerate(Graph):
        for j, val in enumerate(row):
            if val in Group_id:
                if i == 0:
                    if Graph[i][j-1] == val:
                        Group[i * len(Graph[0]) + j] = Group[(i * len(Graph[0])) + (j-1)]
                        Group_id[Group[i * len(Graph[0]) + j]].append([i, j])
                    else:
                        Group[i * len(Graph[0]) + j] = val + max_val + max(Group_id)
                        Group_id[Group[i * len(Graph[0]) + j]] = [[i, j]]
                        visited.add(val)
                elif j == 0:
                    if Graph[i-1][j] == val:
                        Group[i * len(Graph[0]) + j] = Group[(i-1) * len(Graph[0]) + j]
                        Group_id[Group[i * len(Graph[0]) + j]].append([i, j])
                    else:
                        Group[i * len(Graph[0]) + j] = val + max_val + max(Group_id)
                        Group_id[Group[i * len(Graph[0]) + j]] = [[i, j]]
                        visited.add(val)
                else:
                    if Graph[i][j-1] == val:
                        Group[i * len(Graph[0]) + j] = Group[i * len(Graph[0]) + (j-1)]
                        Group_id[Group[i * len(Graph[0]) + j]].append([i, j])
                        if Graph[i-1][j] == val and Group[i * len(Graph[0]) + j] not in equivalent:
                            equivalent[Group[i * len(Graph[0]) + j]] = Group[(i-1) * len(Graph[0]) + j]
                    elif Graph[i-1][j] == val:
                        Group[i * len(Graph[0]) + j] = Group[(i-1) * len(Graph[0]) + j]
                        Group_id[Group[i * len(Graph[0]) + j]].append([i, j])
                        if Graph[i][j-1] == val and Group[i * len(Graph[0]) + j] not in equivalent:
                            equivalent[Group[i * len(Graph[0]) + j]] = Group[i * len(Graph[0]) + (j-1)]
                    else:
                        Group[i * len(Graph[0]) + j] = val + max_val + max(Group_id)
                        Group_id[Group[i * len(Graph[0]) + j]] = [[i, j]]
                        visited.add(val)
            else:
                Group_id[val] = [[i, j]]
                Group[i * len(Graph[0]) + j] = val
                visited.add(val)

    for i in equivalent:
        Group_id[equivalent[i]] += Group_id[i]
        Group_id.pop(i)

    for i in Group_id:
        Group_Ans = [[None] * len(Graph[0]) for _ in range(len(Graph))]
        for j in Group_id[i]:
            Group_Ans[j[0]][j[1]] = Graph[j[0]][j[1]]
        Ans.append(Group_Ans)

    return Ans
