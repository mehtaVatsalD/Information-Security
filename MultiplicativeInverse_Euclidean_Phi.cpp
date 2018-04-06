#include<bits/stdc++.h>
using namespace std;
int phi(int n)
{
    int m = n,i,a[100]={0},j=0,f=0;
    for(i=2 ;i<m/2 ;i++)
    {
        while(n % i == 0 && n>0)
        {
            a[j] = i;
            n = n/i;
            j++;
            f=1;
        }
        if(n == 0)
        {
            break;
        }
    }
    long long answer=1;
    int c =1,k;
    if(f==1)
    {
        for(int i=0 ;i<j ;i++)
        {
             k = a[i];
            c = 1;
            while(a[i] == a[i+1])
            {
                c++;
                i++;

            }
            //cout << c << " " << k << endl;
            answer *= (pow(k,c)-pow(k,c-1));
            //cout << answer << endl;
        }
    }
    else
    {
        answer = m-1;
    }
    return answer;
}
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
    int a,n,answer;
    cout << "Enter Two Numbers : ";
    cin >> a >> n;
    answer = phi(n);
    long long k = sage(a,answer-1,n);
    cout << "Multiplicative Inverse of " << a << " is " << k << endl;
    return 0;
}
