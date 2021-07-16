n = int(input())
ls = []
for i in range(1, n+1):
    if(i//100 != 0):
        if(i//100-i//10 % 10 == i//10 % 10-i % 10):
            ls.append(int(i))
    else:
        ls.append(i)

print(len(ls))
