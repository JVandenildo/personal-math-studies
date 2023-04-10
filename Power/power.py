def power(a, n):
    count = 1
    p = a

    while count < n:
        p = p * a
        count+=1
    
    return p

a = int(input("Base: "))
n = int(input("Exponent: "))

print(f'{a} raised to the power of {n} is {power(a, n)}.')