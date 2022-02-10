import sys

tc=int(sys.stdin.readline());
arr=list();
for _ in range(tc):
  a,b=map(int,sys.stdin.readline().split());
  arr.append([a,b]);
arr.sort(key=lambda x:(x[1],x[0]));

for a in arr:
  print(a[0],a[1]);