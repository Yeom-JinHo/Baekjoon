import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    ls = list(map(int, sys.stdin.readline().split()))
    ls.sort()
    print(ls[-3])
