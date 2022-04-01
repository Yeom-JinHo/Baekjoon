import sys

N=int(sys.stdin.readline());

stairs=[0]*(N+1);
dp=[[0]*2 for _ in range(N+1)];
for i in range(1,N+1):
  stairs[i]=int(sys.stdin.readline());

for i in range(1,N+1):
  # 1칸
  if i>=3:
    dp[i][0]=max(dp[i][0],dp[i-1][1]+stairs[i]);
  else:
    dp[i][0]=max(dp[i][0],dp[i-1][0]+stairs[i],dp[i-1][1]+stairs[i]);

  if i>=2:
    dp[i][1]=max(dp[i][1],dp[i-2][0]+stairs[i],dp[i-2][1]+stairs[i]);
print(max(dp[N]));