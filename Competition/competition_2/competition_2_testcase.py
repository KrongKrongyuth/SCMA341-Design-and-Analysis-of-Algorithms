"""
(TEST FILE)
Compettion 2: Connected component algorithm.
"""

import matplotlib.pyplot as plt
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
    num_round = 10
    ton_runtime, tonkhao_runtime, tao_runtime, kanthong_runtime, = [], [], [], []
    for _ in range(num_round):
        start = process_time()
        cc.find_connected(start_index = [0,0])
        end = process_time()
        ton_runtime.append(end - start)
        
        start = process_time()
        cc.find_connected(start_index = [0,0])
        end = process_time()
        tao_runtime.append(end - start)
        
        start = process_time()
        cc.find_connected(start_index = [0,0])
        end = process_time()
        tonkhao_runtime.append(end - start)
        
        start = process_time()
        cc.find_connected(start_index = [0,0])
        end = process_time()
        kanthong_runtime.append(end - start)
    
    # Test result
    # print(cc.find_connected(start_index = [1,1])) # PASS
    # print(cc.find_connected(start_index = [0,0]))  # PASS
