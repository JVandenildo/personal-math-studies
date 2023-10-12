def factorial(number):
    i = 1
    result = 1

    while number >= i:
        result = result * i
        i += 1

    return result


# recursive
def factorialRecursive(number):
    if number == 0:
        return 1
    else:
        return number * factorialRecursive(number - 1)


number = int(input("Factorial of: "))

# comparing results
print(f"The factorial of {number} is {factorial(number)}. (NON RECURSIVE)")
print(f"The factorial of {number} is {factorialRecursive(number)}. (RECURSIVE)")
