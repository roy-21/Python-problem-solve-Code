#include<stdio.h>
long long n;
main()
{
    scanf("%lld",&n);

    printf("%lld",n%2?-n>>1:n/2);
}