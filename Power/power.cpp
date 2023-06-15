#include <iostream>
using namespace std;

int power(int a, int n)
{
    int count = 1;
    int p = a;

    while (count < n)
    {
        p = p * a;
        count += 1;
    }

    return p;
}

/* int main(){
    int a, n;
    cout << "Base: ";
    cin >> a;
    cout << "Exponent: ";
    cin >> n;

    cout << a << " raised to the power of " << n << " is " << power(a, n) << ".\n";

    return 0;
} */