import sys
n = int(sys.stdin.readline())
ls = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ls2 = list(map(int, sys.stdin.readline().split()))
ls.sort()
result = []
for l2 in ls2:
    start = 0
    end = n-1
    find = False
    while start <= end:
        mid = (start+end)//2
        if ls[mid] == l2:
            find = True
            break
        elif ls[mid] > l2:
            end = mid-1
        elif ls[mid] < l2:
            start = mid+1
    if find:
        result.append(1)
    else:
        result.append(0)

for re in result:
    print(re, end=' ')
print()
