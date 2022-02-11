from collections import deque
import sys

def bfs(que):
  while que:
    r,c=que.popleft();
    cnt=arr[r][c];
    for i in range(4):
      tr=r+dr[i];
      tc=c+dc[i];
      if tr>=0 and tc>=0 and tr<N and tc<M:
        if arr[tr][tc]==0:
          arr[tr][tc]=cnt+1;
          que.append([tr,tc])

dr=[0,0,-1,1];
dc=[-1,1,0,0];


M,N=map(int,sys.stdin.readline().split());

que=deque();
arr=list();

for _ in range(N):
  arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
for r in range(N):
  for c in range(M):
    if arr[r][c]==1:
      que.append([r,c]);

bfs(que);
answer=0;
for r in range(N):
  for c in range(M):
    if arr[r][c]==0:
      print(-1)
      quit();
    answer=max(answer,arr[r][c])
for a in arr:
  print(a)
print(answer-1)