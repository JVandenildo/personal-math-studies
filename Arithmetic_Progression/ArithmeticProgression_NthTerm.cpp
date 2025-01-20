#include <iostream>
#include <vector>

std::vector<int> ArithmeticProgression(float iTerm, float fTerm, float constant)
{
    std::vector<int> listTerms;

    if (constant < 1 && iTerm > fTerm)
    {
        while (iTerm >= fTerm)
        {
            listTerms.push_back(iTerm);
            iTerm = iTerm + constant;
        }
    }
    else if (constant >= 1 && iTerm < fTerm)
    {
        while (iTerm <= fTerm)
        {
            listTerms.push_back(iTerm);
            iTerm = iTerm + constant;
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
    std::cout << "Last term: "; // depending on the constant may not be the last term
    std::cin >> finalTerm;
    std::cout << "Constant: ";
    std::cin >> constant;

    for (size_t i = 0; i < ArithmeticProgression(initialTerm, finalTerm, constant).size(); i++)
    {
        std::cout << ArithmeticProgression(initialTerm, finalTerm, constant)[i];
        if (i < ArithmeticProgression(initialTerm, finalTerm, constant).size() - 1)
        {
            std::cout << ", ";
        }
    }
    std::cout << ". " << std::endl;
    std::cout << ArithmeticProgression(initialTerm, finalTerm, constant).size() << " terms." << std::endl;

    return 0;
}