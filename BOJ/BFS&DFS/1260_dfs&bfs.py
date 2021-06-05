import sys
from collections import deque


def dfs(graph, start_node):
    stack = [start_node]
    visited = []

    while stack:
        current_node = stack.pop()
        # 내가 생각한 코드
        # if current_node in visited:
        #     continue
        # visited.append(current_node)
        # for i in range(len(graph[current_node])-1, -1, -1):  # 작은 번호부터 방문하기위해서
        #     if graph[current_node][i] not in visited:
        #         stack.append(graph[current_node][i])
        #         # print(stack)

        # 더 나은 방식
        if current_node not in visited:
            visited.append(current_node)
            # reversed 는 내장함수로, list에서 제공하는 함수가 아니다.
            stack += reversed(graph[current_node])  # 작은 번호부터 방문하기위해서
    return visited


def bfs(graph, start_node):
    queue = deque()
    queue.append(start_node)
    visited = []

    while queue:
        current_node = queue.popleft()
        visited.append(current_node)
        for adj_node in graph[current_node]:
            if adj_node not in visited and adj_node not in queue:  # node가 중복되어 visited에 들어가는것 방지
                queue.append(adj_node)
    return visited


n, m, v = map(int, sys.stdin.readline().split())

graph = {}

# 그래프를 딕셔너리로 만들기
for i in range(n):  # 딕셔너리에 i : [] 형태로 key와 value 초기화
    graph[i+1] = []

# 딕셔너리에 값 추가  #{1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]}
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i+1].sort()

# print(graph)
print(*dfs(graph, v))
print(*bfs(graph, v))
