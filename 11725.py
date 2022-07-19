from collections import deque
import sys

N=int(sys.stdin.readline())

chk=[0]*(N+1)
edges=list();
for _ in range(N+1):
  edges.append(list())

for _ in range(N-1):
  a,b=map(int,sys.stdin.readline().split())
  edges[a].append(b)
  edges[b].append(a)

que=deque();
que.append(1);
while que:
  now =que.popleft();
  for i in (edges[now]):
    if chk[i]==0:
      chk[i]=now;
      que.append(i);

for i in range(2,N+1):
  print(chk[i])

