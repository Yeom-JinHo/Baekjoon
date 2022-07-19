from collections import deque
import sys

def bfs(start):
  que=deque([start]);
  while que:
    now =que.popleft();
    chk[now]=True;
    for i in range(1,N+1):
      if not chk[i]:
        if edges[i][now]:
          chk[i]=True;
          que.append(i)
          bfsArr.append(str(i));

def dfs(start):
  chk[start]=True;
  for i in range(1,N+1):
    if not chk[i]:
      if edges[i][start]:
        dfsArr.append(str(i));
        dfs(i)

N,M,V=map(int,sys.stdin.readline().split())

edges=[[False]*(N+1) for _ in range(N+1)]

chk=[False]*(N+1);
bfsArr=[str(V)];
dfsArr=[str(V)];
for _ in range(M):
  A,B=map(int,sys.stdin.readline().split());
  edges[A][B]=True
  edges[B][A]=True

bfs(V);
chk=[False]*(N+1);
dfs(V);
print(' '.join(dfsArr))
print(' '.join(bfsArr))


