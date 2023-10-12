#include <iostream>

int factorial(int number)
{
    int i = 1;
    int result = 1;

    while (number >= i)
    {
        result = result * i;
        i += 1;
    }

    return result;
}

int factorialRecursive(int number)
{
    if (number == 0)
    {
        return 1;
    }
    else
    {
        return number * factorial(number - 1);
    }
}

int main()
{
    int number;
    std::cout << "Factorial of: ";
    std::cin >> number;

    // comparing results
    std::cout << "The factorial of " << number << " is " << factorial(number) << ". (NON RECURSIVE)\n";
    std::cout << "The factorial of " << number << " is " << factorialRecursive(number) << ". (RECURSIVE)\n";

    return 0;
}