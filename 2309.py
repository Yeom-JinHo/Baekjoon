import sys

li=list()

for _ in range(9):
  li.append(int(sys.stdin.readline().rstrip()))
for i in range(9):
  for j in range(i+1,9):
    if (sum(li)-li[i]-li[j]==100):
      li[i]=0
      li[j]=0
      li.sort()
      for l in li:
        if(l!=0):
          print(l)
      exit()