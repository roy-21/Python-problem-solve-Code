#include <stdio.h>

int main()
 {
int  i, n, a, b, c, ans=0;
scanf("%d", &n);
for(i = 0; i < n; i++)
        {
            scanf("%d %d %d", &a, &b, &c);
            int ans1 = a + b + c;
            ans = ans + ans1/2;}
            printf("%d",ans);
            return 0;}