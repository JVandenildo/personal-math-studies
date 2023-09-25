import random as rd


def meanOfLst(array):
    sum = 0
    for i in array:
        sum = sum + i

    return round(sum / len(array), 2)


lst = [rd.randint(1, 100) for x in range(rd.randint(5, 15))]

print(f"List: {lst};\nLength: {len(lst)};\nMean: {meanOfLst(lst)}.")
