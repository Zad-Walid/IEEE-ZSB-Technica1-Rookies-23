#include <iostream>

using namespace std;

int sum(int l[] , int n){
        if (n <= 0) {
            return 0;
          }
     return sum (l , n-1) + l[n-1];
}

int main()
{
    int n;
    cin>>n;
    int l[n];
    int sum1 =0 ;
    int sum2 =0 ;
    int sum3 =0 ;

  for(int i = 0 ; i<n ; i++){
            cin >> l[i];}

  for(int i = 0 ; i<n ; i++){
            sum1 += l[i];}


    int j = 0;
    while(j<n){
    sum2 += l[j];
    j++;}


      cout<<sum1<<endl;
      cout<<sum2<<endl;
      sum3 = sum(l , n);
      cout<<sum3;



    return 0;
}
