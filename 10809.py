import sys
result=[]
text=sys.stdin.readline().rstrip()

for i in range(ord('a'),ord('z')+1):
  result.append(text.find(chr(i)))

for a in result:
  print(a,end=' ')