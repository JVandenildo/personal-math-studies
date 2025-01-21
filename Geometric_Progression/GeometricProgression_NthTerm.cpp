#include <iostream>
#include <vector>

std::vector<float> GeometricProgression_NthTerm(float iTerm, float fTerm, float constant)
{
    std::vector<float> listTerms;

    if (constant < 1 && iTerm > fTerm)
    {
        while (iTerm >= fTerm)
        {
            listTerms.push_back(iTerm);
            iTerm = iTerm * constant;
        }
    }
    else if (constant >= 1 && iTerm < fTerm)
    {
        while (iTerm < fTerm)
        {
            listTerms.push_back(iTerm);
            iTerm = iTerm * constant;
        }
    }
    else
    {
        return listTerms;
    }

    return listTerms;
}

int main()
{
    float initialTerm, finalTerm, constant;

    std::cout << "First term: ";
    std::cin >> initialTerm;
    std::cout << "Last term: ";
    std::cin >> finalTerm;
    std::cout << "Constant: ";
    std::cin >> constant;

    std::vector<float> listTerms = GeometricProgression_NthTerm(initialTerm, finalTerm, constant);
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