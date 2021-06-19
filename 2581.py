mi=int(input())
ma=int(input())
ls=[]
for k in range(mi,ma+1):
    cnt=0
    for i in range(1,k):
        if(k%i==0):
            cnt+=1
        if(cnt>=2):
            break
    if(cnt==1):
        ls.append(k)
    


if(len(ls)==0):
    print('-1')
else:
    print(sum(ls))
    print(ls[0])
    
