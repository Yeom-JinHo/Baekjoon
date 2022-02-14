import sys
from unittest import result

def comb(cnt,start):
  if cnt==n:
    if not sum(tmp) in result:
      result.append(sum(tmp))
  else:
    for i in range(start,4):
      tmp[cnt]=arr[i];
      comb(cnt+1,i)

n=int(sys.stdin.readline());
arr=[1,5,10,50];
result=list();
tmp=[0]*n;
comb(0,0);
print(len(result))