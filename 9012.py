import sys

n=int(sys.stdin.readline())

for i in range(n):
    sta=[]
    text=sys.stdin.readline()
    cnt=0
    for t in text:
        if t=='(':
            sta.append(t)
        elif t==')':
            if len(sta)==0:
                print('NO')
                break
            else:
                top=sta.pop()
                if top!='(':
                    print('NO')
                    break        
        cnt=cnt+1
    if cnt==len(text):
        if len(sta)==0:
            print('YES')
        else:
            print('NO')
    
            
