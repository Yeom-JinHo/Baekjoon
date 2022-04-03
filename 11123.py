from collections import deque
import sys
dr=[0,0,-1,1];
dc=[-1,1,0,0];

def bfs(sr,sc):
  que=deque([[sr,sc]]);
  chk[sr][sc]=True;

  while que:
    now = que.popleft()
    for i in range(4):
      tr = now[0]+dr[i];
      tc = now[1]+dc[i];
      if tr>=0 and tc>=0 and tr<R and tc<C:
        if arr[tr][tc]=='#' and not chk[tr][tc]:
          que.append([tr,tc]);
          chk[tr][tc]=True

T=int(sys.stdin.readline());

for _ in range(T):
  R,C=map(int,sys.stdin.readline().split());
  arr=list();
  for _ in range(R):
    arr.append(list(sys.stdin.readline().rstrip()));
  
  chk=[[False]*C for _ in range(R)];

  count=0;

  for r in range(R):
    for c in range(C):
      if arr[r][c]=='#' and not chk[r][c]:
        bfs(r,c)
        count+=1;

  print(count)