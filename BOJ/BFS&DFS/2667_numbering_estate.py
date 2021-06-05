import sys

# dfs

n = int(sys.stdin.readline())
house_location = [list(map(int, sys.stdin.readline().rstrip()))
                  for _ in range(n)]  # 집 위치 리스트

estate_group = []  # 단지 리스트
cnt = 0  # 단지의 집 개수 count

visited = [[False] * n for _ in range(n)]  # 방문체크 리스트

## 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 내 생각
# for 문으로(0, 0)부터 순차탐색하다가
# 1을 찾으면 0으로 바꾸고 상하좌우 찾아가면서 1찾고 0으로 바꿈
# 상하좌우 다 0이면(0, 1)부터 다시 순차탐색

def dfs(x, y):

    global cnt
    cnt += 1
    visited[x][y] = True

    for i in range(4):  # (x,y)의 상하좌우 좌표 탐색
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_y < n and 0 <= next_x < n:
            # (next_x,next_y)의 값이 1 이고 아직 방문하지 않은 좌표라면 dfs 재귀함수 호출
            if house_location[next_x][next_y] == 1 and visited[next_x][next_y] == False:
                dfs(next_x, next_y)


# 모든 좌표 확인해서 시작점이 될수있는지 확인
for i in range(n):
    for j in range(n):
        if house_location[i][j] == 1 and visited[i][j] == False:  # 시작점으로 가능하면 dfs 함수 호출
            cnt = 0
            dfs(i, j)
            estate_group.append(cnt)


# 출력
print(len(estate_group))
estate_group.sort()
for i in estate_group:
    print(i)
