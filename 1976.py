import sys
def union(a,b):
  aRoot=findParent(a);
  bRoot=findParent(b);
  if aRoot!=bRoot:
    parent[bRoot]=aRoot;

def findParent(a):
  if a==parent[a]:
    return a;
  parent[a]=findParent(parent[a]);
  return parent[a];
N=int(sys.stdin.readline());
M=int(sys.stdin.readline());
arr=list();
parent=[i for i in range(N)];

for _ in range(N):
  arr.append(list(map(int,sys.stdin.readline().split())));

for r in range(N):
  for c in range(N):
    if arr[r][c]==1:
      union(r,c);

travel=list(map(int,sys.stdin.readline().split()))
start=findParent(travel[0]-1);
answer=True;
for i in range(1,M):
  if start!=findParent(travel[i]-1):
    answer=False;
    break;
if answer:
  print("YES")
else:
  print("NO")