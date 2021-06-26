from abc import abstractproperty

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
aparts = []
visted = [[False]*(n+1) for _ in range(n+1)]

graph = []
for i in range(n):
    graph.append(list(input()))


def dfs(x, y):
    visted[x][y] = True
    vistedApart.append([x, y])
    for d in range(4):
        tx = x+dx[d]
        ty = y+dy[d]
        if tx >= 0 and ty >= 0 and tx < n and ty < n:
            if visted[tx][ty] == False and graph[tx][ty] == '1':
                dfs(tx, ty)
    return len(vistedApart)


for x in range(n):
    for y in range(n):
        if not visted[x][y] and graph[x][y] == '1':
            vistedApart = []
            aparts.append(dfs(x, y))
aparts.sort()
print(len(aparts))
for apart in aparts:
    print(apart)
