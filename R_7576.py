# 백준 7576 토마토 
# 오랜만에 bfs/dfs 풀어보고 싶어서 풀었습니다.
# 한번 푼 문제라 10분 예상
# 실제 푼 걸린 시간

from typing import Deque

def bfs(graph, visited):
    que = Deque()
    print(graph)
    print(graph[0][0])
    for x in range(len(graph)):
      for y in range(len(graph[x])):
        if graph[x][y]==1:
          que.append([x,y])
          print(que)
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
    return day


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
cnt = [[0]*m for _ in range(n)]
graph = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
  graph.append(input().split())

print(bfs(graph, visited))

