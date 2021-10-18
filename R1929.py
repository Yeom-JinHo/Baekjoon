m, n = map(int, input().split())

result = []
for i in range(m, n+1):
    cnt = 0
    for k in range(2, i):
        if i % k == 0:
            cnt += 1
    if cnt < 1:
        result.append(i)

for re in result:
    print(re)
