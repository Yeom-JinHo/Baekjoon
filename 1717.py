import sys
def union(a,b):
  aRoot=findParent(a);
  bRoot=findParent(b);
  if aRoot!=bRoot:
    parent[bRoot]=aRoot;

def findParent(a):
  if a==parent[a]:
    return a
  parent[a]=findParent(parent[a]);
  return parent[a];
N,M=map(int,sys.stdin.readline().split())
parent=[i for i in range(N+1)];

for _ in range(M):
  command,a,b=map(int,sys.stdin.readline().split())
  if command==0:
    union(a,b)
  elif command==1:
    if findParent(a)==findParent(b):
      print("YES")
    else:
      print("NO")