#include <iostream>
using namespace std;

string root(int base, int b)
{
    int r = 1;
    int p;
    int count;
    string answer;

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
                answer = to_string(r);

                return answer;
            }
        }
        r = r + 1;
    }
    if (p == base && count == b)
    {
        answer = to_string(r);
    }
    else
    {
        answer = "not an integer";
    }

    return answer;
}

/*int main(){
    int base, b;
    cout << "Base number: ";
    cin >> base;
    cout << "Root number: ";
    cin >> b;

    // some combinations doesn't return the correct result; be aware
    // for testing, try these combinations: 25, 5; 8, 3; 1728, 3 (is 12)
    cout << "Root of " << base << " by " << b << " is " << root(base, b) << ".\n";

    return 0;
}*/