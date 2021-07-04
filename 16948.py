dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

n = int(input())
sx, sy, ex, ey = map(int, input().split())
visted = [[False]*n for _ in range(n)]
cnt = [[0]*n for _ in range(n)]

que = [[sx, sy]]
visted[sx][sy] = True

while que:
    x, y = que[0][0], que[0][1]
    del que[0]
    if x == ex and y == ey:
        print(cnt[x][y])
        quit()
    for d in range(6):
        tx = x+dx[d]
        ty = y+dy[d]
        if tx >= 0 and ty >= 0 and tx < n and ty < n:
            if visted[tx][ty] == False:
                visted[tx][ty] = True
                que.append([tx, ty])
                cnt[tx][ty] = cnt[x][y]+1
print(-1)
