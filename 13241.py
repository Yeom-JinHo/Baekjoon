import sys
def gcd(a,b):
  return gcd(b,a%b) if b else a

A,B =map(int,sys.stdin.readline().split());

g=gcd(A,B);

print(A*B//g)