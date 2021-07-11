# P는 응시자가 앉아있는 자리를 의미합니다.
# O는 빈 테이블을 의미합니다.
# X는 파티션을 의미합니다.

# 맨해튼 거리가 2 이하 일때 파티션 없으면 거리두기 X
# 맨해튼 거리가 2 이하 일때 파티션으로 막혀있으면 거리두기 O


# places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
#                                                                                                          "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

places = [["PPPPP", "XXXXX", "XXXXX", "XXXXX", "XXXXX"]]
# bfs 로 풀어보자
# 참가자위치 기준으로 상하좌우를 검사하고 (거리1)
# 상하좌우에서 다시 각각 상하좌우를 검사할때 (거리2)
# 검사 도중 O나 P가 발견되면 바로 검사 종료

# 그럼 bfs로는 어떻게 풀어야되나
# bfs는 우선 Queue로 구현가능하다.
# visited라는 방문 노드를 담는 리스트를 하나 만들어 놓는다.
# 각 노드는 -1 < <5 사이의 x,y 좌표로 이뤄져 있다.


def confirm_p(place, p):  # 테스트케이스 8번 빼고 모두 성공... 8번은 반례를 못찾겠음
    visited = []
    queue = [p]
    # print(queue)
    # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for _ in range(2):  # 이 부분이 잘못 구현됨 // 큐가 비어있기 전까지 반복문 돌고 탈출조건은 visited에 따로 거리값을 줘서 거리값이 3보다 클때 break해줘야됨
        if len(queue) == 0:
            break
        current_node = queue.pop(0)
        visited.append(current_node)
        for j in range(4):
            if -1 < current_node[0]+dx[j] < 5 and -1 < current_node[1]+dy[j] < 5:
                next_val = place[current_node[0]+dx[j]][current_node[1]+dy[j]]
                next_node = (current_node[0]+dx[j], current_node[1]+dy[j])
                # print("X:", current_node[0]+dx[j])
                # print("Y:", current_node[1]+dy[j])
                if next_val == "X":
                    continue
                elif next_val == "P" and next_node not in visited:
                    return 0
                if next_node not in visited:
                    queue.append(next_node)

    return 1


def confirm_p2(place, p):  # confirm_p3을 토대로 내 로직을 바꿈
    visited = [[0] * 5 for _ in range(5)]
    visited[p[0]][p[1]] = 1
    queue = [p]
    # print(queue)
    # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while queue:
        current_x, current_y = queue.pop(0)
        if visited[current_x][current_y] == 3:  # 거리가 2를 넘어 3이 된다면 탈출
            break
        for i in range(4):
            # 아직 방문안한 노드일 경우
            if (0 <= current_x + dx[i] < 5) and (0 <= current_y + dy[i] < 5) and visited[current_x+dx[i]][current_y+dy[i]] == 0:
                if place[current_x+dx[i]][current_y+dy[i]] == 'X':
                    continue
                elif place[current_x+dx[i]][current_y+dy[i]] == 'P':
                    return 0  # 수칙위반 걸리는 순간 종료
                else:  # 사람이 앉지 않은 빈 자리일때
                    visited[current_x+dx[i]][current_y+dy[i]
                                             ] = visited[current_x][current_y] + 1
                    queue.append((current_x+dx[i], current_y+dy[i]))
    return 1


def confirm_p3(place, p):  # 프로그래머스 다른 사람 풀이 참조
    visited = [[0] * 5 for _ in range(5)]
    visited[p[0]][p[1]] = 1
    queue = [p]
    # print(queue)
    # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while queue:
        current_x, current_y = queue.pop(0)
        if visited[current_x][current_y] == 3:
            break
        for i in range(4):
            if (0 <= current_x + dx[i] < 5) and (0 <= current_y + dy[i] < 5) and place[current_x+dx[i]][current_y+dy[i]] != 'X' and visited[current_x+dx[i]][current_y+dy[i]] == 0:
                if place[current_x+dx[i]][current_y+dy[i]] == 'P':
                    return 0  # 수칙위반 걸리는 순간 종료
                else:  # 사람이 앉지 않은 빈 자리일때
                    visited[current_x+dx[i]][current_y+dy[i]
                                             ] = visited[current_x][current_y] + 1
                    queue.append((current_x+dx[i], current_y+dy[i]))
    return 1


def solution(places):
    answer = []
    for place in places:
        p_tuple_list = []
        place_confirm_list = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    p_tuple_list.append((i, j))
        print("p_tuple_list: ", p_tuple_list)
        for i in range(len(p_tuple_list)):
            if confirm_p2(place, p_tuple_list[i]) == 0:
                place_confirm_list.append(0)
            else:
                place_confirm_list.append(1)
        print("place_confirm_list: ", place_confirm_list)
        if 0 in place_confirm_list:
            answer.append(0)
        else:
            answer.append(1)

    return answer


print(solution(places))
