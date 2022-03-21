import sys
sys.setrecursionlimit(10**6);
def union(a,b):
  aRoot=findParent(a);
  bRoot=findParent(b);
  if aRoot!=bRoot:
    parent[aRoot]=bRoot;

def findParent(a):
  if parent[a]==a:
    return a;
  parent[a]=findParent(parent[a]);
  return parent[a];

T=int(sys.stdin.readline());
global parent;
for t in range(T):
  N=int(sys.stdin.readline());
  parent=[i for i in range(N)];
  K=int(sys.stdin.readline());
  for _ in range(K):
    a,b=map(int,sys.stdin.readline().split());
    union(a,b);
  M=int(sys.stdin.readline());
  print("Scenario "+str(t+1)+":");
  for _ in range(M):
    u,v=map(int,sys.stdin.readline().split());
    if findParent(u)!=findParent(v):
      print("0");
    else:
      print("1");
  print()