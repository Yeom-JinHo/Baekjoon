import sys

n=int(sys.stdin.readline())
dp=[sys.maxsize]*(n+1);
dp[0]=0;
dp[1]=1;
for i in range(1,n+1):
  for j in range(int(i**0.5)+1):
    dp[i]=min(dp[i],dp[i-j*j]+1)
print(dp[n])