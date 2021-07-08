dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input()))

visted = [[False]*n for _ in range(n)]

for x in n:
    for y in n:
        if visted[x][y] == False:
            dfs(x, y, graph, visted)
