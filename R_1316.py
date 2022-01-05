import sys

n=int(sys.stdin.readline())
for _ in range(n):
  words=list(sys.stdin.readline().rstrip())
  ls=list()
  for word in words:
    if word in ls:
      if ls[-1]!=word:
        n-=1
        break
    else:
      ls.append(word)
  print(ls)
print(n)