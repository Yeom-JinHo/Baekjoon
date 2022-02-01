import sys

N,M = map(int,sys.stdin.readline().split());

a=set();
b=set();
for i in range(N):
  a.add(sys.stdin.readline().rstrip());

for j in range(M):
  b.add(sys.stdin.readline().rstrip());
result=list(a & b);
result.sort()
print(len(result))
for r in result:
  print(r);