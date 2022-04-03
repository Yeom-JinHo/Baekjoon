import sys
sys.setrecursionlimit(10**6);

def union(a,b):
  aRoot =findParent(a);
  bRoot =findParent(b);
  if aRoot!=bRoot:
    parents[bRoot]=aRoot;

def findParent(a):
  if a==parents[a]:
    return a;
  parents[a]=findParent(parents[a]);
  return parents[a];
N=int(sys.stdin.readline());
chk=[False]*N;
parents=[0]*N;

for i in range(N):
  parents[i]=i;

arr=list(sys.stdin.readline().rstrip())
for i in range(N):
  if arr[i]=='E':
    if i!=N-1:
      union(i,i+1);
  elif arr[i]=='W':
    if i!=0:
      union(i-1,i)
for i in range(N):
  chk[parents[i]]=True;

answer=0;
for i in range(N):
  if chk[i]:
    answer+=1;

print(answer)
