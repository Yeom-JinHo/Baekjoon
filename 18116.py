import sys

def union(a,b):
  aRoot =findParent(a);
  bRoot =findParent(b);
  if aRoot!=bRoot:
    parents[aRoot]=bRoot;
    cnts[bRoot]+=cnts[aRoot];
    cnts[aRoot]=0
def findParent(a):
  if parents[a]==a:
    return a
  parents[a]=findParent(parents[a]);
  return parents[a];

N=int(sys.stdin.readline())
M=1000000;
parents=[i for i in range(M+1)];
cnts=[1]*(M+1);

print(parents[0:10])
print(cnts[0:10])

for _ in range(N):
  inp =list(sys.stdin.readline().split());
  if inp[0]=='I':
    union(int(inp[1]),int(inp[2]))
  else:
    # count=0;
    root=findParent(int(inp[1]));
    print(cnts[root]);
    # for i in range(M+1):
      # if findParent(i)==root:
        # count+=1;
    # print(count);
  print(parents[0:10])
  print(cnts[0:10])
  # print(parents)