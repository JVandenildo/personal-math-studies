#include <iostream>
#include <vector>

std::vector<float> GeometricProgression(float n, float term, float constant)
{
    std::vector<float> listTerms = {term};

    while (listTerms.size() < n)
    {
        term = term * constant;
        listTerms.push_back(term);
    }

    return listTerms;
}

int main()
{
    float n, term, constant;
    std::cout << "Number of terms: ";
    std::cin >> n;
    std::cout << "1st term: ";
    std::cin >> term;
    std::cout << "Constant: ";
    std::cin >> constant;

    std::vector<float> listTerms = GeometricProgression(n, term, constant);

    for (size_t i = 0; i < listTerms.size(); i++)
    {
        std::cout << listTerms[i];
        if (i < listTerms.size() - 1)
        {
            std::cout << ", ";
        }
    }
    std::cout << "." << std::endl;

    return 0;
}