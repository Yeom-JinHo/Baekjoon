from collections import deque
import sys
dr=[-1,-1,-1,0,0,1,1,1];
dc=[-1,0,1,-1,1,-1,0,1];

def bfs(sr,sc):
  que=deque([[sr,sc]]);
  chk[sr][sc]=True;

  while que:
    r,c=que.popleft();

    for i in range(8):
      tr=r+dr[i];
      tc=c+dc[i];
      if tr>=0 and tc>=0 and tr<R and tc<C:
        if arr[tr][tc]==1 and not chk[tr][tc]:
          chk[tr][tc]=True
          que.append([tr,tc])
    
R,C=map(int,sys.stdin.readline().split())

arr=list();
chk=[[False]*C for _ in range(R)];
for _ in range(R):
  arr.append(list(map(int,sys.stdin.readline().split())));

answer =0;

for r in range(R):
  for c in range(C):
    if arr[r][c]==1 and not chk[r][c]:
      bfs(r,c);
      answer+=1;
print(answer)