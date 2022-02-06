import sys

n=int(sys.stdin.readline())
arr=sorted(list(map(int,sys.stdin.readline().split())))
x=int(sys.stdin.readline())

start=0;
end=n-1;
count=0;
while start<end:
  tmp=arr[start]+arr[end]
  if tmp==x:
    count+=1;
    start+=1;
  elif tmp>x:
    end-=1;
  else:
    start+=1;
print(count)