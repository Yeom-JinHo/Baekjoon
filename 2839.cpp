#include <iostream>

using namespace std;

int main()
{
  int n;
  cin >> n;
  int dp[5001];
  for (int i = 0; i < 5001; i++)
  {
    dp[i] = 9999;
  }
  dp[3] = 1;
  dp[5] = 1;
  for (int i = 6; i < n + 1; i++)
  {
    if (dp[i - 3] != 9999)
      dp[i] = min(dp[i], dp[i - 3] + 1);
    if (dp[i - 5] != 9999)
      dp[i] = min(dp[i], dp[i - 5] + 1);
  }
  if (dp[n] != 9999)
    cout << dp[n];
  else
    cout << -1;
  return 0;
}