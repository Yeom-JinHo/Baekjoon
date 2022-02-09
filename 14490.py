import sys

def gcd(a,b):
  return gcd(b,a%b) if b else a;

n,m=map(int,sys.stdin.readline().split(':'));
g=gcd(n,m);

print(f'{n//g}:{m//g}');