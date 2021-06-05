import sys
from collections import deque

# bfs
# 토마토


def bfs_queue(n, m, loc_list):
    queue = deque()
    result = -1

    ## 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if loc_list[i][j] == 1:
                queue.append((i, j))

    # print(queue)

    while queue:
        for _ in range(len(queue)):
            curr_y, curr_x = queue.popleft()

            for i in range(4):  # 상하좌우 인접 토마토 위치 찾기
                next_y = curr_y + dy[i]
                next_x = curr_x + dx[i]

                if 0 <= next_y < n and 0 <= next_x < m and loc_list[next_y][next_x] == 0:
                    loc_list[next_y][next_x] = 1
                    queue.append((next_y, next_x))
        # print(loc_list)
        # print(queue)

        result += 1

    for i in range(n):
        for j in range(m):
            if loc_list[i][j] == 0:
                return -1

    return result


m, n = map(int, sys.stdin.readline().split())

tomato_list = []

# 토마토 위치를 2차원 리스트로 저장 # tomato_list = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    tomato_list.append(row)

print(bfs_queue(n, m, tomato_list))
