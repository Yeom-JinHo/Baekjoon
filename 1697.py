from typing import Deque

n, k = map(int, input().split())
que = Deque([n])
MaxN = 100001
visited = [False]*MaxN
cnt = [0]*MaxN
while que:
    n = que.popleft()
    if n == k:
        print(cnt[n])
        break
    for a in (n-1, n+1, n*2):
        if 0 <= a and a < MaxN and visited[a] == False:
            que.append(a)
            cnt[a] = cnt[n]+1
            visited[a] = True
