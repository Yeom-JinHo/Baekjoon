def so(n):
    if(n==1):
        return False
    for k in range(2,n):
        if(n%k==0):
            return False
    return True

n=int(input())
ls=list(map(int,input().split()))
cnt =0
for k in ls:
    if(so(k)):
        cnt+=1

print(cnt)
