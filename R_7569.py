from collections import deque
import sys
dr=[-1,1,0,0,0,0];
dc=[0,0,-1,1,0,0];
dd=[0,0,0,0,-1,1];

def bfs(q):
  # print(q);
  while q:
    # print(q);
    d,r,c,count=q.popleft();
    li[d][r][c]=1;
    for i in range(6):
      td=d+dd[i];
      tr=r+dr[i];
      tc=c+dc[i];
      if td>=0 and tr>=0 and tc>=0 and td<H and tr<N and tc<M:
        if li[td][tr][tc]==0:
          q.append([td,tr,tc,count+1])
          li[td][tr][tc]=1;
  return count;

M,N,H=map(int,sys.stdin.readline().split());

li=[[[0]*M for _ in range(N)] for _ in range(H)];

for d in range(H):
  for r in range(N):
    inp=list(map(int,sys.stdin.readline().split()));
    li[d][r]=inp
result=-1;
q=deque();
for d in range(H):
  for r in range(N):
    for c in range(M):
      if li[d][r][c]==1:
        q.append([d,r,c,0]);
if q:        
  result=bfs(q);

for d in range(H):
  for r in range(N):
    for c in range(M):
      if li[d][r][c]==0:
        print(-1);
        exit();
print(result)