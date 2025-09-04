'''
problem link - https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/N
'''

#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    int A, B;
    scanf("%d %d", &A, &B);

    char S[20];  // Max length 10+10+1 = 21
    scanf("%s", S);

    int len = strlen(S);

    if(len != A + B + 1) {
        printf("No\n");
        return 0;
    }

    if(S[A] != '-') {
        printf("No\n");
        return 0;
    }

    for(int i = 0; i < len; i++) {
        if(i != A && !isdigit(S[i])) {
            printf("No\n");
            return 0;
        }
    }

    printf("Yes\n");
    return 0;
}