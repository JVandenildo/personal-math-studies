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
    print(f'Multiples of a: {multiplesA}.') # all multiples of a got for later comparison

    factor = 1 # factor gets here being bigger than 1, so we must reassign it to 1
    while multiplesB[len(multiplesB) - 1] < CommonMultiple:
        factor = factor + 1

        multipleB = b * factor
        multiplesB.append(multipleB)
    print(f'Multiples of b: {multiplesB}.') # all multiples of b got for later comparison
    
    # comparing multiples of each argument
    # an array may be bigger than the other, so to avoid error the 'if/else statement' comes
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

# for testing try those: 13, 7 (91); 92, 1024 (23552)
print(f'The least common multiple between {a} and {b} is {LeastCommonMultiple(a, b)}.')