import sys
MAX_N=1299709+1;
tc=int(sys.stdin.readline());
chk=[True]*(MAX_N+1);
m=int(MAX_N**0.5);
for i in range(2,m+1):
  if chk[i]:
    for j in range(2*i, MAX_N, i):
        chk[j] = False
primes=[i for i in range(2,MAX_N) if chk[i]==True];
for _ in range(tc):
  n=int(sys.stdin.readline());
  for i in range(len(primes)):
    if n==primes[i]:
      answer=0;
      break;
    if n<primes[i]:
      answer=primes[i]-primes[i-1];
      break;
  print(answer)
  print(*[i for i in range(2,n+1) if primes[i]])