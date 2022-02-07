import sys

a,b=sys.stdin.readline().split()
a,b=a[::-1],b[::-1]
print(a if a>b else b)
