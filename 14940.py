from collections import deque
import sys

dr=[0,0,-1,1];
dc=[-1,1,0,0];

R,C=map(int,sys.stdin.readline().split());

que=deque();
arr=list();

for _ in range(R):
  arr.append(list(map(int,sys.stdin.readline().split())))


for r in range(R):
  for c in range(C):
    if arr[r][c]==2:
      que.append([r,c]);
      arr[r][c]=0
    else:
      arr[r][c]=-arr[r][c]


while que:
  r,c =que.popleft();

  for i in range(4):
    tr=r+dr[i];
    tc=c+dc[i];
    if tr>=0 and tc>=0 and tr<R and tc<C:
      if arr[tr][tc]<0:
        arr[tr][tc]=arr[r][c]+1
        que.append([tr,tc])


for r in range(R):
  for c in range(C):
    print(arr[r][c],end=" ")
  print()
  