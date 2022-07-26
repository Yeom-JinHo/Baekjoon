from collections import deque
import sys

dr=[0,0,-1,1];
dc=[1,-1,0,0];

R,C=map(int,sys.stdin.readline().split());

arr=list();

chk=[[False]*C for _ in range(R)];

for _ in range(R):
  arr.append(list(sys.stdin.readline().rstrip())) 

que= deque([[0,0,0]]);
chk[0][0]=True;
while que:
  nr,nc,d=que.popleft();

  if nr==R-1 and nc==C-1:
    print(d+1)
    break;
  for i in range(4):
    tr=nr+dr[i];
    tc=nc+dc[i];
    if tr>=0 and tr<R and tc>=0 and tc<C:
      if arr[tr][tc]=='1' and not chk[tr][tc]:
        chk[tr][tc]=True;
        que.append([tr,tc,d+1])
