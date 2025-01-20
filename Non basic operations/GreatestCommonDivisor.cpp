#include <iostream>
#include <vector>

int GreatestCommonDivisor(int a, int b)
{
    int factor = 1;

    std::vector<int> DivisorsA;
    int DivisorA;
    while (factor <= a)
    {
        if (a % factor == 0)
        {
            DivisorA = a / factor;
            DivisorsA.push_back(DivisorA);
        }
        factor = factor + 1;
    }
    std::cout << "Divisors of a: ";
    for (size_t i = 0; i < DivisorsA.size(); i++)
    {
        std::cout << DivisorsA[i];
        if (i < DivisorsA.size() - 1)
        {
            std::cout << ", ";
        }
    }
    std::cout << "." << std::endl;

    factor = 1; // factor gets here being bigger than 1, so we must reassign it to 1
    std::vector<int> DivisorsB;
    int DivisorB;
    while (factor <= b)
    {
        if (b % factor == 0)
        {
            DivisorB = b / factor;
            DivisorsB.push_back(DivisorB);
        }
        factor = factor + 1;
    }
    std::cout << "Divisors of b: ";
    for (size_t i = 0; i < DivisorsB.size(); i++)
    {
        std::cout << DivisorsB[i];
        if (i < DivisorsB.size() - 1)
        {
            std::cout << ", ";
        }
    }
    std::cout << "." << std::endl;

    /*
    comparing divisors of each argument
    an array may be bigger than the other, so to avoid error the 'if/else statement' comes
    */
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

    // in case no GDC is found
    return 0;
}

int main()
{
    int a, b;
    std::cout << "a: ";
    std::cin >> a;
    std::cout << "b: ";
    std::cin >> b;

    std::cout << GreatestCommonDivisor(a, b);

    return 0;
}