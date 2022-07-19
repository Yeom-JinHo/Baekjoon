from collections import deque
import sys

dr=[0,0,1,-1,0,0]
dc=[0,0,0,0,-1,1]
dh=[1,-1,0,0,0,0]
C,R,H =map(int,sys.stdin.readline().split());

arr=list();

for _ in range(H):
  tmp =list();
  for _ in range(R):
    tmp.append(list(map(int,sys.stdin.readline().split())));
  arr.append(tmp);


que=deque();

for h in range(H):
  for r in range(R):
    for c in range(C):
      if arr[h][r][c]==1:
        que.append([h,r,c]);

while que:
  h,r,c =que.popleft();
  for i in range(6):
    th=h+dh[i];
    tr=r+dr[i];
    tc=c+dc[i];
    if th<H and th>=0 and tc<C and tc>=0 and tr<R and tr>=0:
      if arr[th][tr][tc]==0:
        arr[th][tr][tc]=arr[h][r][c]+1;
        que.append([th,tr,tc])

answer =0;

for h in range(H):
  for r in range(R):
    for c in range(C):
      if arr[h][r][c]==0:
        print(-1);
        quit();
      else:
        answer=max(answer,arr[h][r][c]);
print(answer-1)

