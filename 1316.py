n=int(input())
cnt=0
for i in range(n):
    word=input()
    ls=[]
    p=0
    gr=True
    for k in range(len(word)):
        if(word[k] not in ls):
            ls.append(word[k])
        else:
            if(word[k-1]!=word[k]):
                gr=False
                break
    if(gr):
        cnt+=1
print(cnt)
