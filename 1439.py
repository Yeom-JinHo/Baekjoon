import sys

n = list(sys.stdin.readline().rstrip())
zCnt, oCnt = 0, 0

before = ''
for i in range(len(n)):
    if before != n[i]:
        if n[i] == '0':
            zCnt += 1
            before = '0'
        elif n[i] == '1':
            oCnt += 1
            before = '1'
print(min(zCnt, oCnt))
