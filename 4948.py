import sys

MAX_N=123456+1;
chk=[False,False]+[True]*(2*MAX_N)
for i in range(2,int(2*MAX_N**0.5)+1):
  if chk[i]:
    for j in range(i+i,2*MAX_N,i):
      chk[j]=False;
while True:
  n=int(sys.stdin.readline())
  if n==0:
    break;
  count=0;
  for i in range(n+1,2*n+1):
    if chk[i]:
      count+=1;
  print(count)
