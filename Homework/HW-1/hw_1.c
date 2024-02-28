#include <stdio.h>
#include <math.h>

/*
********** Q1 **********
Quesion/Task -> Write the algorithm that can find largest and second largest.
*/

typedef int TestCase[10];
typedef struct
{
    int Max;
    int secondMax;
} TwoLargest; TwoLargest result;

TwoLargest find_two_largest(int[], int);
void print_array(int[], int);

int main(int argc, char const *argv[])
{
    TestCase example_case = {5, 32, 12, 93, 76, 82, 76, 65, 81, 32};

    int *pArray_size = NULL;    // Array size pointer
    int size = sizeof(example_case)/sizeof(example_case[0]);    // Calculate size of array

    pArray_size = &size;

    print_array(example_case, *pArray_size);
    find_two_largest(example_case, *pArray_size);
    printf("Max: %d\nSecond Max: %d", result.Max, result.secondMax);

    return 0;
}

void print_array(int array[], int size)
{
    printf("Test case: [");
    for (int i = 0; i < size; i++)
    {
        printf(" %d ", array[i]);
    }
    printf("]\n");
}

TwoLargest find_two_largest(int array[], int size)
{
    if (size == 0)
    {
        printf("Max: INVAID\nSecond Max: INVAID");
    }

    for (int i = 0; i < size; i++)
    {
        if (i == 0)
        {
            result.Max = array[i];
        }
        else if (result.Max < array[i])
        {
            result.Max = array[i];
        }
        else if (result.secondMax < array[i] && result.secondMax < result.Max)
        {
            result.secondMax = array[i];
        }
    }

    return result;
}

/*
********** Q2 **********
Quesion/Task -> Loop invariant that describes the fact about the two main variables.

Ans -> Loop invariant statement -> "result.Max and result.secondMax will store the Largest value and 2nd Largest value from the observed list. 
    -> Moreover, result.secondMax must always be less than result.Max (result.Max > result.secondMax).
*/

/*
********** Q3 **********
Quesion/Task -> Wrute tge statements that we need to prove in order to guarantee that the algorithm works by using math induction and loop invariant.

Ans -> When we need to prove the statements of loop invariant by using math induction we need to do 2 main steps.
    ->
    -> Basic step: To L.I. statement from Q2 when we start the first iteration before we observed the element from the list result.Max and result.secondMax
    -> will be "negative INFINITY" but after the first element from the list has been observed we will update the value of result.Max = FirstElement.
    -> Then L.I. still True (obvious!).
    ->
    -> Inductive step: In this step, we must prove the statement "L.I.(k) + action -> L.I.(k+1)", so we can do it by using a print statement within the loop
    -> to check the process while the loop is running. So the things that we need to print are result.Max, result.secondMax, and example_case.
*/
