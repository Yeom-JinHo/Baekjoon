from typing import Deque

n, k = map(int, input().split())
que = Deque([n])
path = Deque()
MaxN = 100001
cnt = [0]*MaxN
before = [0]*MaxN
while que:
    n = que.popleft()
    if n == k:
        print(cnt[n])
        break
    for a in (n-1, n+1, n*2):
        if 0 <= a and a < MaxN and cnt[a] == 0:
            que.append(a)
            cnt[a] = cnt[n]+1
            before[a] = n
x = k
for _ in range(cnt[k]+1):
    path.appendleft(x)
    x = before[x]
for p in path:
    print(p, end=' ')
print()
