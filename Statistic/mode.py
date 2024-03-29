# mode is the most repeating value in a set of data values

import random as rd
from scipy import stats


def checkMode(array: list) -> bool:
    """
    Verify if there's a mode.
    """
    countI = 0

    for i in array:
        countJ = 0

        for e in array:
            if i == e:
                countJ = countJ + 1
                # array.remove(e)
            if countI < countJ and countJ > 1:
                countI = countJ

    if countI == 0:
        return False
    else:
        return True


def modeOfLst(array: list) -> float:
    """
    Return the mode's value.
    """
    countI = 0
    modeNumber = 0

    for i in array:
        countJ = 0

        # print(i)
        for e in array:
            if i == e:
                countJ = countJ + 1
                # array.remove(e)
            if countI < countJ and countJ > 1:
                countI = countJ
                modeNumber = e

    return modeNumber


lst = [rd.randint(1, 100) for x in range(rd.randint(5, 15))]
print(f"List: {lst}\nLength: {len(lst)}.")

if checkMode(lst):
    # result got by scipy method
    print(f"Scipy mode: {stats.mode(lst)}.")

    # result by function
    print(f"List: {lst};\nLength: {len(lst)};\nMean: {modeOfLst(lst)}.")

else:
    # result got by scipy method
    print(f"Scipy mode: {stats.mode(lst)}.")

    # result by function
    print("There's no mode.")
