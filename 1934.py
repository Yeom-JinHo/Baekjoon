import sys
def gcd(a,b):
  return gcd(b,a%b) if b else a;
n =int(sys.stdin.readline());

for _ in range(n):
  a,b= map(int,sys.stdin.readline().split());
  g = gcd(max(a,b),min(a,b));
  if g==0:
    print(a*b);
  else:
    print(a*b//g);