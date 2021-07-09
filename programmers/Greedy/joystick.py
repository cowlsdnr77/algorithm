
# PS
# 첫 글자부터 만들어나간다.
# 단 알파벳을 바꿀때 뒤에서부터가 빠른지 앞에서부터가 빠른지 계산해야됨
# 왼쪽 진행과 오른쪽 진행을 다 해보고 최소를 더한다..?

# 아니면 그냥 현재 위치에서 오른쪽 왼쪽 비교해서 더 많은 횟수가 필요한거 먼저 처리한다.


# 다시 생각해보자
# 먼저 상하 조작으로 각 위치에서 name의 위치 알파벳을 만드는 횟수 리스트 만들어놓고
# 좌우 조작은 매 위치에서 왼쪽/오른쪽으로 이동하며 상하 조작이 처음 나오는 위치까지 조작횟수를 비교해서 적은 방향으로 이동한다.
# name을 만족할때까지 반복
name = "JEROEN"


def solution(name):
    answer = 0
    change_list = [min(ord(n) - ord("A"), ord("Z") - ord(n) + 1) for n in name]
    index, answer = 0, 0

    while True:
        answer += change_list[index]  # 현재 인덱스의 상하 조작횟수를 answer에 더하고
        change_list[index] = 0  # change_list의 현재 인덱스 값을 0으로 변경

        if sum(change_list) == 0:  # 모든 change_list의 값을 다 answer에 더하고 change_list의 값들이 다 0이라면 break
            break

        left, right = 1, 1
        # 왼쪽으로 이동하면서 값을 바꿔야 하는 위치가 나오기 전까지 left += 1
        while change_list[index-left] == 0:
            left += 1

        # 오른쪽으로 이동하면서 값을 바꿔야 하는 위치가 나오기 전까지 right += 1
        while change_list[index+right] == 0:
            right += 1
        # left: 현재 인덱스(index)에서 값을 변경해야하는 다음 인덱스까지 왼쪽으로 이동한 횟수
        # right: 현재 인덱스(index)에서 값을 변경해야하는 다음 인덱스까지 오른쪽으로 이동한 횟수
        answer += left if left < right else right  # left와 right 중 작은 값을 answer에 더함
        # index도 left와 right 중 작은 쪽으로 움직이고 난 다음 index로 바꿈
        index += -left if left < right else right

    return answer


print(solution(name))
