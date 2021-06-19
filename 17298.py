import sys

n =int(sys.stdin.readline())
inp=list(map(int,sys.stdin.readline().split()))
sta=[]
for i in range(n):
    while sta and inp[sta[-1]]<inp[i] :
        tmp=sta.pop()
        inp[tmp]=inp[i]
    sta.append(i)

while sta:
    inp[sta.pop()]=-1
for out in inp:
    print(out,end=' ')
