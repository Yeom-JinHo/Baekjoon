import sys

n,m=map(int,sys.stdin.readline().split());
arr=list();
for _ in range(n):
  arr.append(int(sys.stdin.readline()))

arr=sorted(arr);

start=0;
end=0;

answer=sys.maxsize;
while start<=end and end<n:
  tmp=arr[end]-arr[start];
  if tmp>=m:
    answer = min(answer,tmp);
    start+=1;
  else:
    end+=1
print(answer)