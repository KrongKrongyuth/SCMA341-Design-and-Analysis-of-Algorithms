"""
(TEST FILE)
Compettion 2: Connected component algorithm.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import ton_module as ton
import tao_module as tao
import tonkhao_module as khao
from time import process_time, sleep

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
    num_round = 60
    ton_runtime, tonkhao_runtime, tao_runtime, kanthong_runtime = [], [], [], []
    for _ in range(num_round):
        ton_start = process_time()
        cc.find_connected(start_index = [0,0])
        ton_end = process_time()
        ton_runtime.append(ton_end - ton_start)
        
        tao_start = process_time()
        tao.find_connected(input_grid)
        tao_end = process_time()
        tao_runtime.append(tao_end - tao_start)
        
        khao_start = process_time()
        khao.find_connected(input_grid)
        khao_end = process_time()
        tonkhao_runtime.append(khao_end - khao_start)
        
        # start = process_time()
        # cc.find_connected(start_index = [0,0])
        # end = process_time()
        # kanthong_runtime.append(end - start)
        # sleep(5)

    fig, axs = plt.subplots(3,3)
    fig.suptitle('Algorithm runtime', fontsize = 20)
    axs[0, 0].plot(range(num_round), ton_runtime, marker = ".")
    axs[0, 0].set_title("Ton Runtime")
    axs[0, 1].plot(range(num_round), tao_runtime, marker = ".")
    axs[0, 1].set_title("Tao Runtime")
    axs[0, 2].plot(range(num_round), tonkhao_runtime, marker = ".")
    axs[0, 2].set_title("Tonkhao Runtime")
    
    sns.histplot(data = ton_runtime, ax = axs[1,0], kde = True)
    sns.histplot(data = tao_runtime, ax = axs[1,1], kde = True)
    sns.histplot(data = tonkhao_runtime, ax = axs[1,2], kde = True)
    
    sns.boxplot(x = ton_runtime, ax = axs[2,0])
    sns.boxplot(x = tao_runtime, ax = axs[2,1])
    sns.boxplot(x = tonkhao_runtime, ax = axs[2,2])
    
    plt.tight_layout()
    plt.show()
    
    fig = plt.figure()
    
    sns.lineplot(x = range(num_round), y = ton_runtime, label = "Ton")
    sns.lineplot(x = range(num_round), y = tao_runtime, label = "Tao")
    sns.lineplot(x = range(num_round), y = tonkhao_runtime, label = "Tonkhao")
    
    plt.show()
    
    print(tonkhao_runtime)
    
    # Test result
    # print(cc.find_connected(start_index = [1,1])) # PASS
    # print(cc.find_connected(start_index = [0,0]))  # PASS
