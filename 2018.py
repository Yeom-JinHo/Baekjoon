import sys
import math
n = int(sys.stdin.readline())
ls = []
dls = []
dic = dict()
for i in range(0, n):
    inp = int(sys.stdin.readline())
    ls.append(inp)
    if(inp in dic):
        dic[inp] += 1
    else:
        dic[inp] = 1
dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)

for i in range(len(dic)):
    if(dic[i][1] == dic[0][1]):
        dls.append(dic[i][0])
ls.sort()
dls.sort()
print(round(sum(ls)/n))
print(ls[math.floor(n/2)])

if(len(dls) == 1):
    print(dls[0])
else:
    print(dls[1])
print(max(ls)-min(ls))
