import random as rd
from scipy import stats


def checkMode(array):
    countI = 0

    for i in array:
        countJ = 0

        # print(i)
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


def modeOfLst(array):
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

if checkMode(lst):
    # result by function
    print(f"List: {lst};\nLength: {len(lst)};\nMean: {modeOfLst(lst)}.")

    # result by scipy method for comparison
    print(f"Scipy median: {stats.mode(lst)}.")
else:
    print("There's no mode.")
