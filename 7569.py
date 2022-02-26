from collections import deque
from sys import stdin


def bfs(graph, que):
    while que:
        x,y,z=que.popleft();
        for i in range(6):
            rx = x+dx[i]
            ry = y+dy[i]
            rz = z+dz[i]
            if rx >= 0 and ry >= 0 and rz >= 0 and rx < h and ry < n and rz < m:
                if graph[rx][ry][rz] == 0:
                    graph[rx][ry][rz]=graph[x][y][z]+1;
                    que.append([rx, ry, rz])

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

m, n, h = map(int, stdin.readline().rstrip().split())

graph = []
que = deque()
for _ in range(h):
    tgraph = []
    for _ in range(n):
        tgraph.append(list(map(int, stdin.readline().rstrip().split())))
    graph.append(tgraph)
for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c] == 1:
                que.append([a, b, c])
bfs(graph, que)
max = 0
for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c]==0:
                print(-1)
                quit()
            elif max < graph[a][b][c]:
                max = graph[a][b][c]

if max == 1:
    print(0)
else:
    print(max-1)
