def factorial(number):
    i = 1
    result = 1

    while number >= i:
        result = result * i
        i += 1

    return result


number = int(input("Factorial of: "))

print(f"The factorial of {number} is {factorial(number)}.")
