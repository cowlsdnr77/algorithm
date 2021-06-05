import sys
from collections import deque

# deque를 쓰되 popleft()는 사용가능하지만, pop()는 쓰면 안됨
# 2번연산(왼쪽으로 한칸 이동), 3번연산(오른쪽으로 한칸 이동) 의 합의 최소값을 출력하는 문제


n, m = map(int, sys.stdin.readline().split())

# 입력 조건(m개만큼 입력)은 따로 구현 안함 -> 채점 시 문제 생길수 있음
location_list = list(map(int, sys.stdin.readline().split()))

q_list = []  # 원소 1 ~ 원소 n 까지 담을 QUEUE

for i in range(n):  # 원소 1 ~ 원소 n 까지 값 추가
    q_list.append(i+1)

q_list = deque(q_list)

cnt = 0


# 어쨌든 location_list의 원소값이 위치하고 있는 곳을 알아야됨
# pop
for i in range(len(location_list)):

    while q_list[0] != location_list[i]:
        qList = [0, 1, 2.3, 4, 5, 6, 7]
        if q_list.index(location_list[i]) <= len(q_list)-q_list.index(location_list[i]):
            temp = q_list.popleft()
            q_list.append(temp)
            print("left rotate")
            print(q_list)
        else:
            temp = q_list.pop()
            q_list.appendleft(temp)
            print("right rotate")
            print(q_list)
        cnt += 1

    if q_list[0] == location_list[i]:
        q_list.popleft()
        print("pop")
        print(q_list)

print(cnt)
