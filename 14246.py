import sys

n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()));
k=int(sys.stdin.readline());

start=0;
end=1;
tmp=arr[start];
count=0;
while True:
  if tmp>k:
    count+=n-end;
    start+=1
    end=start+1
    if end==n:
      break;
    tmp=arr[start]+arr[end];
  else:
    end+=1
    if end==n:
      break
    tmp+=arr[end];


print(count)


import sys

n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()));
# arr=sorted(list(map(int,sys.stdin.readline().split())));
k=int(sys.stdin.readline());

start=0;
end=0;
tmp=arr[start];
count=0;
while True:
  if tmp>k:
    count+=n-end;
    start+=1
    end=start+1
    if end==n:
      break;
    tmp=arr[start]+arr[end];
  else:
    end+=1
    if end==n:
      break
    tmp+=arr[end];
    

print(count)