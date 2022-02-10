import sys

n=int(sys.stdin.readline())

erased=[False]*(n+1);

prime=list();
for i in range(2,n+1):
  if not erased[i]:
    prime.append(i);
    for j in range(i*2,n+1,i):
      erased[j]=True;

start=0;
end=0;
result=0;
while end<len(prime):
  tmp=sum(prime[start:end+1]);
  if tmp>n:
    start+=1
  elif tmp==n:
    result+=1;
    end+=1;
  else:
    end+=1;
print(result)
