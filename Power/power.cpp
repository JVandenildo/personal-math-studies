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

/*int main()
{
    int a, n;
    std::cout << "Base: ";
    std::cin >> a;
    std::cout << "Exponent: ";
    std::cin >> n;

    std::cout << a << " raised to the power of " << n << " is " << power(a, n) << ".\n";

    return 0;
}*/