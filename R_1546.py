import sys

n=int(sys.stdin.readline())
input=list(map(int,sys.stdin.readline().split()))

print(sum(input)/float(max(input))*100/len(input))
