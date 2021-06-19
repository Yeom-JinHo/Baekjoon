import sys
n,m=map(int,sys.stdin.readline().split())
result=[]
visited=[False]*n
def back(dep,idx,m):
    if dep==m:
        print(' '.join(map(str,result)))
    else:
        for i in range(idx,n):
            if not visited[i]:
                visited[i]=True
                result.append(i+1)
                back(dep+1,i+1,m)
                visited[i]=False
                result.pop()
back(0,0,m)
