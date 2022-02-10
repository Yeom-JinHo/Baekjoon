import sys

n=int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().split()));

arr.sort();
count=0;
for i in range(0,n):
  count+=arr[i]*(n-i)
print(count)