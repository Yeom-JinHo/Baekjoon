import sys

n, m = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(ls)
result = 0
while start <= end:
    cnt = 0
    mid = (start+end)//2
    for l in ls:
        if l > mid:
            cnt += l-mid
        if cnt >= m:
            break
    if cnt >= m:
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)
