from collections import deque
from typing import Deque


def dfs(root, visited):
    visited[root] = True
    print(root, end=' ')
    for i in range(n+1):
        if visited[i] == False and graph[root][i] == 1:
            dfs(i, visited)


def bfs(root, visited):
    visited[root] = True
    que = deque([root])
    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in range(n+1):
            if visited[i] == False and graph[v][i] == 1:
                que.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [False]*(n+1)
dfs(v, visited)
print()
visited = [False]*(n+1)
bfs(v, visited)
print()
