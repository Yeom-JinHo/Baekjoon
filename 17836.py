from collections import deque
import sys

dr=[0,0,-1,1];
dc=[-1,1,0,0];

R,C,T=map(int,sys.stdin.readline().split())

arr=list();
chk=[[[False]*C for _ in range(R)] for _ in range(T)]
for _ in range(R):
  arr.append(list(map(int,sys.stdin.readline().split())))
answer=sys.maxsize;
que =deque([[0,0,0,0]]);


while que:
  sr,sc,t,g=que.popleft();
  if sr==R-1 and sc==C-1:
    answer=min(answer,t)
    continue
  for i in range(4):
    tr=sr+dr[i];
    tc=sc+dc[i];
    if tr>=0 and tr<R and tc>=0 and tc<C:
      # 검이 있다면
      if g==1 and not chk[1][tr][tc]:
        que.append([tr,tc,t+1,1])
        chk[1][tr][tc]=True;
      elif not chk[0][tr][tc] and not arr[tr][tc]==1:
        if arr[tr][tc]==2:
          que.append([tr,tc,t+1,1]);
        else:
          que.append([tr,tc,t+1,0]);
        chk[0][tr][tc]=True

if answer>T:
  print('Fail')
else:
  print(answer)