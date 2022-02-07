import sys
sys.setrecursionlimit(10000)
dr=[0,0,1,-1]
dc=[-1,1,0,0]
def dfs(r,c,li):
  li[r][c]=0;
  for i in range(4):
    tr=r+dr[i];
    tc=c+dc[i];
    if(tr>=0 and tc>=0 and tr<len(li) and tc<len(li[0])):
      if(li[tr][tc]==1):
        dfs(tr,tc,li);

testC=int(sys.stdin.readline());
for _ in range(testC):
  result=0;
  M,N,K=map(int,sys.stdin.readline().split());
  li=[[0]* M for _ in range(N)];
  for _ in range(K):
    c,r=map(int,sys.stdin.readline().split());
    li[r][c]=1;
  for r in range(N):
    for c in range(M):
      if(li[r][c]==1):
        dfs(r,c,li)
        result+=1;
  print(result)