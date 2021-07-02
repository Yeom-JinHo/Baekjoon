n = list(map(int, (input())))
cnt = [0]*10

for l in n:
    cnt[l] += 1
sixNine = cnt[6]+cnt[9]

cnt[6] = round(sixNine/2)
cnt[9] = sixNine-cnt[6]

print(max(cnt))
