#include<stdio.h>
int main()
{
    int a,b,c,t;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%d", &a, &b, &c);
        puts(a+b==c? "+" : "-");
    }
    return 0;
}