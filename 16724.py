import sys
def dfs(sr,sc):  
  i=dd.index(arr[sr][sc]);
  tr=sr+dr[i];
  tc=sc+dc[i];
  union(sr,sc,tr,tc)

def union(sr,sc,er,ec):
  aRoot =findParents(sr,sc);
  bRoot =findParents(er,ec);
  if aRoot!=bRoot:
    parents[sr][sc]=parents[er][ec];

def findParents(r,c):
  if r*C+c==parents[r][c]:
    return r*C+c
  parents[r][c]=findParents(parents[r][c]//C,parents[r][c]%C);
  return parents[r][c];

# u d l r
dr=[-1,1,0,0];
dc=[0,0,-1,1];
dd=['U','D','L','R'];
R,C=map(int,sys.stdin.readline().split());
arr=list();

parents=[[0]*C for _ in range(R)];
count=0;
for r in range(R):
  for c in range(C):
    parents[r][c]=count;
    count+=1;

for _ in range(R):
  arr.append(list(sys.stdin.readline().rstrip()))

for r in range(R):
  for c in range(C):
      dfs(r,c);

chk=[False]*(R*C);

for r in range(R):
  for c in range(C):
    parents[r][c]=findParents(r,c);
answer=0;
for r in range(R):
  for c in range(C):
    if not chk[parents[r][c]]:
      chk[parents[r][c]]=True;
      answer+=1;

print(answer);