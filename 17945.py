import sys,math

A,B=map(int,sys.stdin.readline().rstrip().split());
if(A*A-B==0):
  print(-A);
elif(A*A-B>0):
  print(int((-A-math.sqrt(A*A-B))),end=" ");
  print(int((-A+math.sqrt(A*A-B))));