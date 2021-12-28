def solve(limit):
  selfNums=list()
  for i in range(1,limit+1):
    selfNums.append(i)
  for i in range(1,limit+1):
    # while(True):
      nextNum=i+sum(map(int,str(i)))
      if(nextNum in selfNums):
        selfNums.remove(nextNum)
      # else:
        # break
  for selfNum in selfNums:
    print(selfNum)

solve(10000)



