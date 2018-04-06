#include<bits/stdc++.h>
using namespace std;
long long gcd(long long a,long long b)
{
    if(b == 0)
        return a;
    else
    {
        gcd(b,a%b);
    }
}
int main()
{
    long long a,b,answer;
    cout << "Enter two Numbers : ";
    cin >> a >> b;
    answer = gcd(a,b);
    cout << "The GCD of Two numbers " <<"("<<a<<"," << b << ") is : "<< answer;
    return 0;
}
