import sys
MAX_SIZE =10**5+1;
N,K=map(int,sys.stdin.readline().split());

coins=[0]*(N+1);
dp=[[MAX_SIZE]*(K+1) for _ in range(N+1)];
for i in range(1,N+1):
  coins[i]=int(sys.stdin.readline());

dp[0][0]=0
for i in range(1,N+1):

  for k in range(K+1):
    # i 번째를 하나도 안고를때
    dp[i][k]=dp[i-1][k]

    if k-coins[i]>=0:
      dp[i][k]=min(dp[i][k],dp[i][k-coins[i]]+1);

if dp[N][K]==MAX_SIZE:
  print(-1)
else:
  print(dp[N][K])