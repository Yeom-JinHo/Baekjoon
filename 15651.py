import sys

n,m=map(int,sys.stdin.readline().split())
ls=list()
visited=[False]*n
def back(dep,idx,m):
    if dep==m:
        print(' '.join(map(str,ls)))
    else:
        for i in range(idx,n):
            if not visited[idx]:
                ls.append(i+1)
                back(dep+1,i,m)
                ls.pop()
back(0,0,m)
