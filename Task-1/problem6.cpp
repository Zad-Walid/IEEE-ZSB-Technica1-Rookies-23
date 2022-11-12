#include <iostream>

using namespace std;

int main()
{
    int a,b;
    cin>>a>>b;
    int g;
  if ( b > a) {
    int temp = b;
    b = a;
    a = temp;
  }
    for (int i = 1; i <=  b; i++) {
    if (a % i == 0 && b % i ==0) {
      g = i;
    }
  }
 cout<<g;
    return 0;
}
