import sys

n, m = map(int, sys.stdin.readline().split())
4 2
visited = [False]*n  # 이미 방문한 노드(값)이라면 다음 노드를 탐색하도록 하기 위함 [f,f,f,f]
search_path = [0]*m  # 탐색과정에서 방문한 노드 값을 담을 리스트 [0,0]


def dfs(n, m, depth):
    if depth == m:  # depth(탐색 깊이 = 출력 리스트 길이)가 m과 같으면 출력
        print(*search_path)
        return  # 함수 호출한 곳으로 이동

    # 재귀하면서 백트래킹할 반복문 구현
    for i in range(n):  # 0부터 n-1까지 반복 0~3 0~3
        if not visited[i]:  # 해당 노드(i번째 노드)를 방문하지 않았다면
            visited[i] = True  # 해당 노드를 방문상태(True)로 변경 [t,f,f,f]
            # 해당 깊이를 index로 하여 i+1 값 저장 [0,0] -> [1,0] -> [1,2]
            search_path[depth] = i + 1
            dfs(n, m, depth+1)  # 다음 자식 노드 방문을 위해 depth(탐색 깊이)를 1 증가시키면서 재귀 호출

            # 자식 노드 방문이 끝나고 돌아오면 다음 탐색을 위해 방문 노드를 방문하지 않은 상태(False)로 변경
            visited[i] = False


dfs(n, m, 0)
