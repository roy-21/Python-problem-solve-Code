#include <stdio.h>
int main()
{
    int i,num,ans;
    scanf("%d",&num);
    ans=num/5;
    if (num % 5==0)
    {
        printf("%d",ans);
    }
    else
    {
        printf("%d",ans+1);
    }
return 0;
}
