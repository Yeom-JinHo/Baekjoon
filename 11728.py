import re
import sys

N,M = map(int,sys.stdin.readline().split())

a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))


ap=0
bp=0
result=list();
while len(result)<N+M:
  if ap>=N:
    result.append(b[bp]);
    bp+=1;
    continue
  if bp>=M:
    result.append(a[ap]);
    ap+=1;
    continue
  if a[ap]<b[bp]:
    result.append(a[ap]);
    ap+=1
  else:
    result.append(b[bp]);
    bp+=1

print(" ".join(map(str,result)))