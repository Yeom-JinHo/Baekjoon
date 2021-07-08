
import sys

n = int(sys.stdin.readline())
ls = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ls2 = list(map(int, sys.stdin.readline().split()))
result = [0]*20000001
for l in ls:
    result[l] += 1

for l2 in ls2:
    print(result[l2], end=' ')
print()
