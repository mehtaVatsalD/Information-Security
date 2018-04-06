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

long long fermat(long long a, long long b)
{
    long long n = b - 2,d;
    d = sage(a,n,b);
    return d;
}

int main()
{
    long long a,b,answer;
    cout << "Enter Integer and Prime Numbers : ";
    cin >> a >> b;
    answer = fermat(a,b);
    cout << "Inverse of " << a <<" is : " << answer;
    return 0;
}
