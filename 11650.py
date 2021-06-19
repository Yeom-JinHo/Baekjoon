n=int(input())
ls=[]
for i in range(n):
    x,y=map(int,input().split())
    ls.append([x,y])
ls.sort()
for k in range(len(ls)):
    print(ls[k][0],end=' ')
    print(ls[k][1])
