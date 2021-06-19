n=int(input())
ls=[]
for i in range(n):
    ls.append(input())
dic=dict()
for word in ls:
    tls=[]
    tls.append(word)
    if(len(word) in dic):
        tls=tls+(dic[len(word)])
    dic[len(word)]=tls
dic=sorted(dic.items(),key= lambda x :x[0])
for n,k in dic:
    k=set(k)
    k=list(k)
    k.sort()
    for a in k:
        print(a)

