from collections import deque
import sys

dr=[-1,1,0,0];
dc=[0,0,-1,1];
C,R = map(int,sys.stdin.readline().split())
arr=list();

for _ in range(R):
  arr.append(list(map(int,sys.stdin.readline().split())))

que=deque();
for c in range(C):
  for r in range(R):
    if arr[r][c]==1:
      que.append([r,c]);

answer=0;
while que:
  sr,sc = que.popleft();
  for i in range(4):
    tr=sr+dr[i];
    tc=sc+dc[i];
    if tr<R and tc<C and tc>=0 and tr>=0:
      if arr[tr][tc]==0:
        que.append([tr,tc])
        arr[tr][tc]=arr[sr][sc]+1
        

for c in range(C):
  for r in range(R):
    if arr[r][c]==0:
      print(-1);
      quit()
    answer=max(answer,arr[r][c])
print(answer-1)
