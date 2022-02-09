import sys

def gcd(a,b):
  return gcd(b,a%b) if b else a;

tc=int(sys.stdin.readline());

for _ in range(tc):
  a,b=map(int,sys.stdin.readline().split());
  g=gcd(a,b);
  print(a*b//g);
