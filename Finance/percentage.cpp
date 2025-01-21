#include <iostream>

int main()
{
    float initialPrice = 10;
    float afterPrice = 15;
    float PriceDiff = afterPrice - initialPrice;

    float percentage = (abs(initialPrice - afterPrice) / initialPrice) * 100;

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
