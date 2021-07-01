

def bfs(visited, sx, sy, ex, ey):
    visited[sx][sy] = True
    que = [[sx, sy]]
    while que:
        x, y = que[0][0], que[0][1]
        del que[0]
        if x == ex and y == ey:
            return cnt[x][y]
        for a in range(8):
            tx = x+dx[a]
            ty = y+dy[a]
            if tx >= 0 and tx < l and ty >= 0 and ty < l:
                if visited[tx][ty] == False:
                    que.append([tx, ty])
                    cnt[tx][ty] = cnt[x][y]+1
                    visited[tx][ty] = True


dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
n = int(input())
result = list()
for i in range(n):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    visited = [[False]*l for _ in range(l)]
    cnt = [[0]*(l+1) for _ in range(l+1)]
    print((bfs(visited, sx, sy, ex, ey)))
