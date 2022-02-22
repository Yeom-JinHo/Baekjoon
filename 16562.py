from gettext import find
import sys
def findParent(a):
  if a==parents[a]:
    return a
  parents[a]=findParent(parents[a]);
  return parents[a];

def union(a,b):
  aRoot=findParent(a);
  bRoot=findParent(b);

  if aRoot!=bRoot:
    if pay[aRoot]<pay[bRoot]:
      parents[bRoot]=aRoot;
    else:
      parents[aRoot]=bRoot;
N,M,K=map(int,sys.stdin.readline().split());

pay=list(map(int,sys.stdin.readline().split()));
parents=[i for i in range(N)];
for _ in range(M):
  a,b=map(int,sys.stdin.readline().split());
  union(a-1,b-1);
chk=[False]*N;
totalPay=0;

for p in parents:
  i=findParent(p);
  if not chk[i]:
    chk[i]=True
    totalPay+=pay[i]
if totalPay<=K:
  print(totalPay);
else:
  print("Oh no");
