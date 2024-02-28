import random as rd


# function to generate list
def ArithmeticProgression(n, term, constant):
    listTerms = [term]

    while len(listTerms) < n:
        term = round(term * constant, 2)
        listTerms.append(term)

    return listTerms


# function to find sum
def SumOfTerms(array, term, constant, n):
    print(f"List: {array};\nLength: {n};\nConstant: {constant}.")

    # sum = 0
    # for i in array:
    #     sum = sum + i
    # return sum

    if constant > 1:
        return (term * ((constant**n) - 1)) / (constant - 1)
    else:
        return (term * (term - (constant**n))) / (1 - constant)


n = rd.randint(3, 50)  # number of terms
term = rd.randint(-50, 50)  # 1st term
constant = rd.randint(-50, 50)  # constant


lst = ArithmeticProgression(n, term, constant)

print(SumOfTerms(lst, term, constant, n))
