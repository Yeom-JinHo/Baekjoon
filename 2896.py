import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
days = 1
v = v-a
days += math.ceil(v/((a-b)*1.0))

print(days)
