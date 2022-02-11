from collections import deque
import sys
def per(n,dep):
  if n==dep:
    for a in q:
      print(a,end=' ');
    print()
  else:
    for i in range(1,n+1):
      if not chk[i]:
        chk[i]=True;
        q.append(i);
        per(n,dep+1);
        q.pop();
        chk[i]=False;

n=int(sys.stdin.readline());

chk=[False]*(n+1);

q=deque();
per(n,0);