#include <iostream>
using namespace std;

int root(int base, int b){
    int r = 1;

    while(r != base){
        int p = r;
        int count = 1;

        while(count < b){
            p = p * r;
            count += 1;
            if(p == base){
                return r;
            }
        }

        if(r == base){
            return r;
        }
        else{
            r = r + 1;
        }
    }

    return r;
}

int main(){
    int base, b;
    cout << "Base number: ";
    cin >> base;
    cout << "Root number: ";
    cin >> b;

    // some combinations doesn't return the correct result; be aware
    cout << "Root of " << base << " by " << b << " is " << root(base, b) << ".\n";

    return 0;
}