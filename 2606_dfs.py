n = int(input())
m = int(input())


def dfs(root):
    visited[root] = True
    for i in range(n+1):
        if visited[i] == False and graph[root][i] == 1:
            dfs(i)


graph = [[0]*(n+1)for _ in range(n+1)]
visited = [False]*(n+1)
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
dfs(1)
print(visited.count(True)-1)
