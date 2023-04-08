#include <iostream>
using namespace std;

int main(){
    int a;
    cout << "Base: ";
    cin >> a;
    int n;
    cout << "Exponent: ";
    cin >> n;
    int count = 1;
    int p = a;

    while (count < n) {
        p = p * a;
        count+=1;
    }
    cout << a << " raised to the power of " << n << " is " << p << ".\n";
    
    return 0;
}
