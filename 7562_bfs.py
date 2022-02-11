from collections import deque
import sys

def bfs(sr,sc,er,ec,l):
  chk=[[False]*l for _ in range(l)];
  q=deque([[sr,sc,0]]);
  while q:
    r,c,cnt=q.popleft();
    chk[r][c]=True;
    if r==er and c==ec:
      return cnt;
    for i in range(8):
      tr=r+dr[i];
      tc=c+dc[i];
      if tr>=0 and tc>=0 and tr<l and tc<l:
        if not chk[tr][tc]:
          q.append([tr,tc,cnt+1])
          chk[tr][tc]=True
  

dr=[-1,-2,-2,-1,1,2,2,1];
dc=[-2,-1,1,2,2,1,-1,-2];

tc=int(sys.stdin.readline());
for t in range(tc):
  l=int(sys.stdin.readline());
  sr,sc=map(int,sys.stdin.readline().split());
  er,ec=map(int,sys.stdin.readline().split());
  print(bfs(sr,sc,er,ec,l));