#include <iostream>
#include <math.h>

int power(int a, int n)
{
    int count = 1;
    int p = a;

    while (count < n)
    {
        p = p * a;
        count += 1;
    }

    return p;
}

int recursivePower(int a, int n)
{
    if (n == 0)
    {
        return 1;
    }
    else
    {
        return a * recursivePower(a, n - 1);
    }
}

int main()
{
    int a, n;
    std::cout << "Base: ";
    std::cin >> a;
    std::cout << "Exponent: ";
    std::cin >> n;

    std::cout << power(a, n) << " (NON RECURSIVE)" << std::endl;
    std::cout << recursivePower(a, n) << " (RECURSIVE)" << std::endl;
    std::cout << pow(a, n) << " (C++)" << std::endl;

    return 0;
}