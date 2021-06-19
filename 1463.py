import sys
cnt=0
x=int(sys.stdin.readline())

while x!=1:
    if(x%3==0):
        x=int(x/3)
        cnt+=1
    elif(x%3==1):
        x=x-1
        cnt+=1
    elif(x%2==0):
        x=int(x/2)
        cnt+=1
    else:
        x=x-1
        cnt+=1
print(cnt)
