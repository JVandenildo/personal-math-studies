def GreatestCommonDivisor(a, b):
    factor = 1

    DivisorsA = []
    while factor <= a:
        if a % factor == 0:
            DivisorA = a / factor
            DivisorsA.append(DivisorA)
        factor = factor + 1
    print(f'Divisors of a: {DivisorsA}.')
    
    factor = 1 # factor gets here being bigger than 1, so we must reassign it to 1
    DivisorsB = []
    while factor <= b:
        if b % factor == 0:
            DivisorB = b / factor
            DivisorsB.append(DivisorB)
        factor = factor + 1
    print(f'Divisors of b: {DivisorsB}.')

    # comparing divisors of each argument
    # an array may be bigger than the other, so to avoid error the 'if/else statement' comes
    if len(DivisorsB) <= len(DivisorsA):
        for i in DivisorsB:
            for e in DivisorsA:
                if i == e:
                    return i

    else:
        for i in DivisorsA:
            for e in DivisorsB:
                if i == e:
                    return i

a = int(input("a: "))
b = int(input("b: "))

print(f'The greatest common divisor of {a} and {b} is {GreatestCommonDivisor(a, b)}.')