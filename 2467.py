import sys
n=int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().split()))

start=0;
end=n-1;
result=sys.maxsize;
resultS=-1;
resultE=-1;
while start<end:
  tmp = arr[start]+arr[end];
  if result>abs(tmp):
    result=abs(tmp);
    resultS=start;
    resultE=end;
  else:
    if tmp>0:
      end-=1
    else:
      start+=1
print(arr[resultS],arr[resultE])