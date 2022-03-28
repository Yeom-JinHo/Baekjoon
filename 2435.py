import sys

N,K=map(int,sys.stdin.readline().split());

arr=list(map(int,sys.stdin.readline().split()));
answer=-100*(N+1);

for i in range(0,N-K+1):
  answer=max(answer,sum(arr[i:i+K]));

print(answer)