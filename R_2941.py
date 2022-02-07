import sys

ls=['1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ','0']

words=sys.stdin.readline().rstrip()
result=0

for word in words:
  for l in ls:
    if word in l:
      result+=ls.index(l)+2
      break
    
print(result)