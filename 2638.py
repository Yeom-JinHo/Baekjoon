from collections import deque
import sys
dr=[0,0,-1,1];
dc=[1,-1,0,0];

R,C=map(int,sys.stdin.readline().split());
arr=list()
cheeseCount=0;
for _ in range(R):
  inp=list(map(int,sys.stdin.readline().split()));
  cheeseCount+=inp.count(1);
  arr.append(inp);


answer=0;
while True:
  if cheeseCount==0:
    print(answer);
    break;
  chk=[[False]*C for _ in range(R)];
  que=deque([[0,0]]);

  count=0;
  while que:
    r,c=que.popleft();
    for i in range(4):
      tr=r+dr[i];
      tc=c+dc[i];
      if tr>=0 and tc>=0 and tr<R and tc<C:
        if chk[tr][tc]:
          if arr[tr][tc]==1:
            arr[tr][tc]=0;
            count+=1;
        else:
          if arr[tr][tc]==0:
            que.append([tr,tc])
          chk[tr][tc]=True
  cheeseCount-=count;
  answer+=1;