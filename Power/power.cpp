#include <iostream>

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

int powerRecursive(int a, int n)
{
    if (n == 0)
    {
        return 1;
    }
    else
    {
        return a * powerRecursive(a, n - 1);
    }
}

int main()
{
    int a, n;
    std::cout << "Base: ";
    std::cin >> a;
    std::cout << "Exponent: ";
    std::cin >> n;

    // comparing results
    std::cout << a << " raised to the power of " << n << " is " << power(a, n) << ". (NON RECURSIVE)\n";
    std::cout << a << " raised to the power of " << n << " is " << powerRecursive(a, n) << ". (RECURSIVE)\n";

    return 0;
}