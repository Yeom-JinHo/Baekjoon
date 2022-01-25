import sys
from collections import deque
def check(r,c):
  if r>=0 and c>=0 and r<n and c<n:
    return True;
  return False;

def bfs(r,c):
  que=deque([[r,c]])
  count=1;
  visted[r][c]=True
  while que:
    r,c=que.popleft();
    for i in range(4):
      tr=r+dr[i];
      tc=c+dc[i];
      if check(tr,tc):
        if visted[tr][tc]==False and li[tr][tc]=='1':
          que.append([tr,tc]);
          visted[tr][tc]=True;
          count+=1;
  return count;

dr=[-1,1,0,0];
dc=[0,0,-1,1];
n= int(sys.stdin.readline().rstrip())

visted=[[False]*n for _ in range(n)];
li=list();
for _ in range(n):
  li.append(sys.stdin.readline().rstrip());

result=list();
for r in range(n):
  for c in range(n):
    if li[r][c]=='1' and visted[r][c]==False:
      result.append(bfs(r,c));

print(len(result));
result.sort()
for l in result:
  print(l);
