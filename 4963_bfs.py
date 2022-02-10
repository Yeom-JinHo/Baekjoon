from collections import deque
import sys

def bfs(r,c):
  que=deque([[r,c]]);
  visited[r][c]=True;
  while que:
    r,c=que.popleft();
    for i in range(8):
      tr=r+dr[i];
      tc=c+dc[i];
      if tr>=0 and tc>=0 and tr<h and tc<w:
        if not visited[tr][tc] and graph[tr][tc]==1:
          que.append([tr,tc]);
          visited[tr][tc]=True;
# 왼쪽 상단부터
dr=[-1,-1,-1,0,1,1,1,0];
dc=[-1,0,1,1,1,0,-1,-1];


while True:
  w,h=map(int,sys.stdin.readline().split());
  graph=list();
  if w==0 and h==0:
    break;
  for _ in range(h):
    graph.append(list(map(int,sys.stdin.readline().split())))
  visited=[[False]*w for _ in range(h)];
  count=0;
  for r in range(h):
    for c in range(w):
      if not visited[r][c] and graph[r][c]==1:
        bfs(r,c);
        count+=1;
  print(count)