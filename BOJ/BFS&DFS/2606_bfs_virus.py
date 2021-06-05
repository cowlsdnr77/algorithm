import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {}

for i in range(n):  # 딕셔너리에 i : [] 형태로 key와 value 초기화
    graph[i+1] = []


for i in range(m):  # 딕셔너리에 연결을 추가
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 1. 시작 노드를 큐에 넣는다
# 2. 현재 큐의 노드(가장 앞에 있는 노드)를 빼서 visited 에 추가
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가


def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited = []

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        # graph 에서 current_node와 인접한 node들에 대해 반복문
        for adj_node in adj_graph[current_node]:
            if adj_node not in visited and adj_node not in queue:  # node가 중복되어 visited에 들어가는것 방지
                queue.append(adj_node)
    return len(visited)-1


print(bfs_queue(graph, 1))
