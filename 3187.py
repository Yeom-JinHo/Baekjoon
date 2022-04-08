from collections import deque
import sys


def bfs(sr,sc):
  k=0;
  v=0;
  global K;
  global V;
  que=deque([[sr,sc]]);
  chk[sr][sc]=True;

  while que:
    now =que.popleft();
    if arr[now[0]][now[1]]=='k':
      k+=1;
    if arr[now[0]][now[1]]=='v':
      v+=1;        
    for i in range(4):
      tr=now[0]+dr[i];
      tc=now[1]+dc[i];
      if tr>=0 and tc>=0 and tr<R and tc<C:
        if not chk[tr][tc] and arr[tr][tc]!='#':
          chk[tr][tc]=True;
          que.append([tr,tc]);
  if k>v:
    K+=k;
  else:
    V+=v;

dr=[0,0,-1,1];
dc=[-1,1,0,0];

R,C=map(int,sys.stdin.readline().split());

arr=list();
chk=[[False]*C for _ in range(R)];
for _ in range(R):
  arr.append(list(sys.stdin.readline().rstrip()));

K=0;
V=0;

for r in range(R):
  for c in range(C):
    if arr[r][c]=='k' or arr[r][c]=='v':
      if not chk[r][c]:
        bfs(r,c);

print(K,V)