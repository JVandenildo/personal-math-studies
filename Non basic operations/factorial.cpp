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

// recursive
int factorialRecursive(int number)
{
    if (number == 0)
    {
        return 1;
    }
    else
    {
        return number * factorialRecursive(number - 1);
    }
}

int main()
{
    int number;
    std::cout << "Factorial of: ";
    std::cin >> number;

    std::cout << number << "! = " << factorial(number) << " (NON RECURSIVE)" << std::endl;
    std::cout << number << "! = " << factorialRecursive(number) << " (RECURSIVE)" << std::endl;

    return 0;
}