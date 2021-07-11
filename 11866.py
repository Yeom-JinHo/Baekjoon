from typing import Deque


n, k = map(int, input().split())

ls = [i for i in range(1, n+1)]

result = []
index = 0
while ls:
    index += (k-1)
    index %= len(ls)
    result.append(ls[index])
    del ls[index]

result = str(result).replace('[', '<').replace(']', '>')
print(result)
