#include <iostream>
#include <vector>

int GreatestCommonDivisor(int a, int b)
{
    int factorA = 1;
    std::vector<int> DivisorsA;
    while (factorA <= a)
    {
        if (a % factorA == 0)
        {
            int DivisorA = a / factorA;
            DivisorsA.push_back(DivisorA);
        }
        factorA = factorA + 1;
    }

    int factorB = 1;
    std::vector<int> DivisorsB;
    while (factorB <= b)
    {
        if (b % factorB == 0)
        {
            int DivisorB = b / factorB;
            DivisorsB.push_back(DivisorB);
        }
        factorB = factorB + 1;
    }

    /* Comparing divisors of each argument
    an array may be bigger than the other, so to avoid error the 'if/else statement' comes */
    if (DivisorsB.size() <= DivisorsA.size())
    {
        for (int i : DivisorsB)
        {
            for (int e : DivisorsA)
            {
                if (i == e)
                {
                    return i;
                }
            }
        }
    }
    else
    {
        for (int i : DivisorsA)
        {
            for (int e : DivisorsB)
            {
                if (i == e)
                {
                    return i;
                }
            }
        }
    }
}

/*int main()
{
    int a, b;
    std::cout << "a: ";
    std::cin >> a;
    std::cout << "b: ";
    std::cin >> b;

    // for testing use those: 8, 12 (4); 13, 7 (1)
    std::cout << "The greatest common divisor of " << a << " and " << b << " is " << GreatestCommonDivisor(a, b) << ".\n";

    return 0;
}*/