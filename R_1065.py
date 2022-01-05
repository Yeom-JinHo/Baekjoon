import sys

def solve(limit):
  ls=[]
  for num in range(1,limit+1):
    if(num<100 or num//100-num//10%10==num//10%10-num%10):
      ls.append(num)
  return ls

input=int(sys.stdin.readline())
print(len(solve(input)))