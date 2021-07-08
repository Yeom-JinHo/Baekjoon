import sys

n = int(sys.stdin.readline())
result = 1
for i in range(1, n+1):
    result *= i
cnt = 0
ten = 10
while True:
    if result % ten == 0:
        cnt += 1
        ten *= 10
    else:
        print(cnt)
        break
