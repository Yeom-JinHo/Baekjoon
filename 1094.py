import sys

X=int(sys.stdin.readline());

init=64;
count=0;
while X>=1:
  if X//init>=1:
    count+=1;
    X=X%init
  else:
    init=init//2;

print(count)