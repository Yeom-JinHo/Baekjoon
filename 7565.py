from collections import deque
from sys import stdin
from typing import get_args


def bfs(graph, que):
    while que:
        x, y = que[0][0], que[0][1]
        del que[0]
        for i in range(4):
            rx = x+dx[i]
            ry = y+dy[i]
            if rx >= 0 and ry >= 0 and rx < n and ry < m:
                if graph[rx][ry] == 0 and visited[rx][ry] == False:
                    cnt[rx][ry] = cnt[x][y]+1
                    visited[rx][ry] = True
                    que.append([rx, ry])


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


m, n = map(int, stdin.readline().rstrip().split())

graph = []
cnt = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
que = deque()

for a in range(n):
    graph.append(list(map(int, stdin.readline().rstrip().split())))

for b in range(n):
    for c in range(m):
        if graph[b][c] == 1:
            cnt[b][c] = 1
            que.append([b, c])
bfs(graph, que)
max = 0
for b in range(n):
    for c in range(m):
        if cnt[b][c] == 0 and graph[b][c] == 0:
            print(-1)
            quit()
        elif max < cnt[b][c]:
            max = cnt[b][c]
if max == 1:
    print(0)
else:
    print(max-1)
for kk in cnt:
    print(kk)
