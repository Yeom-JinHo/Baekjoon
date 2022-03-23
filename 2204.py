import sys

while True:
  N=int(sys.stdin.readline());
  if N==0:
    break;
  first =list(sys.stdin.readline().rstrip());
  for i in range(1,N):
    next=list(sys.stdin.readline().rstrip());
    for j in range(min(len(first),len(next))):
      if first[j].upper()>next[j].upper():
        first=next;
        break;
      elif first[j].upper()<next[j].upper():
        break;
      if j== min(len(first),len(next))-1:
        if len(first)>len(next):
          first=next;
  print("".join(first));