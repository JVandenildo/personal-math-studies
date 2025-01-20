#include <iostream>
#include <vector>

std::vector<float> ArithmeticProgression(size_t n, float term, float constant)
{
    std::vector<float> listTerms = {term};

    while (listTerms.size() < n)
    {
        term = term + constant;
        listTerms.push_back(term);
    }

    return listTerms;
}

int main()
{
    size_t n;
    float term, constant;
    std::cout << "Number of terms: ";
    std::cin >> n;
    std::cout << "First term: ";
    std::cin >> term;
    std::cout << "Constant: ";
    std::cin >> constant;

    for (size_t i = 0; i < ArithmeticProgression(n, term, constant).size(); i++)
    {
        std::cout << ArithmeticProgression(n, term, constant)[i];
        if (i < ArithmeticProgression(n, term, constant).size() - 1)
        {
            std::cout << ", ";
        }
    }
    std::cout << "." << std::endl;

    return 0;
}