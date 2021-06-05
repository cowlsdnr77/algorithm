import sys

n, m = map(int, sys.stdin.readline().split())

search_path = [0]*m  # 탐색과정에서 방문한 노드 값을 담을 리스트

# at 변수는 현재 위치, 즉 어디서부터 시작하는 지를 의미하는 변수(1부터 n까지 가능)

# at 변수로 인해 중복방문인지를 고려할 필요가 없으므로 boolean 배열(visited)로 중복 여부를 체크할 필요 또한 없다.


def dfs(at, depth):
    if depth == m:  # depth(탐색 깊이 = 출력 리스트 길이)가 m과 같으면 출력
        print(*search_path)
        return  # 함수 호출한 곳으로 이동

    # 재귀하면서 백트래킹할 반복문 구현 (i 는 at 부터 탐색하도록 한다)
    for i in range(at, n+1):  # at부터 n까지
        search_path[depth] = i  # 현재 깊이를 index로 하여 해당 위치에 i 값을 담는다.
        # 현재 i 값보다 다음 재귀에서 더 커야하므로 i+1 의 값을 넘겨주고, 깊이 또한 1 증가시켜 재귀호출해준다.
        dfs(i+1, depth+1)


dfs(1, 0)
