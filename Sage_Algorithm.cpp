#include<bits/stdc++.h>
using namespace std;

long long sage(long long x,long long n,long long m)
{
    long long y,u;
    y = 1;
    u = x%m;
    while(n>0)
    {
        if(n%2 == 1)
        {
            y = (y*u) % m;
        }
        if(n>0)
        {
            n = floor((long double)(n/2));
        }
        u = u*u % m;
    }
    return y;
}

int main()
{
    long long x,n,m,answer;
    cout << "Enter Values of x,n,m for finding 'x^n mod m' : ";
    cin >> x >> n >> m;
    answer = sage(x,n,m);
    cout << "Answer of x^n mod m is : " << answer;
    return 0;
}
