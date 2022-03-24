import sys

def perm(ind,start):
  if ind==M:
    for t in tmp:
      print(t,end=" ");
    print()
  else:
    for i in range(start,N):
        tmp[ind]=arr[i];
        perm(ind+1,i);
N,M=map(int,sys.stdin.readline().split());

arr=list(map(int,sys.stdin.readline().split()));
tmp=[-1]*M;
arr.sort()
perm(0,0);
