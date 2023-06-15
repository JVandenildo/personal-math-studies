#include <iostream>
using namespace std;

int factorial(int number)
{
    int i = 1;
    int result = 1;

    while (number >= i)
    {
        result = result * i;
        i += 1;
    }

    return result;
}

/*int main(){
    int number;
    cout << "Number: ";
    cin >> number;

    cout << "The factorial of " << number << " is " << factorial(number) << ".\n";

    return 0;
}*/