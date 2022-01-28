import sys

N=int(sys.stdin.readline());
li = [[0]*2 for _ in range(N)];
maxX=0;
maxY=0;
for i in range(N):
  li[i][0],li[i][1]=map(int,sys.stdin.readline().split());
  if li[i][1]>maxY:
    maxY=li[i][1];
    maxX=li[i][0];
li.sort( key = lambda x :x[0]);
result=0;
py=0;
for i in range(N):
  nowX=li[i][0];
  nowY=li[i][1];
  if nowX == maxX:
    result+=nowY;
    maxX+=1;
    break;
  elif nowX<maxX:
    if py>nowY:
      continue;
    result+=(nowY-py)*(maxX-nowX);
    py=nowY

py=0;
for i in range(N-1,0,-1):
  nowX=li[i][0]+1;
  nowY=li[i][1];
  if nowX == maxX:
    break;
  elif nowX>maxX:
    if py>nowY:
      continue;
    result+=(nowY-py)*(nowX-maxX);
    py=nowY
print(result)


