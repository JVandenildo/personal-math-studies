def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


a = int(input("Base: "))
n = int(input("Exponent: "))

print(f"{a} raised to the power of {n} is {power(a, n)}.")
