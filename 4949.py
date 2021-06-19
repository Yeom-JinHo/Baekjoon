import sys

while True:
    sta=[]
    text=sys.stdin.readline().rstrip()
    if text=='.':
        break
    cnt=0
    for t in text:
 
        if t=='(' or t=='[':
            sta.append(t)
        elif t==')':
            if sta:
                top=sta.pop()
                if top!='(':
                    break
            else:
                break
        elif t==']':
            if sta:
                top=sta.pop()
                if top!='[':
                    break
            else:
                break
        cnt+=1
    if len(sta)==0 and cnt==len(text):
        print('yes')
    else:
        print('no')
