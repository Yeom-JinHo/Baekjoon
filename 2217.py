import sys;

n=int(sys.stdin.readline())
li=[0]*n;

for i in range(n):
  li[i]=int(sys.stdin.readline());

result=0;
li.sort();
for i in range(1,n+1):
  result=max(result,li[-i]*i);
print(result);