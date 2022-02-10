import sys
def gcd(a,b):
  return gcd(b,a%b) if b else a;
def dfs(depth):
  global answer
  if depth==2:
    re=list();
    for i in range(len(visted)):
      if visted[i]:
        re.append(arr[i]);
    answer=max(answer,gcd(max(re),min(re)));
  else:
    for i in range(len(arr)):
      if not visted[i]:
        visted[i]=True;
        dfs(depth+1);
        visted[i]=False;

global answer;
n=int(sys.stdin.readline());
arr=list();
visted=list();
for i in range(n):
  answer=-1;
  arr=list(map(int,sys.stdin.readline().split()));
  visted=[False]*len(arr);
  dfs(0)
  print(answer);
