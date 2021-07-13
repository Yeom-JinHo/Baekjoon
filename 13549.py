from typing import Deque

n, k = map(int, input().split())
que = Deque([n])
MaxN = 100001

cnt = [0]*MaxN
while que:
    n = que.popleft()
    if n == k:
        print(cnt[n])
        break
    for a in (2*n, n-1, n+1):
        if 0 <= a and a < MaxN and cnt[a] == 0:
            que.append(a)
            if a == n*2:
                cnt[a] = cnt[n]
            else:
                cnt[a] = cnt[n]+1
