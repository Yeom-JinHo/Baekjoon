#include <iostream>

using namespace std;
void solution(int n)
{
  int dp[11];

  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 4;
  for (int i = 4; i < n + 1; i++)
  {
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
  }
  cout << dp[n] << '\n';
}
int main()
{
  int t;
  cin >> t;
  for (int i = 0; i < t; i++)
  {
    int n;
    cin >> n;
    solution(n);
  }
  return 0;
}
