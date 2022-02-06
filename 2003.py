import sys

N,M =map(int,sys.stdin.readline().split());
arr=list(map(int,sys.stdin.readline().split()));


start=0;
end=0;
count=0;
while start<=end and end<=N:
  sumArr=sum(arr[start:end]);
  if sumArr<=M:
    if sumArr==M:
      count+=1;
    end+=1;
  else:
    start+=1;
  # print(start,end,sumArr,count);
print(count);