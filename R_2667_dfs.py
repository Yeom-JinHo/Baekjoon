import sys
def check(r,c):
  if r>=0 and c>=0 and r<n and c<n:
    return True
  return False

def dfs(r,c):
  visited[r][c]=True;
  visitedP.append([r,c])
  for i in range(4):
    tr=r+dr[i];
    tc=c+dc[i];
    if(check(tr,tc)):
      if visited[tr][tc]==False and li[tr][tc]=='1':
        dfs(tr,tc);
  return len(visitedP);
dr=[-1,0,1,0];
dc=[0,1,0,-1]
n=int(sys.stdin.readline().rstrip())
li=list();
for _ in range(n):
  li.append(sys.stdin.readline().rstrip())

visited=[[False]*n for _ in range(n)];

result=list();
for r in range(n):
  for c in range(n):
    if visited[r][c]==False and li[r][c]=='1':
      visitedP=[]
      result.append(dfs(r,c));
result.sort();
print(len(result));
for r in result:
  print(r);