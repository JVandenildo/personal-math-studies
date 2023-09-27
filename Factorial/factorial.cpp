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

/*int main()
{
    int number;
    std::cout << "Number: ";
    std::cin >> number;

    std::cout << "The factorial of " << number << " is " << factorial(number) << ".\n";

    return 0;
}*/