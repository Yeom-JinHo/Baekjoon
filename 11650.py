import sys
n = int(sys.stdin.readline())
ls = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ls.append([x, y])
ls.sort()
for i in range(n):
    print(ls[i][0], ls[i][1])
