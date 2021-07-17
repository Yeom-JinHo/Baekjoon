import sys

m, n = map(int, sys.stdin.readline().split())

ls = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(ls)
result = 0
while start <= end:
    mid = (start+end)//2
    tmp = 0
    for l in ls:
        tmp += l//mid
    if tmp < m:
        end = mid-1
    else:
        start = mid+1
        result = mid
print(result)
