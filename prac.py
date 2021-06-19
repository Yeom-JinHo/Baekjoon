n, m = map(int, input().split())
visited = [False] * n
result = []
def solve(depth, n, m):
    if depth == m:
        print(result)
        print(' '.join(map(str, result)))
        return
    else:
        for i in range(len(visited)):
            if not visited[i]:
                visited[i] = True
                result.append(i+1)
                solve(depth+1, n, m)
                visited[i] = False
                result.pop()
solve(0, n, m)

