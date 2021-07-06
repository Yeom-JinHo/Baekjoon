from collections import deque
import sys


def bfs(start, graph, visted):
    if visted[start] == False:
        que = deque([start])
        visted[start] = True
        while que:
            v = que.popleft()
            for i in graph[v]:
                if not visted[i]:
                    que.append(i)
                    visted[i] = True
        return True
    else:
        return False


n, m = map(int, (sys.stdin.readline().split()))


graph = [[] for _ in range(n+1)]
visted = [False]*(n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)
cnt = 0
for i in range(1, n+1):
    if bfs(i, graph, visted):
        cnt += 1

print(cnt)
