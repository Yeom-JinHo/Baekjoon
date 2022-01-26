from collections import deque
import sys

dr=[[-1,-1,-1],[0,-1,-2],[1,1,1],[0,1,2],
    [1,1,1],[0,-1,-2],[-1,-1,-1],[0,1,2],
    [0,1,1],[1,1,2],[0,1,1],[-1,-1,-2],
    [1,1,1],[-1,0,1],[-1,-1,-1],[1,0,-1],
    [0,0,0],[1,2,3],[0,1,1]
    ]
dc=[[0,-1,-2],[1,1,1],[0,1,2],[-1,-1,-1],
    [0,-1,-2],[-1,-1,-1],[0,1,2],[1,1,1],
    [1,1,2],[0,-1,-1],[-1,-1,-2],[0,-1,-1],
    [-1,0,1],[-1,-1,-1],[-1,0,1],[1,1,1],
    [1,2,3],[0,0,0],[1,0,1]
    ]
N,M=map(int,sys.stdin.readline().split());

arr=[[0]*M for _ in range(N)];

for n in range(N):
  line =list(map(int,sys.stdin.readline().split()));
  for m in range(M):
    arr[n][m]=line[m];
max=0;
for r in range(N):
  for c in range(M):
    for i in range(19):
      tmp=arr[r][c];
      for j in range(3):
        tr=r+dr[i][j];
        tc=c+dc[i][j];
        if tr>=0 and tc>=0 and tr<N and tc<M:
          tmp+=arr[tr][tc];
        else:
          tmp=0;
          break;
      if max<tmp:
        max=tmp;
print(max)