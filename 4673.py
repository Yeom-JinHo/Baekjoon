def sel(n):
    ls=[]
    for i in range(1,n):
        ls.append(i)
    for a in range(1,n):
        while (a<=n):
            al=list(map(int,str(a)))
            a=a+sum(al)
            if(ls.count(a)==0):
                break
            else:
                ls.remove(a)
    for k in ls:
        print(k)
sel(10000)
