#include<bits/stdc++.h>
using namespace std;

void EEA(long long a,long long b)
{
    long long s1,s2,t1,t2,r1,r2,q,r,s,t;
    // initialization
    s1=1;
    s2=0;
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
        //s update
        s = s1 - q*s2;
        s1 = s2;
        s2 = s;
        // t update
        t = t1 - q*t2;
        t1 = t2;
        t2 = t;
    }
    cout << "gcd(" << a<<"," << b << ")" << "is : " << r1 << endl;
    cout << "s = " << s1 << " And " << "t = " << t1 << endl;
    cout << "You can verify Answer using s*a + t*b = gcd(a,b)";
}

int main()
{
   long long a,b;
   cout << "Enter two Numbers : " ;
   cin >> a >> b;
   EEA(a,b);
   return 0;
}
