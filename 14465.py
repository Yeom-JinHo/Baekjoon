import sys

N,K,B=map(int,sys.stdin.readline().split());

arr=[0]*(N+1);

for _ in range(B):
  bIndex=int(sys.stdin.readline());
  arr[bIndex]=1;
sumArr=list();
sumR=0;
for a in arr:
  sumR+=a;
  sumArr.append(sumR);
start=1;
minResult=sys.maxsize;

while start<=N-K+1:
  tmp=sumArr[start+K-1]-sumArr[start-1];
  minResult =min(minResult,tmp);
  start+=1;
print(minResult)