import sys

arr=list();
maxC=0;
answer=0;
for _ in range(10):
  inp=int(sys.stdin.readline())
  arr.append(inp);
  if maxC<arr.count(inp):
    maxC=arr.count(inp);
    answer=inp;
print(sum(arr)//10);
print(answer);
print(arr.index(max(arr)));