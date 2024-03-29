import random as rd
import numpy as np


def meanOfLst(array: list) -> float:
    sum = 0
    for i in array:
        sum = sum + i

    return round(sum / len(array), 2)


lst = [rd.randint(1, 100) for x in range(rd.randint(5, 15))]
print(f"List: {lst}\nLength: {len(lst)}.")

# result got by numpy
print(f"Numpy mean: {round(np.mean(lst), 2)}.")
# result got by function
print(f"Mean: {meanOfLst(lst)}.")
