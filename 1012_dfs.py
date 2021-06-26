import sys
sys.setrecursionlimit(10000)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, graph, visited):
    visited[y][x] = True
    for index in range(4):
        rx = x+dx[index]
        ry = y+dy[index]
        if rx >= 0 and ry >= 0 and rx < m and ry < n:
            if graph[ry][rx] == 1 and visited[ry][rx] == False:
                dfs(rx, ry, graph, visited)


n = int(input())
count = [0]*n
for i in range(n):
    m, n, k = map(int, input().split())
    graph = [[0]*(m) for _ in range(n)]
    visited = [[False]*(m) for _ in range(n)]
    for a in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for ai in range(m):
        for bi in range(n):
            if graph[bi][ai] == 1 and visited[bi][ai] == False:
                dfs(ai, bi, graph, visited)
                count[i] += 1
for countt in count:
    print(countt)
