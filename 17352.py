import sys
sys.setrecursionlimit(10**6);

def findParent(a):
  if parents[a]==a:
    return a
  parents[a]=findParent(parents[a])
  return parents[a]

def union(a,b):
  aRoot =findParent(a);
  bRoot =findParent(b);
  if aRoot!=bRoot:
    parents[aRoot]=bRoot;

N=int(sys.stdin.readline())
parents=[i for i in range(N+1)];
for _ in range(N-2):
  a,b=map(int,sys.stdin.readline().split());
  union(a,b);

for i in range(1,N+1):
  for j in range(i+1,N+1):
    iRoot =findParent(i);
    jRoot =findParent(j);
    if iRoot!=jRoot:
      print(i,j);
      quit()