import sys

N,S=map(int,sys.stdin.readline().split());

arr=list(map(int,sys.stdin.readline().split()));

start=0;
end=0;
tmpS=arr[start]
answer=N+1;
while True:
  if tmpS>=S:
    answer=min(answer,end-start+1);
    tmpS-=arr[start]
    start+=1
  else:
    end+=1
    if end==N:
      break;
    tmpS+=arr[end]
if answer==N+1:
  print(0)
else:
  print(answer)