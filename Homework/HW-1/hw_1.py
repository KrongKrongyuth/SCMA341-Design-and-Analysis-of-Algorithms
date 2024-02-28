"""
Homework 1

********** Q1 **********
Quesion/Task -> Write the algorithm that can find largest and second largest.
"""

import numpy as np

def find_two_largest(array):
    """
    This function will find the Maximum and 2ndMaximum from the array.
    """
    max_so_far = second_max_so_far = -np.inf

    if len(array) == 0:
        return [max_so_far, second_max_so_far]

    for i, value in enumerate(array):
        if i == 0:
            max_so_far = value
        elif max_so_far < value:
            second_max_so_far, max_so_far = max_so_far, value
        elif second_max_so_far < value and second_max_so_far < max_so_far:
            second_max_so_far = value

    return [max_so_far, second_max_so_far]

if __name__ == "__main__":
    test_case = np.random.randint(100, size = 10)
    result = find_two_largest(test_case)

    print(f"Test case: {test_case}\nMax: {result[0]}\nSecond Max: {result[1]}")

"""
********** Q2 **********
Quesion/Task -> Loop invariant that describes the fact about the two main variables.

Ans -> Loop invariant statement -> "max_so_far and second_max_so_far will store the Largest value and 2nd Largest value from the observed list. 
    -> Moreover, second_max_so_far must always be less than max_so_far (max_so_far > second_max_so_far).
"""

"""
********** Q3 **********
Quesion/Task -> Wrute tge statements that we need to prove in order to guarantee that the algorithm works by using math induction and loop invariant.

Ans -> When we need to prove the statements of loop invariant by using math induction we need to do 2 main steps.
    ->
    -> Basic step: To L.I. statement from Q2 when we start the first iteration before we observed the element from the list max_so_far and second_max_so_far
    -> will be "negative INFINITY" but after the first element from the list has been observed we will update the value of max_so_far = FirstElement.
    -> Then L.I. still True (obvious!).
    ->
    -> Inductive step: In this step, we must prove the statement "L.I.(k) + action -> L.I.(k+1)", so we can do it by using a print statement within the loop
    -> to check the process while the loop is running. So the things that we need to print are max_so_far, second_max_so_far, and test_case.
"""
