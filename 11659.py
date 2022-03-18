import sys

N,M = map(int,sys.stdin.readline().split());

arr=list(map(int,sys.stdin.readline().split()));

sumArr=[0]*(N+1);
for i in range(1,N+1):
  sumArr[i]=sumArr[i-1]+arr[i-1]

for _ in range(M):
  start,end=map(int,sys.stdin.readline().split());
  print(sumArr[end]-sumArr[start-1]);
