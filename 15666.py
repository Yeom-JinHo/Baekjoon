from re import L
import sys

def perm(ind,start):
  if ind==M:
    for t in tmp:
      print(t,end=" ");
    print()
  else:
    for i in range(start,len(arr)):
      tmp[ind]=arr[i];
      perm(ind+1,i);
    
N,M=map(int,sys.stdin.readline().split());

arr=list(map(int,sys.stdin.readline().split()));
tmp=[-1]*M;
arr=list(set(arr));
arr.sort();
perm(0,0);