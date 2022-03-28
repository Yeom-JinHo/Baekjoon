from collections import deque
import sys

dr=[-1,1,0,0];
dc=[0,0,-1,1];

def bfs(sr,sc):
  chk=[[False]*C for _ in range(R)];
  depth=0;
  que=deque([[sr,sc,depth]]);
  chk[sr][sc]=True;

  while que:
    r,c,depth=que.popleft();
    for i in range(4):
      tr=r+dr[i]
      tc=c+dc[i]
      if tr>=0 and tr<R and tc>=0 and tc<C:
        if arr[tr][tc]=="L" and not chk[tr][tc]:
          que.append([tr,tc,depth+1]);
          chk[tr][tc]=True;
  return depth;

R,C=map(int,sys.stdin.readline().split())

lands=list();
arr=list();
for r in range(R):
  inp =list(sys.stdin.readline().rstrip());
  arr.append(inp);
  for c in range(C):
    if inp[c]=="L":
      lands.append([r,c]);

answer=0;
for land in lands:
  answer=max(answer,bfs(land[0],land[1]));
print(answer)