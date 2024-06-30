def power(a: int, n: int):
    count = 1
    p = a

    while count < n:
        p = p * a
        count += 1

    return p


# recursive
def powerRecursive(a: int, n: int):
    if n == 0:
        return 1
    else:
        return a * powerRecursive(a, n - 1)


a = int(input("Base: "))
n = int(input("Exponent: "))

# comparing results
print(f"{a} raised to the power of {n} is {power(a, n)}. (NON RECURSIVE)\n")
print(f"{a} raised to the power of {n} is {powerRecursive(a, n)}. (RECURSIVE)\n")
# result with native python function
print(f"{a} raised to the power of {n} is {pow(a, n)}. (PYTHON)\n")
