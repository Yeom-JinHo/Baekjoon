from collections import deque
import sys

def comb(start,dep):
  if dep==3:
    tmp=[[0]*C for _ in range(R)];
    for r in range(R):
      for c in range(C):
        tmp[r][c]=arr[r][c]
    cnt=0;
    for c in combArr:
      if tmp[ableBlock[c][0]][ableBlock[c][1]]==0:
        tmp[ableBlock[c][0]][ableBlock[c][1]]=1
        cnt+=1;
    if cnt==3:
      solve(tmp)
  else:
    for i in range(start,len(ableBlock)):
      combArr[dep]=i;
      comb(i+1,dep+1);
def solve(tmp):
  for r in range(R):
      for c in range(C):
        if tmp[r][c]==2:
          dfs(r,c,tmp)
  cnt=0;
  for r in range(R):
    for c in range(C):
      if tmp[r][c]==0:
        cnt+=1;
  global answer;
  answer=max(cnt,answer);
def dfs(sr,sc,arr):
  que=deque([[sr,sc]]);
  while que:
    now=que.popleft();
    r=now[0]
    c=now[1]
    for i in range(4):
      tr=r+dr[i];
      tc=c+dc[i];
      if tr>=0 and tc>=0 and tr<R and tc<C:
        if arr[tr][tc]==0:
          arr[tr][tc]=2;
          que.append([tr,tc]);
R,C =map(int,sys.stdin.readline().split());
arr=list();
ableBlock=list();
answer=0;
dr=[0,0,-1,1]
dc=[1,-1,0,0]
for _ in range(R):
  arr.append(list(map(int,sys.stdin.readline().split())));

for r in range(R):
  for c in range(C):
    if arr[r][c]==0:
      ableBlock.append([r,c]);

combArr=[-1]*3
comb(0,0)
print(answer)