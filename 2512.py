import sys
n = int(sys.stdin.readline())
ls = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 1
end = max(ls)
result = 0
while start <= end:
    mid = (start+end)//2
    total = 0
    for l in ls:
        if l >= mid:
            total += mid
        else:
            total += l
    if total <= m:
        start = mid+1
        result = mid
    else:
        end = mid-1
print(result)
