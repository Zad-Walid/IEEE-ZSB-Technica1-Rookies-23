#include <iostream>

using namespace std;

int main()
{
  cout <<"enter number" <<endl;
  int n;
  cin>>n;
  int sum = 0;
  for(int i = 0 ; i<= n ; i++)
    sum += i;

  cout<<sum;
    return 0;
}
