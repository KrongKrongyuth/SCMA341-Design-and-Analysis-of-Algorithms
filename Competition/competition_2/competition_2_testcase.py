"""
(TEST FILE)
Compettion 2: Connected component algorithm.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import ton_module as ton
import tao_module as tao
import tonkhao_module as khao
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
    input_grid = TEST_CASE["case_1"][0]
    cc = ton.ConnectedComponent(input_grid)
    
    # Run time test
    num_round = 50
    ton_runtime, tonkhao_runtime, tao_runtime, kanthong_runtime = [], [], [], []
    for _ in range(num_round):
        start = process_time()
        cc.find_connected(start_index = [0,0])
        end = process_time()
        ton_runtime.append(end - start)
        
        start = process_time()
        tao.find_connected(input_grid)
        end = process_time()
        tao_runtime.append(end - start)
        
        start = process_time()
        khao.find_connected(input_grid)
        end = process_time()
        tonkhao_runtime.append(end - start)
        
        # start = process_time()
        # cc.find_connected(start_index = [0,0])
        # end = process_time()
        # kanthong_runtime.append(end - start)

    fig, axs = plt.subplots(2,3)
    fig.suptitle('Algorithm runtime')
    axs[0, 0].plot(range(num_round), ton_runtime)
    axs[0, 0].set_title("Ton Runtime")
    axs[0, 1].plot(range(num_round), tao_runtime)
    axs[0, 1].set_title("Tao Runtime")
    axs[0, 2].plot(range(num_round), tonkhao_runtime)
    axs[0, 2].set_title("Tonkhao Runtime")
    
    sns.histplot(data = ton_runtime, ax = axs[1,0], kde = True)
    sns.histplot(data = tao_runtime, ax = axs[1,1], kde = True)
    sns.histplot(data = tonkhao_runtime, ax = axs[1,2], kde = True)
    plt.tight_layout()
    plt.show()
    
    # Test result
    # print(cc.find_connected(start_index = [1,1])) # PASS
    # print(cc.find_connected(start_index = [0,0]))  # PASS
