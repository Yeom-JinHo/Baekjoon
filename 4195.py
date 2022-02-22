import sys
def union(a,b):
  aRoot=findParent(a);
  bRoot=findParent(b);
  if aRoot!=bRoot:
    parents[bRoot]=aRoot;
    fCount[aRoot]+=fCount[bRoot];
  return fCount[aRoot];

def findParent(a):
  if a==parents[a]:
    return a
  parents[a]=findParent(parents[a]);
  return parents[a];

tc=int(sys.stdin.readline())

for _ in range(tc):
  f = int(sys.stdin.readline());
  fCount=dict();
  parents=dict();
  for _ in range(f):
    inp=list(sys.stdin.readline().rstrip().split());
    for i in inp:
      if not i in parents:
        parents[i]=i;
        fCount[i]=1;
    print(union(inp[0],inp[1]));
