import sys
st=[]

def push(n):
    st.append(n)
    
def pop():
    if(len(st)!=0):
        re=st[len(st)-1]
        del st[len(st)-1]
        print(re)
    else:
        print('-1')
    
def size():
    print(len(st))

def empty():
    if(len(st)==0):
        print('1')
    else:
        print('0')

def top():
    if(len(st)!=0):
        re=st[len(st)-1]
        print(re)
    else:
        print('-1')
n=int(input())
for i in range(n):
    ls=sys.stdin.readline().split()
    if(len(ls)==1):
        le=ls[0]
        if(le=='pop'):
            pop()
        elif(le=='size'):
            size()
        elif(le=='empty'):
            empty()
        elif(le=='top'):
            top()
    elif(len(ls)==2):
        push(ls[1])
