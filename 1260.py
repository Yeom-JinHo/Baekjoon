n, m, v = map(int, input().split())
print(n, m, v)
nodes = []

for n in range(m):
    nodes.append(list(map(int, input().split())))
print(nodes)
graph = [[] for _ in range(n+1)]
print(graph)
for node in nodes:
    graph[node[0]].append(node[1])
    graph[node[1]].append(node[0])

print(graph)
