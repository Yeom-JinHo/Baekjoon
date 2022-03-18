import sys

N=int(sys.stdin.readline());
arr=[[sys.maxsize]*(N+1)];

for _ in range(N):
  arr.append([sys.maxsize]+list(map(int,sys.stdin.readline().split())));

dp=[[sys.maxsize]*(N+1) for _ in range(N+1)];

for r in range(1,N+1):
  for c in range(1,N+1):
    if r==1 and c==1:
      dp[r][c]=0;
      continue

    left=dp[r][c-1]+(0 if arr[r][c-1]>arr[r][c] else arr[r][c]-arr[r][c-1]+1)
    top= dp[r-1][c]+(0 if arr[r-1][c]>arr[r][c] else arr[r][c]-arr[r-1][c]+1);
    dp[r][c]=min(left,top)

print(dp[N][N]);