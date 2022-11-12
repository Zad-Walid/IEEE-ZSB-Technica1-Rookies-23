#include <iostream>

using namespace std;

int main()
{
    cout << "please, enter number"<<endl;
    int n;
    cin >> n;
    long long f = 1;
    for(int i = 1 ; i<=n ; i++){
        f *= i;
    }
    cout << f;
    return 0;
}
