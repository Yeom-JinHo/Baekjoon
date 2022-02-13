import sys

def fac(n):
  if n<=1:
    return 1;
  else:
    return n*fac(n-1);

n,m=map(int,sys.stdin.readline().split());

print(fac(n)//(fac(n-m)*fac(m)));