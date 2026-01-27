from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")



def bubble_sort(array):
    arr = len(array)

    for i in range(arr):
        already_sorted = True

        for e in range(arr - i - 1):
            if array[e] > array[e + 1]:
                array[e], array[e + 1] = array[e + 1], array[e]
                already_sorted = False

        if already_sorted:
            break
    
    return array


a = [4,1,2,56,6,12,33,5]

print(bubble_sort(a))
