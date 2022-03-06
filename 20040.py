import sys
sys.setrecursionlimit(10**6)

def findParent(a):
  if(a==parents[a]):
    return a;
  parents[a]=findParent(parents[a]);
  return parents[a];
def union(a,b):
  aRoot=findParent(a);
  bRoot=findParent(b);
  if(aRoot!=bRoot):
    parents[aRoot]=bRoot;
    return False;
  else:
    return True;

n,m=map(int,sys.stdin.readline().split());
parents=[i for i in range(n)];
answer=0;
for i in range(m):
  a,b=map(int,sys.stdin.readline().split());
  if union(a,b):
    print(i+1);
    quit();
print(0);
