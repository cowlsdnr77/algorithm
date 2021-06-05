import sys
import heapq

# 다익스트라 알고리즘 특징
# - 그리디 알고리즘 방식으로 동작한다. -> 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복한다
# - 음의 간선이 없을 때 정상적으로 동작한다
# - 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않는다 -> 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있다
# - 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장된다 -> 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 한다

v, e = map(int, sys.stdin.readline().split())  # v는 정점의 개수, e는 간선의 개수
k = int(sys.stdin.readline())  # 시작 정점

# 각 정점에 연결되어 있는 정점의 정보를 담는 리스트.  각각 (도착 정점번호,가중치) 형태로 저장
graph = [[] for i in range(v+1)]

# 최단 거리 테이블을 모두 무한으로 초기화
INF = int(1e9)
# INF = sys.maxsize 도 가능
distance = [INF] * (v+1)  # 각 정점까지의 최단 거리를 담는 리스트

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))  # 출발점 a, 도착점 b, 거리 c


# heapq.heappush를 사용해 우선 순위 큐 또는 힙을 쉽게 생성할 수 있다. 첫번째 인자는 heap 자체인 list이고,
# 두번째 인자는 튜플인데 튜플의 첫번째 요소는 우선순위 값, 두번째 요소는 데이터를 넣어주면 된다.
# 함수의 두번째 인자로 튜플이 아닌 일반 값을 넣어주면, 값을 기준으로 heap을 만들어준다.

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))  # (거리,위치)로 저장
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)  # 거리가 가장 작은 요소가 pop 됨
        if distance[now] < dist:  # 최단거리 리스트의 값보다 현재 거리가 크다면 탐색할 필요 없으므로
            continue

        for i in graph[now]:  # 현재 위치의 인접 노드를 탐색하여
            # 현재 위치까지의 가중치(거리)와 현재 위치에서 인접 노드까지의 가중치(거리)를 더함
            cost = dist + i[1]
            if cost < distance[i[0]]:  # cost가 인접 노드 i의 최단거리보다 작다면
                distance[i[0]] = cost  # 인접 노드 i의 최단거리를 cost로 갱신
                # (갱신된 거리, 갱신된 노드)를 우선순위 큐에 push
                heapq.heappush(queue, (cost, i[0]))


dijkstra(k)
# print(graph)
# print(distance)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
