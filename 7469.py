import sys
def Q(ls,i,j,k):
    ls_q=ls[i:j+1]
    ls_q.sort()
    return ls_q[k]

n,qn=map(int,sys.stdin.readline().split())
ls=list(map(int,sys.stdin.readline().split()))
for i in range(qn):
    i,j,k=map(int,sys.stdin.readline().split())
    print(Q(ls,i,j,k))
