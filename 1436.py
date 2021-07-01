import sys

n = int(sys.stdin.readline())
number = 666
cnt = 0
while True:
    numberS = str(number)
    if numberS.count('666') >= 1:
        cnt += 1
        if n == cnt:
            print(number)
            break
    number += 1
