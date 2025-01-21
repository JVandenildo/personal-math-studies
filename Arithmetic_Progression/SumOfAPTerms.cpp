#include <iostream>
#include <vector>

int SumOfTerms(int n, std::vector<float> array)
{
    for (size_t i = 0; i < array.size(); i++)
    {
        std::cout << array[i];
        if (i < array.size() - 1)
        {
            std::cout << ", ";
        }
    }
    std::cout << "." << std::endl;

    int sum;
    /* sum = 0;
    for (int i : array)
    {
        sum = sum + i;
    } */
    sum = (n * (array[0] + array[n - 1])) / 2;

    return sum;
}

int main()
{
    std::cout << SumOfTerms(3, {10, 14, 18, 22});

    return 0;
}