from collections import deque
from pickle import FALSE
import sys

F,S,G,U,D = map(int,sys.stdin.readline().rstrip().split());

que=deque([S]);
visited=[-1]*(F+1);
df=[U,-D];
count=0;
visited[S]=0;
while que:
  nowF=que.popleft();
  if nowF == G:
    print(visited[nowF])
    break;
  for i in range(len(df)):
    tmpF=nowF+df[i];
    if tmpF>0 and tmpF<=F:
      if visited[tmpF]==-1:
        que.append(tmpF)
        visited[tmpF]=visited[nowF]+1
        
if visited[G]==-1:
  print("use the stairs")