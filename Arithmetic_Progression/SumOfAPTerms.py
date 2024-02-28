import random as rd


# function to generate list
def ArithmeticProgression(n, term, constant):
    listTerms = [term]

    while len(listTerms) < n:
        term = term + constant
        listTerms.append(term)

    return listTerms


# function to find sum
def SumOfTerms(n, array):
    print(f"List: {array};\nLength: {len(array)}.")

    # sum = 0
    # for i in array:
    #     sum = sum + i
    # print(f"Sum: {sum}!")

    sum = n * (array[0] + array[len(array) - 1]) / 2

    return sum


n = rd.randint(3, 50)  # number of terms
term = rd.randint(-50, 50)  # 1st term
constant = rd.randint(-50, 50)  # constant


lst = ArithmeticProgression(n, term, constant)

print(SumOfTerms(n, lst))
