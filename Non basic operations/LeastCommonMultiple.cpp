#include <iostream>
#include <vector>

int LeastCommonMultiple(int a, int b)
{
    int factor = 1;
    int multipleA = a * factor;
    std::vector<int> multiplesA = {multipleA};
    int multipleB = b * factor;
    std::vector<int> multiplesB = {multipleB};

    int CommonMultiple = multipleA * multipleB;

    while (multiplesA[multiplesA.size() - 1] <= CommonMultiple)
    {
        factor = factor + 1;

        multipleA = a * factor;
        multiplesA.push_back(multipleA);
    }
    std::cout << "Multiples of a: ";
    for (size_t i = 0; i < multiplesA.size(); i++)
    {
        std::cout << multiplesA[i];
        if (i < multiplesA.size() - 1)
        {
            std::cout << ", ";
        }
    }
    std::cout << "." << std::endl;

    factor = 1; // factor gets here being bigger than 1, so we must reassign it to 1
    while (multiplesB[multiplesB.size() - 1] <= CommonMultiple)
    {
        factor = factor + 1;

        multipleB = b * factor;
        multiplesB.push_back(multipleB);
    }
    std::cout << "Multiples of b: ";
    for (size_t i = 0; i < multiplesB.size(); i++)
    {
        std::cout << multiplesB[i];
        if (i < multiplesB.size() - 1)
        {
            std::cout << ", ";
        }
    }
    std::cout << "." << std::endl;

    /*
    comparing multiples of each argument
    an array may be bigger than the other, so to avoid error the 'if/else statement' comes
    */
    if (multiplesB.size() <= multiplesA.size())
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

    // in case not found
    return 0;
}

int main()
{

    int a, b;
    std::cout << "a: ";
    std::cin >> a;
    std::cout << "b: ";
    std::cin >> b;

    std::cout << LeastCommonMultiple(a, b) << std::endl;

    return 0;
}