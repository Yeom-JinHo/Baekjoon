import sys

N=int(sys.stdin.readline())
A=[0]+list(map(int,sys.stdin.readline().split()))
dp=[0]*(N+1)
dp[0]=0
for i in range(1,N+1):
  for j in range(0,i):
    if A[i]>A[j]:
      dp[i]=max(dp[i],dp[j]+A[i])

print(max(dp))