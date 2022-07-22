from collections import deque
import sys

dr=[0,0,1,1,1,-1,-1,-1]
dc=[1,-1,-1,0,1,-1,0,1];

R,C = map(int,sys.stdin.readline().split());

arr=list();

for _ in range(R):
  arr.append(list(map(int,sys.stdin.readline().split())))

answer =0;

sharks = deque();

for r in range(R):
  for c in range(C):
    if arr[r][c]==1:
      sharks.append([r,c]);
    else:
      arr[r][c]=sys.maxsize;

while sharks:
  sr,sc=sharks.popleft();
  que= deque([[sr,sc]]);

  while que:
    nr,nc=que.popleft();  
    for i in range(8):
      tr=nr+dr[i];
      tc=nc+dc[i];
      if tr>=0 and tr<R and tc>=0 and tc<C:
        if arr[tr][tc]>arr[nr][nc]+1:
          arr[tr][tc]=arr[nr][nc]+1;
          que.append([tr,tc])

for r in range(R):
  for c in range(C):
    answer= max(answer,arr[r][c])
print(answer-1)
