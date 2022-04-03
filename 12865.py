import sys

N,K=map(int,sys.stdin.readline().split());

arr=list();
arr.append([0]*(K+1))
for _ in range(N):
  arr.append(list(map(int,sys.stdin.readline().split())));

dp=[[0]*(K+1) for _ in range(N+1)];

for item in range(1,N+1):
  for size in range(1,K+1):
    ## 안 넣는 경우
    maxValue=dp[item-1][size];
    ## 해당 아이템을 넣을 수 있을때
    if size-arr[item][0]>=0:
      maxValue=max(maxValue,dp[item-1][size-arr[item][0]]+arr[item][1])
      
    dp[item][size]=maxValue;

print(dp[N][K])