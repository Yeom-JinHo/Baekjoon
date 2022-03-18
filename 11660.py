import sys

N,M=map(int,sys.stdin.readline().split());

arr=[[0]*(N+1)];

for _ in range(N):
  arr.append([0]+list(map(int,sys.stdin.readline().split())))

total=[[0]*(N+1) for _ in range(N+1)]

for r in range(1,N+1):
  for c in range(1,N+1):
    total[r][c]+=total[r-1][c]+total[r][c-1]-total[r-1][c-1]+arr[r][c];

for _ in range(M):
  sr,sc,er,ec=map(int,sys.stdin.readline().split());
  answer=0;
  answer+=total[sr-1][sc-1];
  answer-=total[sr-1][ec];
  answer-=total[er][sc-1];
  answer+=total[er][ec]
  print(answer)