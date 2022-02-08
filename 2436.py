import sys

A,B = map(int,sys.stdin.readline().split());
def gcd(num1,num2):
  return gcd(num2,num1%num2) if num2 else num1;
answer=[sys.maxsize]*2;
for i in range(A,int((A*B)**0.5)+1,A):
  if A*B%i==0:
    a=i;
    b=A*B//i;
    if sum(answer)>a+b and gcd(a,b)==A:
      answer[0]=a;
      answer[1]=b;
print(answer[0],answer[1]);