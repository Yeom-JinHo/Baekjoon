import sys
n = int(sys.stdin.readline())
cnt = 0
lastNum, layer = 1, 1
while lastNum < n:
    lastNum += 6*layer
    layer += 1
print(layer)
