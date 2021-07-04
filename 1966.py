for _ in range(int(input())):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    chk = [False]*n
    chk[m] = True
    cnt = 1
    while True:
        maxN = max(li)
        if li[0] == maxN:
            if chk[0]:
                print(cnt)
                break
            chk.pop(0)
            li.pop(0)
            cnt += 1
        else:
            li.append(li.pop(0))
            chk.append(chk.pop(0))
