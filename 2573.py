from collections import deque
import sys

dr=[0,0,-1,1];
dc=[-1,1,0,0];

def bfs(sr,sc):
  que=deque([[sr,sc]]);
  chk[sr][sc]=True;
  while que:
    r,c=que.popleft();
    count=0;
    for i in range(4):
      tr=r+dr[i];
      tc=c+dc[i];
      if not chk[tr][tc]:
        if arr[tr][tc]!=0:
          que.append([tr,tc])
          chk[tr][tc]=True
        else:
          count+=1;
    arr[r][c]=0 if arr[r][c]-count<0 else arr[r][c]-count;


R,C=map(int,sys.stdin.readline().split());
arr=list();
for _ in range(R):
  arr.append(list(map(int,sys.stdin.readline().split())));

answer=0;

while True:
  count=0;
  chk=[[False]*C for _ in range(R)];
  for r in range(1,R-1):
    for c in range(1,C-1):
      if arr[r][c]!=0 and not chk[r][c]:
        bfs(r,c)
        count+=1;
  if count>=2:
    print(answer)
    break;
  if count==0:
    print(0);
    break;
  answer+=1;
