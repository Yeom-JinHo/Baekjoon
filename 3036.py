import sys

def gcd(a,b):
  return gcd(b,a%b) if b else a

n = int(sys.stdin.readline());

arr=list(map(int,sys.stdin.readline().split()));

for i in range(1,n):
  g=gcd(arr[0],arr[i]);
  print(f"{arr[0]//g}/{arr[i]//g}");
