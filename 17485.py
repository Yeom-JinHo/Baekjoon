import sys

R,C = map(int,sys.stdin.readline().split())

arr=list()
for _ in range(R):
  arr.append(list(map(int,sys.stdin.readline().split())));

dp=[[[sys.maxsize]*(C) for _ in range(R)] for _ in range(3)];

for i in range(3):
    for c in range(C):
        dp[i][0][c] = arr[0][c];


for r in range(1,R):
  for c in range(C):
    for i in range(3):
      # i는 지금 진행할 방향
        dp[i][r][c] = min(
                dp[0][r - 1][c - 1] + arr[r][c] if i != 0 and c - 1 >= 0 else sys.maxsize,
                dp[1][r - 1][c] + arr[r][c] if i != 1 else sys.maxsize,
                dp[2][r - 1][c + 1] + arr[r][c] if i != 2 and c + 1 < C else sys.maxsize,
            )

answer=sys.maxsize;

for i in range(3):
  for c in range(C):
    answer=min(answer,dp[i][R-1][c]);

print(answer)

