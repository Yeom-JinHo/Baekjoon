a, b = map(int, input().split())

for i in range(100001, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        print(i*(a // i)*(b // i))
        break
