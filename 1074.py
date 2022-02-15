import sys

N,R,C =map(int,sys.stdin.readline().split())

result=0;
for i in range(N,0,-1):
  len = 2**(i-1);
  td = 1 if R>=len else 0
  lr = 1 if C>=len else 0
  result+=2**(2*i-1)*td+2**(2*i-2)*lr;
  R-=len*td;
  C-=len*lr;
print(result)