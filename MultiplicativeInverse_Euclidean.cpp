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

int MMI(long long a, long long b)
{
    long long t1,t2,r1,r2,q,r,t;
    // initialization
    r1=a;
    r2=b;
    t1=0;
    t2=1;
    while(r2 > 0)
    {
        q = r1/r2;
        // r update
        r = r1 - q*r2;
        r1 = r2;
        r2 = r;
        // t update
        t = t1 - q*t2;
        t1 = t2;
        t2 = t;
    }
    return t1;
}

int main()
{
    long long a,b,c,m,n,answer;
    cout << "Enter Two Numbers : " ;
    cin >> a >> b;
    c = gcd(a,b);
    m = a;
    n = b;
    if(c == 1)
    {
        answer = MMI(a,b);
        if(answer < 0)
        {
            cout << "Multiplicative Inverse of " << a << " is " << answer << " or " << answer+a << endl;
        }
    }
    else
    {
        cout << "Multiplicative Inverse of " << a << " doesn't Exist... " << endl;
    }
    return 0;
}
