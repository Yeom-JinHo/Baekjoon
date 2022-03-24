import sys

def perm(ind):
  if ind==M:
    for t in tmp:
      print(t,end=" ");
    print()
  else:
    for i in range(N):
      if not chk[i]:
        chk[i]=True;
        tmp[ind]=arr[i];
        perm(ind+1);
        chk[i]=False;
N,M=map(int,sys.stdin.readline().split());

arr=list(map(int,sys.stdin.readline().split()));
chk=[False]*N;
tmp=[-1]*M;
arr.sort()

perm(0);
