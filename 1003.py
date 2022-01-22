from glob import glob
import sys
def fibonacci(n):
    global dp;
    return [dp[n-1][0]+dp[n-2][0],dp[n-1][1]+dp[n-2][1]];

dp=list();
dp.append([1,0]);
dp.append([0,1]);
for i in range(2,40+1):
  dp.append(fibonacci(i));
testCase=int(sys.stdin.readline());
for _ in range(testCase):
  zc,oc=dp[int(sys.stdin.readline())];
  print(zc,oc);
