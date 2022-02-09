import sys

M,N=map(int,sys.stdin.readline().split());

chk=[False,False]+[True]*(N-1);
for i in range(2,int(N**0.5)+1):
  if chk[i]:
    for j in range(i+i,N+1,i):
      chk[j]=False;

for i in range(M,N+1):
  if chk[i]:
    print(i);
print(chk)