import sys

def dfs(r,c,dep):
  chk[ord(arr[r][c])-ord("A")]=True;
  global answer;
  answer=max(answer,dep);
  for i in range(4):
    tr=r+dr[i];
    tc=c+dc[i];
    if tr>=0 and tc>=0 and tr<R and tc<C:
      if not chk[ord(arr[tr][tc])-ord("A")]:
        chk[ord(arr[tr][tc])-ord("A")]=True;
        dfs(tr,tc,dep+1);
        chk[ord(arr[tr][tc])-ord("A")]=False;
R,C=map(int,sys.stdin.readline().split());
chk=[False]*26;
arr=list();
dr=[-1,0,1,0];
dc=[0,1,0,-1];
answer=0;
for _ in range(R):
  arr.append(list(sys.stdin.readline().rstrip()));

dfs(0,0,1);
print(answer)
