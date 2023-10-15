#include <iostream>

std::string root(int base, int b)
{
    int r = 1;
    int p;
    int count;
    std::string answer;

    while (r != base)
    {
        p = r;
        count = 1;

        while (count < b)
        {
            p = p * r;
            count += 1;

            if (p == base && count == b)
            {
                answer = std::to_string(r);

                return answer;
            }
        }
        r = r + 1;
    }

    if (p == base && count == b)
    {
        return std::to_string(r);
    }
    else
    {
        return "not an integer";
    }
}

// int main()
// {
//     int base, b;
//     std::cout << "Base number: ";
//     std::cin >> base;
//     std::cout << "Root number: ";
//     std::cin >> b;

//     /*
//         some combinations doesn't return the correct result; be aware
//         for testing, try these combinations: 25, 5; 8, 3; 1728, 3 (is 12)
//     */
//     std::cout << "Root of " << base << " by " << b << " is " << root(base, b) << ".\n";

//     return 0;
// }