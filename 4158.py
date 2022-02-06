import sys

N=0;
M=0;
while True:
  N,M = map(int,sys.stdin.readline().split());
  if N==0 and M==0:
    break
  a=list();
  b=list();
  for _ in range(N):
    a.append(int(sys.stdin.readline()))
  for _ in range(M):
    b.append(int(sys.stdin.readline()))
  ap=0;
  bp=0;
  count=0

  while ap<N and bp<M:
    if a[ap]==b[bp]:
      count+=1;
      ap+=1;
      bp+=1;
    elif a[ap]>b[bp]:
      bp+=1;
    else:
      ap+=1

  print(count)