from collections import deque
import sys
dr=[0,0,-1,1];
dc=[1,-1,0,0];

def bfs(sr,sc):
  que=deque([[sr,sc]]);
  tmpQ=deque([[sr,sc]]);
  while que:
    r,c=que.popleft();
    chk[r][c]=True;
    for i in range(4):
      tr=r+dr[i];
      tc=c+dc[i];
      if tr>=0 and tr<12 and tc>=0 and tc<6:
        if not chk[tr][tc] and arr[tr][tc]==arr[r][c]:
          chk[tr][tc]=True;
          que.append([tr,tc]);
          tmpQ.append([tr,tc]);
  
  if len(tmpQ)>=4:
    return tmpQ
  else:
    return []

def bomb(bombQ):
  while bombQ:
    sr,sc=bombQ.popleft();
    for r in range(sr,0,-1):
      arr[r][sc]=arr[r-1][sc];
    arr[0][sc]="."
    
arr=list();
for _ in range(12):
  arr.append(list(sys.stdin.readline().rstrip()));


answer=0;
while True:
  chk=[[False]*6 for _ in range(12)];

  bombQ=deque();
  for r in range(12):
    for c in range(6):
      if arr[r][c]!=".":
        bombQ.extend(bfs(r,c));
  # print(bombQ)
  if len(bombQ)==0:
    break;
  bomb(bombQ);
  # for i in range(12):
    # print(arr[i])
  # break;
  answer+=1
print(answer);