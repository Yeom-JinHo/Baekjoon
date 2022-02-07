# 백준 2447
# 예상 시간 : 10분
# 소요 시간 : 20분
# 문제 선정 이유 : 오랜만에 별찍기를 해보고 싶었는데 이게 가장 어려워 보여서
# 시간이 오래걸린 이유 : 재귀 규칙을 찾느라고 오래걸린거 같다. 그리고 더 간단한 재귀로 풀 수 있을수도? 머리아파서 더 못풀겠다.


def dStar(x, y, dep, stars):
    for i in range(x, x+dep):
        for k in range(y, y+dep):
            stars[i][k] = ' '


def pStar(x, y, dep, stars):
    if dep == 3:
        stars[x+1][y+1] = ' '
    else:
        for dx in range(x, x+dep, dep//3):
            for dy in range(y, y+dep, dep//3):
                if dx == x+dep//3 and dy == y+dep//3:
                    dStar(dx, dy, dep//3, stars)
                else:
                    pStar(dx, dy, dep//3, stars)


n = int(input())
stars = [['*']*n for _ in range(n)]
pStar(0, 0, n, stars)
for row in stars:
    for star in row:
        print(star, end='')
    print()
