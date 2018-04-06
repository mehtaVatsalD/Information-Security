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

cremainder(int a1, int b1,int a2, int b2,int a3, int b3)
{
    long long b = b1*b2*b3;
    long long B1,B2,B3,c1,c2,c3;
    B1 = b/b1;
    B2 = b/b2;
    B3 = b/b3;
    c1 = MMI(b1,B1);
    c2 = MMI(b2,B2);
    c3 = MMI(b3,B3);
    //cout << B1 <<" "<< B2  <<" " << B3 << endl;
    //cout << c1 <<" "<< c2  <<" " << c3 << endl;
    if(c1 < 0)
    {
        c1 = c1+b1;
    }
    else if(c2 < 0)
    {
        c2 = c2+b2;
    }
    else if(c3 < 0)
    {
        c3 = c3+b3;
    }
    return (a1*B1*c1 + a2*B2*c2 + a3*B3*c3) % b;
}
int main()
{
    int x,a1,b1,a2,b2,a3,b3,g1,g2,g3;
    cout << "Enter 3 pairs : "<< endl;
    cin >> a1 >> b1;
    cin >> a2 >> b2;
    cin >> a3 >> b3;
    g1 = gcd(b1,b2);
    g2 = gcd(b2,b3);
    g3 = gcd(b3,b1);
    //cout << b1 <<" "<< b2  <<" " << b3 << endl;
    if(g1 == 1 && g2 == 1 && g3 == 1)
    {
        x = cremainder(a1,b1,a2,b2,a3,b3);
        cout << "Answer of the x is : " << x ;
    }
    else
    {
        cout << "Can't Use the Chinese Remainder Theorem..." << endl;
    }
    return 0;
}
