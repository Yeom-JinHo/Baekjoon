def bCheck(r, c):
    cnt = 0
    for dr in range(0, 8):
        for dc in range(0, 8):
            if chess[r+dr][c+dc] != bChess[dr][dc]:
                cnt += 1
    return cnt


def wCheck(r, c):
    cnt = 0
    for dr in range(0, 8):
        for dc in range(0, 8):
            if chess[r+dr][c+dc] != wChess[dr][dc]:
                cnt += 1
    return cnt


m, n = map(int, input().split())

wChess = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW',
          'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
bChess = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB',
          'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
chess = list()
for i in range(m):
    chess.append(input())
bCnt, wCnt = [], []
for r in range(m-7):
    for c in range(n-7):
        bCnt.append(bCheck(r, c))
        wCnt.append(wCheck(r, c))

print(min(min(bCnt), min(wCnt)))
