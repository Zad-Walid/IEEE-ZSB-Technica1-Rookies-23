#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
   int n1 = n;
    int reversed = 0 ;
    int rem = 0;
    while(n!=0)
  {
     rem = n%10;
     reversed = reversed*10 + rem;
     n/=10;
  }
  cout<< reversed <<endl ;
  if(n1 == reversed)
    cout<<"True";
  else
    cout<<"false";
    return 0;
}
