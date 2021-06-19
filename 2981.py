n=int(input())
ori=dict()
ls=[]
for i in range(n):
    ip=int(input())
    o=dict()
    for k in range(2,ip+1):
        if(i==0):
            ori[k]=ip%k
        else:
            o[k]=ip%k
    if(i!=0):
        for i, j in ori.items() :
            for i1, j1 in o.items() :
                if i==i1 and j=j1  :
                    ls.append(i)
    for j in ls:
        
for i,j in ori.items():
    print(i,end=' ')
