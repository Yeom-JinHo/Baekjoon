import sys

N=int(sys.stdin.readline());

dp=[[0]*N for _ in range(N)];

inp=list(map(int,sys.stdin.readline().split()));

answer=0;
for i in range(N):
  dp[i][i]=inp[i];
  prev=inp[i];
  for j in range(i+1,N):
    if prev>inp[j]:
      dp[i][j]=dp[i][j-1]+inp[j]
      prev=inp[j]
    else:
      dp[i][j]=dp[i][j-1];

for i in range(N):
  print(dp[i])
  answer=max(answer,max(dp[i]));

print(answer)
