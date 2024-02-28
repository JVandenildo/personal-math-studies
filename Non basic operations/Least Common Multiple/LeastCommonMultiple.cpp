#include <iostream>
#include <vector>

int LeastCommonMultiple(int a, int b)
{
    int factorA = 1;
    int multipleA = a * factorA;
    std::vector<int> multiplesA = {multipleA};
    int multipleB = b * factorA;
    std::vector<int> multiplesB = {multipleB};

    int CommonMultiple = multipleA * multipleB;

    while (multiplesA[multiplesA.size() - 1] < CommonMultiple)
    {
        factorA = factorA + 1;
        multipleA = a * factorA;
        multiplesA.push_back(multipleA);
    }
    std::cout << "Size of A " << multiplesA.size() << std::endl;

    int factorB = 1; // factor gets here being bigger than 1, so we must reassign it
    while (multiplesB[multiplesB.size() - 1] < CommonMultiple)
    {
        factorB = factorB + 1;
        multipleB = b * factorB;
        multiplesB.push_back(multipleB);
    }
    std::cout << "Size of B " << multiplesB.size() << std::endl;

    /*
        comparing multiples of each argument
        an array may be bigger the other, so to avoid error the 'if/else statement' comes
    */
    if (multiplesB.size() <= multiplesB.size())
    {
        for (int i : multiplesB)
        {
            for (int e : multiplesA)
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
        for (int i : multiplesA)
        {
            for (int e : multiplesB)
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
    int a;
    std::cout << "A: ";
    std::cin >> a;
    int b;
    std::cout << "B: ";
    std::cin >> b;

    // for testing try those: 13, 7 (91)
    std::cout << LeastCommonMultiple(a, b);

    return 0;
}*/