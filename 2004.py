import sys
def countN(n,i):
  count=0;
  while n:
    n//=i;
    count+=n;
  return count;

n,m=map(int,sys.stdin.readline().split());

count2=countN(n,2)-countN(n-m,2)-countN(m,2);
count5=countN(n,5)-countN(n-m,5)-countN(m,5);
print(min(count2,count5))



