import sys

testCount=int(sys.stdin.readline())

for _ in range(testCount):
  #scores[0]<< N
  scores=list(map(int,sys.stdin.readline().split()))
  scoresAvg=sum(scores[1:])/float(scores[0])
  overAvgCount=0
  for i in range(1,len(scores)):
    if(scores[i]>scoresAvg):
      overAvgCount+=1
  print('{:.3f}%'.format(overAvgCount/scores[0]*100))

