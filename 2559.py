import sys
N,K=map(int,sys.stdin.readline().split());
arr=list(map(int,sys.stdin.readline().split()))
addArr=[0]*N;
addArr[0]=arr[0];
for i in range(1,N):
  addArr[i]=addArr[i-1]+arr[i];

answer=addArr[K-1];
for j in range(1,N-K):
  answer=max(answer,addArr[j+K]-addArr[j]);
print(answer)
