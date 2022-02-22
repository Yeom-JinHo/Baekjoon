import sys
def findParent(a):
  if a==parents[a]:
    return a;
  parents[a]=findParent(parents[a]);
  return parents[a];
def union(a,b):
  aRoot=findParent(a);
  bRoot=findParent(b);
  if aRoot!=bRoot:
    parents[bRoot]=aRoot;
    arr[aRoot]+=arr[bRoot];
  return arr[aRoot];
N,M=map(int,sys.stdin.readline().split());

arr=[0]*(N+1);
parents=[i for i in range(N+1)];
for i in range(N):
  arr[i+1]=int(sys.stdin.readline());

for _ in range(M):
  a,b=map(int,sys.stdin.readline().split());
  print(union(a,b));