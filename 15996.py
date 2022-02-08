import sys

N,A=map(int,sys.stdin.readline().split());
count=0;
while N>0:
  N//=A;
  count+=N;
print(count)