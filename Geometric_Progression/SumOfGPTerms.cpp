#include <iostream>
#include <math.h>

float SumOfTerms(float initialTerm, float constant, size_t n)
{
    return (initialTerm * (pow(constant, (n - 1 + 1)) - 1)) / (constant - 1);
}

int main()
{
    float initialTerm, constant;
    size_t n;
    std::cout << "Primeiro termo: ";
    std::cin >> initialTerm;
    std::cout << "Constante: ";
    std::cin >> constant;
    std::cout << "Numero de termos: ";
    std::cin >> n;

    std::cout << SumOfTerms(initialTerm, constant, n);

    return 0;
}