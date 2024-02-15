"""
This file use for test the algorithm correctness.
"""

import subprocess
from competition_1_logestsubstring import Competition
from time import process_time

def messure_time(start, end):
    """_summary_

    Args:
        start (float): Start time from time.process_time()
        end (float): End time from time.process_time()

    Returns:
        float: Algorithm execution time.
    """
    print(f"CPU Execution time is {end - start} secounds")
    return end - start

if __name__ == "__main__":
    test_case = {"case1" : ["parachute",        "shuttle",          (5, 1, 3)],
                "case2" :  ["programming",      "program",          (0, 0, 7)],
                "case3" :  ["abcdef",           "12345",            (-1, -1, 0)],
                "case4" :  ["abcd",             "abcd",             (0, 0, 4)],
                "case5" :  ["abcd",             "wxyz",             (-1, -1, 0)],
                "case6" :  ["",                 "",                 (-1, -1, 0)],
                "case7" :  ["abcdefg",          "bcdefgh",          (1, 0, 6)],
                "case8" :  ["apple",            "olymppus",         (1, 4, 2)],
                "case9" :  ["abracadabra",      "cadabraabra",      (4, 0, 7)],
                "case10":  ["a",                "bcdaet",           (0, 3, 1)],
                "case11":  ["",                 "bcdaet",           (-1, -1, 0)]}
    subprocess.run(["clear"])                                                   # Clear terminal before checking.

    # Algorithm checking...
    for case in test_case.keys():

        method = Competition(text_1=test_case[case][0],text_2=test_case[case][1])

        print(f"\n{case} is running...")
        start_time = process_time()                                             # Store the start of running time.
        result = method.ton_algorithm()                                         # Change the method here.
        end_time = process_time()                                               # Store the end of running time.
        print(f"{case} status: {result == test_case[case][2]}")
        messure_time(start_time, end_time)
        print("************************************************************")
