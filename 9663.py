import sys

n=int(sys.stdin.readline())
x=y=n
cnt=0
ls=[]
visted=[[False for i in range(x)] for k in range(y)]
def back(dep,x,y,n):
    if dep==n:
        cnt=cnt+1
        return
    else:
        for a in range(n):
            for i in range(x):
                for k in range(y):
                    if not visited[x][y]:
                        ls.append(
        





back(0,x,y)
