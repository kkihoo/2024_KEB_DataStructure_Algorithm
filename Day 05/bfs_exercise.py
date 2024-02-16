# https://www.acmicpc.net/problem/18352
from collections import deque


N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

distance = [-1] * (N + 1)
distance[X] = 0

queue = deque([X])
while queue:
    current = queue.popleft()
    for next in graph[current]:
        if distance[next] == -1:
            distance[next] = distance[current] + 1
            queue.append(next)

check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)
