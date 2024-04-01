"""
(TEST FILE)
Compettion 2: Connected component algorithm.
"""

from ton_module import *
from time import process_time

TEST_CASE = {"case_1": [[[1, 2, 2, 2, 4],
                        [ 1, 3, 3, 2, 4],
                        [ 1, 1, 3, 2, 4],
                        [ 3, 3, 3, 2, 4],
                        [ 3, 3, 3, 4, 4]],

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
                        [ 3,     3,    3,   None, None]],

                        [[None, None, None,  None,  1 ],
                        [None,  None, None,  None,  1 ],
                        [None,  None, None,  None,  1 ],
                        [None,  None, None,  None,  1 ],
                        [None,  None, None,   1,    1 ]]]}

if __name__ == "__main__":
    cc = ConnectedComponent(TEST_CASE["case_1"][0])
    # Run time test
    # start = process_time()
    # cc.find_connected(current_index = [0,0])
    # end = process_time()
    # print(end - start)
    
    # Test result
    # print(cc.find_connected(current_index = [1,1])) # ERROR
    print(cc.find_connected())  # PASS
    
    # Other
    # print(list(filter(lambda x: 0 <= x[0] < 5 and 0 <= x[1] < 5, [list(map(lambda x,y: x + y, [3,3], [1, 1]))])))
    # TEST_CASE["case_1"][0][0][1] = 5
    # print(TEST_CASE["case_1"][0][0][1])
    # table = {1: [1,2], 2: [2,3]}
    # print(3 in table.keys())
    # dict_test = {1: [1,2], 2: [2,3]}
    # print(dict_test.pop(1), dict_test)
