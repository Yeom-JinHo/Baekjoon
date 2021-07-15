import sys

n, k = map(int, sys.stdin.readline().split())
ls = []
for _ in range(n):
    ls.append(int(sys.stdin.readline().rstrip()))

start = 1
end = max(ls)
result = 0
while start <= end:
    cnt = 0
    mid = (start+end)//2

    for l in ls:
        cnt += l//mid

    if cnt < k:
        end = mid-1
    else:
        start = mid+1
        result = mid
print(result)
