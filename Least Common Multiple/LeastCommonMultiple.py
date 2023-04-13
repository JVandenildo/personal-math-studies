def LeastCommonMultiple(a, b):
    factor = 1
    multipleA = a * factor
    multiplesA = [multipleA]
    multipleB = b * factor
    multiplesB = [multipleB]

    CommonMultiple = multipleA * multipleB

    while multiplesA[len(multiplesA) - 1] < CommonMultiple:
        factor = factor + 1

        multipleA = a * factor
        multiplesA.append(multipleA)
    print(f'Multiples of a: {multiplesA}.')
    factor = 1 # factor gets here being bigger than 1, so we must reassign it to 1
    while multiplesB[len(multiplesB) - 1] < CommonMultiple:
        factor = factor + 1

        multipleB = b * factor
        multiplesB.append(multipleB)
    print(f'Multiples of b: {multiplesB}.')
    
    if len(multiplesB) <= len(multiplesA):
        for i in multiplesB:
            for e in multiplesA:
                if i == e:
                    return i

    else:
        for i in multiplesA:
            for e in multiplesB:
                if i == e:
                    return i

a = int(input("a: "))
b = int(input("b: "))

print(LeastCommonMultiple(a, b))