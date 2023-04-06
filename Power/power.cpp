#include <iostream>
using namespace std;

int power(int a, int b){
    cout << "Base number: " << "\n";
    cin >> a;
    cout << "Power number: " << "\n";
    cin >> b;

    int count = 1;
    int p = a;

    while (count < b)
    {
        p = p * a;
        count+=1;
    }
    
    return p;
}

int main(){
    cout << power << ".\n";
    
    return 0;
}
