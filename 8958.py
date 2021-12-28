import sys

n=int(sys.stdin.readline())

for _ in range(n):
  input=sys.stdin.readline().rstrip()
  result=0
  score=0
  for i in input:
    if(i=='X'):
      score=0
    elif(i=='O'):
      score+=1
    result+=score
  print(result)
