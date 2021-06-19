n=int(input())
while n>1:
    for k in range(2,n+1):
        if(n%k==0):
            print(k)
            n=int(n/k)
            break
