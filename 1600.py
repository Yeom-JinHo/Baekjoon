import sys
from collections import deque

def check(r,c):
  if(r>=0 and c>=0 and r<h and c<w):
    return True
  return False

def horMove(r,c,k):
    for i in range(len(hdr)):
      tr=r+hdr[i];
      tc=c+hdc[i];
      if(check(tr,tc)):
        if(visitCount[tr][tc][k-1]==0 and li[tr][tc]==0):
          que.append([tr,tc,k-1]);
          visitCount[tr][tc][k-1]=visitCount[r][c][k]+1;


def monMove(r,c,k):
    for i in range(len(dr)):
      tr=r+dr[i];
      tc=c+dc[i];
      if(check(tr,tc)):
        if(visitCount[tr][tc][k]==0 and li[tr][tc]==0):
          que.append([tr,tc,k]);
          visitCount[tr][tc][k]=visitCount[r][c][k]+1;


# 좌측 상단부터
hdr=[-1,-2,-2,-1,1,2,2,1];
hdc=[-2,-1,1,2,2,1,-1,-2];
# 상 우 좌 하
dr=[-1,0,0,1];
dc=[0,1,-1,0];

k=int(sys.stdin.readline().rstrip());
w,h=map(int,sys.stdin.readline().rstrip().split());

li=list();
for _ in range(h):
  li.append(list(map(int,sys.stdin.readline().rstrip().split())));

visitCount=[[[0]*(k+1) for _ in range(w)] for _ in range(h)];
que=deque([[0,0,k]]);

while que:
  r,c,k = que.popleft();
  if r==h-1 and c==w-1: # 끝내는 조건
      print(visitCount[r][c][k]);
      break
  if k>=1:
      horMove(r,c,k)
      monMove(r,c,k)
  else : 
      monMove(r,c,k)
else : print(-1)
