import sys

n, m = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))

start = max(ls)
end = sum(ls)
result = 0

while start <= end:
    total = 0
    cnt = 1
    mid = (start+end)//2
    for l in ls:
        if total+l > mid:
            cnt += 1
            total = l
        else:
            total += l
    if cnt > m:
        start = mid+1
    else:
        result = mid
        end = mid-1
print(result)
