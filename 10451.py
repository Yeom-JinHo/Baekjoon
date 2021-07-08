import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    ls = [[0]*2 for _ in range(n+1)]
    print(ls)
    inp = list(map(int, sys.stdin.readline().split()))
