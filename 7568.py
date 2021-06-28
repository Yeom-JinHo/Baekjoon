n = int(input())
ls = list()
rate = list()
for i in range(n):
    ls.append(list(map(int, input().split())))

for x in range(n):
    cnt = 1
    for y in range(n):
        if ls[x][0] < ls[y][0] and ls[x][1] < ls[y][1]:
            cnt += 1
    rate.append(cnt)

for r in rate:
    print(r, end=' ')
