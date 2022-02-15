import sys
def dp(sr,sc,er,ec):
  arr[sr][sc]=1;
  for r in range(sr,er+1):
    for c in range(sc,ec+1):
      if r==sr and c==sc:
        continue
      arr[r][c]+=arr[r-1][c];
      arr[r][c]+=arr[r][c-1];
N,M,K=map(int,sys.stdin.readline().split());

arr=[[0]*(M+1) for _ in range(N+1)];

R=(K-1)//M+1;
C=(K-1)%M+1;
if K!=0:
  result=0;
  dp(1,1,R,C);
  result=arr[R][C];
  dp(R,C,N,M);
  result*=arr[N][M]
  print(result)
else:
  dp(1,1,N,M)
  print(arr[N][M])

