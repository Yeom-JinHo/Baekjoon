from typing import Deque


def bfs(x, y, graph, visited):
    visited[x][y] = True
    que = Deque([x, y])
    cnt[x][y] = 1
    while que:
        v = que.popleft()
        if v == 0:
            x, y = 0, 0
        else:
            x, y = v[0], v[1]
        for i in range(4):
            rx = x+dx[i]
            ry = y+dy[i]
            if rx >= 0 and ry >= 0 and rx < n and ry < m:
                if graph[rx][ry] == 1 and visited[rx][ry] == False:
                    que.append([rx, ry])
                    visited[rx][ry] = True
                    cnt[rx][ry] = cnt[x][y]+1


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
cnt = [[0]*m for _ in range(n)]
graph = []
visited = [[False]*m for _ in range(n)]
for a in range(n):
    graph.append(list(map(int, input())))
bfs(0, 0, graph, visited)
print(cnt[n-1][m-1])
