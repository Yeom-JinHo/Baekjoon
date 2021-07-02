n, k = map(int, input().split())

li = [True]*(n+1)
cnt = 1

for i in range(2, n+1):
    if li[i] == True:
        for j in range(i, n+1, i):
            if li[j] == False:
                continue
            if cnt == k:
                print(j)

            li[j] = False
            cnt += 1
