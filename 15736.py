import sys


n=int(sys.stdin.readline());
k=1;
while True:
  if k*k>n:
    break;
  k+=1
print(k-1)