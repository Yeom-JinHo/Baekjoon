import sys

n=int(sys.stdin.readline());

start=0;
end=0;
count=0;
tmp=0;
while start<=end and end<n:
  if tmp==n:
    count+=1;
    tmp+=end;
    end+=1
  elif tmp>n:
    tmp-=start;
    start+=1
  else:
    tmp+=end
    end+=1

print(count+1)