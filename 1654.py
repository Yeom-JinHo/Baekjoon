import sys

k, n = map(int, sys.stdin.readline().split())
ls = []
for _ in range(k):
    ls.append(int(sys.stdin.readline()))

result = 0
start = 1
end = max(ls)
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for l in ls:
        cnt += l // mid
    if cnt < n:
        end = mid-1
    else:
        result = mid
        start = mid+1
print(result)
