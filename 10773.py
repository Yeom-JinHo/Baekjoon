import sys
n=int(sys.stdin.readline())
ls=[]

for i in range(n):
    inp=int(sys.stdin.readline())
    if(inp==0):
        del ls[len(ls)-1]
    else:
        ls.append(inp)

print(sum(ls))
