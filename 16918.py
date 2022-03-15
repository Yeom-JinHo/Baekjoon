import sys
import copy

dr=[0,0,-1,1]
dc=[1,-1,0,0]
R,C,N =map(int,sys.stdin.readline().split());

arr=list();

for _ in range(R):
  arr.append(list(sys.stdin.readline().rstrip()));

for r in range(R):
  for c in range(C):
    if arr[r][c]=='O':
      arr[r][c]=2;
    else:
      arr[r][c]=0;

for i in range(2,N+1):
  for r in range(R):
    for c in range(C):
      arr[r][c]=arr[r][c]-1;

  if i%2==0:
    for r in range(R):
      for c in range(C):
        if arr[r][c]<=0:
          arr[r][c]=3;
  else:
    for r in range(R):
      for c in range(C):
        if arr[r][c]==0:
          for k in range(4):
            tr=r+dr[k];
            tc=c+dc[k];
            if tr>=0 and tr<R and tc>=0 and tc<C:
              if arr[tr][tc]!=0:
                arr[tr][tc]=-1;
    for r in range(R):
      for c in range(C):
        if arr[r][c]==-1:
          arr[r][c]=0;
          

for r in range(R):
    for c in range(C):
      if arr[r][c]==0:
        print(".",end='')
      else:
        print("O",end='')
    print()