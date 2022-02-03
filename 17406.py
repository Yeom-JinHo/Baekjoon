from collections import deque
import itertools
import sys
import copy

# 센터는 안돌아도 댐 x 센터 기준으로 좌상부터 돈다.
def rotate(sr,sc,len,dep):
  global tmpArr;
  if dep<0:
    return
  if len!=1:
    r=sr;
    c=sc;
    que=deque();
    for i in range(4):
      for _ in range(len-1):
        que.append(tmpArr[r][c])
        r=r+dr[i];
        c=c+dc[i];

    que.appendleft(que.pop());
    
    for i in range(4):
      for _ in range(len-1):
        tmpArr[r][c]=que.popleft();
        r=r+dr[i];
        c=c+dc[i];

  rotate(sr-1,sc-1,len+2,dep-1)

# 우 하 좌 상
dr=[0,1,0,-1];
dc=[1,0,-1,0];

N,M,K=map(int,sys.stdin.readline().split());

arr=deque();
global tmpArr;
turnQue=deque();

for _ in range(N):
  arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
for _ in range(K):
  r,c,s=map(int,sys.stdin.readline().split())
  turnQue.append([r,c,s]);

perList=list(itertools.permutations(turnQue,K));
result=sys.maxsize;
for i in range(len(perList)):
  tmpArr=copy.deepcopy(arr);
  for j in range(K):
    rr,cc,ss=perList[i][j];
    rotate(rr-1,cc-1,1,ss);#인덱스는 0부터 시작이므로 한번 빼줌

  for row in tmpArr:
    result=min(result,sum(row));

print(result)
