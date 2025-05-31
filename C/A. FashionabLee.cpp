#include <bits/stdc++.h>
using namespace std;
int t, n;
int main() 
{
  cin >> t;
  while (t--) {
    scanf("%d", &n);
    puts(n % 4 ? "NO" : "YES");
  }
  return 0;
}