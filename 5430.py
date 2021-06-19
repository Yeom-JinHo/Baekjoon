import sys
n=int(sys.stdin.readline())

for i in range(n):
    te=sys.stdin.readline()
    ln=sys.stdin.readline()
    ls=sys.stdin.readline().split()
    ls=str(ls)
    ls=ls[2:-2]
    for k in range(len(te)-1):
        if(te[k]=='R'):
            ls=ls[1:-1]
            ls=ls[::-1]
            ls='['+ls+']'
        elif(te[k]=='D'):
            if(len(ls)==2):
                print('error')
                break
            else:
                ls=ls[0:1]+ls[3:]
    if(len(ls)!=2):            
        print(ls)
