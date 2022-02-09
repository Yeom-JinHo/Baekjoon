import sys

def gcd(a,b):
  return gcd(b,a%b) if b else a
tA,bA= map(int,sys.stdin.readline().split());
tB,bB= map(int,sys.stdin.readline().split());

t=tA*bB+tB*bA;
b=bA*bB;
g=gcd(t,b);

print(t//g,b//g)
