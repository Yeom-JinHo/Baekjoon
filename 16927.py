import sys
from collections import deque
def rotate(sr,sc,lenR,lenC,depth):
  r=sr;
  c=sc;
  que=deque();
  for ii in range(4):
    l=lenR if ii%2==0 else lenC;
    for _ in range(l-1):
      tr=r+dr[ii];
      tc=c+dc[ii];
      que.append(arr[tr][tc])
      r=tr
      c=tc;
  for _ in range(R%((lenR * 2) + (lenC * 2)- 4)):
      que.appendleft(que.pop())
  for ii in range(4):
    l=lenR if ii%2==0 else lenC;
    for _ in range(l-1):
      tr=r+dr[ii];
      tc=c+dc[ii];
      arr[tr][tc]=que.popleft()
      r=tr
      c=tc;
# 하 우 상 좌
dr=[1,0,-1,0];
dc=[0,1,0,-1];

N,M,R=map(int,sys.stdin.readline().rstrip().split());

arr=list()

for _ in range(N):
  arr.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(min(N,M)//2):
    rotate(0+i,0+i,N-2*i,M-2*i,i)
for r in range(N):
  for c in range(M):
    print(arr[r][c],end=" ")
  print()