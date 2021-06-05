import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {}

for i in range(n):  # 딕셔너리에  i : [] 형태로 key 와 value 초기화
    graph[i+1] = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs_stack(adj_graph, start_node):  # g: 그래프, v: 시작 노드
    stack = [start_node]  # 스택에 시작 노드 넣어줌
    v = []
    while stack:
        cur = stack.pop()
        v.append(cur)
        for adj_node in adj_graph[cur]:
            if adj_node not in v and adj_node not in stack:
                stack.append(adj_node)
    return len(v)-1


# print(graph)
print(dfs_stack(graph, 1))
