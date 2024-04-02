"""
Compettion 1: Longest common substring

Group member
    1. Krong        Krongyuth           6405009 (Submitter)
    2. Nattawat     Trisatheanpisan     6405025
    3. Shothibutr   Tansiri             6405203
    4. Phumioat     kamthong            6405310
"""

def main_algorithm(text_1:str, text_2:str) -> tuple:
    """_summary_
    This algorithm use concept of dynamic programming to find longest common substring.
    By create matrix that contain the number when found common substring.

    Args:
        text_1 (str): This variable contain first text. Defaults to None.
        text_2 (str): This variable contain secound text. Defaults to None.

    Returns:
        Case outside loop (Default):
        result (tuple): (-1, -1, 0)
        
        Case within loop:
        result (tuple): (text_1 starting index (i), text_2 starting index (j), substring length (k))

    """
    # Declear essential variable.
    text_1_size, text_2_size, result = len(text_1), len(text_2), (-1, -1, 0)

    # Declear empty/equal condition checking.
    empty_condition = ((text_1_size == 0) or (text_2_size == 0))
    equal_condition = (text_1 == text_2)

    if empty_condition:
        return result
    if equal_condition:
        result = (0, 0, text_1_size)
        return result

    # Declear intersection condition checking.
    intersect_condition = (len(set(text_1).intersection(set(text_2))) == 0)

    if intersect_condition:
        return result

    # Create matrix for making multiplication table.
    base_matrix = [[0] * text_1_size for _ in range(text_2_size)]

    # Loop.
    for row in range(len(base_matrix)):
        # print("[", end = " ")                                 # DEBUGING
        for col in range(len(base_matrix[0])):
            if text_1[col] == text_2[row] and (row == 0 or col == 0):
                base_matrix[row][col] += 1
            elif text_1[col] == text_2[row]:
                base_matrix[row][col] = base_matrix[row-1][col-1] + 1

            if base_matrix[row][col] > result[2]:
                k = base_matrix[row][col]
                i, j = col - k + 1, row - k + 1
                result = (i, j, k)
            # print(base_matrix[row][col], end = " ")           # DEBUGING
        # print("]",)                                           # DEBUGING
    return result
