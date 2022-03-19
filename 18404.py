from collections import deque
import sys

dr=[-1,-2,-2,-1,1,2,2,1];
dc=[-2,-1,1,2,2,1,-1,-2];
N,M =map(int,sys.stdin.readline().split());
sr,sc=map(int,sys.stdin.readline().split())
endList=deque();

for _ in range(M):
  er,ec=map(int,sys.stdin.readline().split());
  endList.append([er,ec]);

chk=[[-1]*N for _ in range(N)];
que=deque([[sr-1,sc-1,0]]);
chk[sr-1][sc-1]=0;
while que:
  now=que.popleft();
  for i in range(8):
    tr=now[0]+dr[i];
    tc=now[1]+dc[i];
    if tr>=0 and tr<N and tc>=0 and tc<N:
      if chk[tr][tc]==-1:
        chk[tr][tc]=chk[now[0]][now[1]]+1;
        que.append([tr,tc]);

for e in endList:
  print(chk[e[0]-1][e[1]-1],end=" ")