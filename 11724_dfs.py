import sys
sys.setrecursionlimit(100000)


def dfs(start, graph, visited):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(i, graph, visited)


n, m = map(int, (sys.stdin.readline().split()))

visited = [False]*(n+1)
graph = [[0] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, (sys.stdin.readline().split()))
    graph[v].append(u)
    graph[u].append(v)

cnt = 0
for k in range(1, n+1):
    if visited[k] == False:
        dfs(k, graph, visited)
        cnt += 1
print(cnt)
