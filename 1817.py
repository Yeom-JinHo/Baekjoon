import sys

N,M=map(int,sys.stdin.readline().split());
if N==0:
  print(0);
  quit()
arr=list(map(int,sys.stdin.readline().split()));

boxSize=0;
count=0;
for a in arr:
  if a>boxSize:
    count+=1;
    boxSize=M-a;
  else:
    boxSize-=a;
  print(a,boxSize,count)
print(count)