from collections import deque
import sys

def bfs(start):
  global answer;
  que=deque([start])

  while que:
    now =que.popleft();
    chk[now]=True;
    for i in range(N):
      if not chk[i]:
        if(edges[now][i] or edges[i][now]):
          chk[i]=True;
          que.append(i)
          answer+=1;

N=int(sys.stdin.readline())
edges =[[False for _ in range(N)] for _ in range(N)];
chk=[False]*N;
M=int(sys.stdin.readline())
answer=0;
for _ in range(M):
  A,B=map(int,sys.stdin.readline().split());
  edges[A-1][B-1]=True;
  edges[B-1][A-1]=True;

bfs(0)
print(answer)