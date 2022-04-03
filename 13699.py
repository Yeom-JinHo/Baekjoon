import sys

N=int(sys.stdin.readline());

dp=[0]*(N+1);
dp[0]=1;

for i in range(1,N+1):
  for j in range(i):
    dp[i]+=dp[j]*dp[i-j-1]

print(dp[N])