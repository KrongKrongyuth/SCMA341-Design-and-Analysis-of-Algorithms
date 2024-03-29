"""
(TEST FILE)
Compettion 2: Connected component algorithm.
"""

from ton_module import *
from time import process_time

TEST_CASE = {"case_1": [[[1, 2, 2, 2, 1],
                        [ 1, 3, 3, 2, 1],
                        [ 1, 1, 3, 2, 1],
                        [ 3, 3, 3, 2, 1],
                        [ 3, 3, 3, 1, 1]],

                        [[1,   None, None, None, None],
                        [ 1,   None, None, None, None],
                        [ 1,    1,   None, None, None],
                        [None, None, None, None, None],
                        [None, None, None, None, None]],

                        [[None,  2,    2,    2,   None],
                        [None,  None, None,  2,   None],
                        [None,  None, None,  2,   None],
                        [None,  None, None,  2,   None],
                        [None,  None, None, None, None]],

                        [[None, None, None, None, None],
                        [None,   3,    3,   None, None],
                        [None,  None,  3,   None, None],
                        [ 3,     3,    3,   None, None],
                        [ 3,     3,   None, None, None]],

                        [[None, None, None,  None,  1 ],
                        [None,  None, None,  None,  1 ],
                        [None,  None, None,  None,  1 ],
                        [None,  None, None,  None,  1 ],
                        [None,  None, None,   1,    1 ]]]}

if __name__ == "__main__":
    print(ConnectedComponent(TEST_CASE["case_1"][0]).find_connected(TEST_CASE["case_1"][0]))
    # print(list(map(lambda x,y: x + y, [1,2], [3, 4])))
    # TEST_CASE["case_1"][0][0][1] = 5
    # print(TEST_CASE["case_1"][0][0][1])
