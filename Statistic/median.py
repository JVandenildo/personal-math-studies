# The median is the value separating the higher half from the lower half
# In case the set of values is in odd quantity it is the exact mid value
# In case the set of values is in even quantity it is the mean between the two values in the middle

import random as rd
import numpy as np


def medianOfLst(array: list) -> float:
    # j = 0
    # k = 0
    if len(array) % 2 == 0:  # array length is even
        # return array
        while len(array) > 2:
            array.remove(max(array))
            array.remove(min(array))

        return (array[0] + array[1]) / 2

    else:  # array length is odd
        # while j < len(array):
        #     k = array[j]

        #     if k < array[j] and k > array[j + 1]:
        #         array.remove(array[j])
        #         array.remove(array[j + 1])
        #     else:
        #         array.remove(k)
        #     j = j + 1

        # return k
        while len(array) > 1:
            array.remove(max(array))
            array.remove(min(array))

        return array[0]


lst = [rd.randint(1, 100) for i in range(rd.randint(5, 20))]

# result by numpy for comparison
print(f"List: {lst}\nNumpy median: {np.median(lst)}.")
# result by function
print(f"List: {lst};\nLength: {len(lst)};\nMedian: {medianOfLst(lst)}.")
