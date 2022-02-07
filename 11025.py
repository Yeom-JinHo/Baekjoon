import sys
N,K=map(int,sys.stdin.readline().split());
result=0;
print("i",end=" ");
print("r",end=" ");
print("rr",end=" ");
print("re",end=" ");
print();
rr=0;
for i in range(1,N+1):
  result=(result+K)%i
  rr=rr+K;
  print(i,end=" ")
  print(result,end=" ")
  print(rr,end=" ")
  print()
print(result+1)


# 3 6 9 12 15 18 21 28
# 0 0 0  0  0  0  0  0
