import sys

def perm(ind):
  if ind==M:
    for t in tmp:
      print(t,end=" ")
    print()
  else:
    for i in range(N):
      tmp[ind]=arr[i];
      perm(ind+1)
  

N,M=map(int,sys.stdin.readline().split());
arr=list(map(int,sys.stdin.readline().split()));
arr=sorted(arr);
tmp=[0]*M;

perm(0)