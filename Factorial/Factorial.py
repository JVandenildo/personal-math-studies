number = int(input("Factorial of: "))

def factorial(number):
    i = 1
    result = 1

    while number >= i:
        result = result * i
        i += 1
    
    return result

print(f'The factorial of {number} is {factorial(number)}.')