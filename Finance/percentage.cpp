#include <iostream>

int main()
{
    double initialPrice, finalPrice;
    std::cout << "Preço inicial: ";
    std::cin >> initialPrice;
    std::cout << "Preço final: ";
    std::cin >> finalPrice;
    double PriceDiff = finalPrice - initialPrice;

    double percentage = (abs(initialPrice - finalPrice) / initialPrice) * 100;

    if (PriceDiff > 0) // juros
    {
        std::cout << "Juros de ";
    }
    else if (PriceDiff < 0) // desconto
    {
        std::cout << "Desconto de ";
    }
    else // não houve alteração
    {
        std::cout << "Não houve alteração de preço!";
    }
    std::cout << percentage << "%." << std::endl;

    return 0;
}
