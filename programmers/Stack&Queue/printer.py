from collections import deque

# 양방향 큐를 활용해서 문제를 풀자


priorities = [1, 1, 9, 1, 1, 1]
location = 0


def solution(priorities, location):
    answer = 0
    index_list = deque([i for i in range(0, len(priorities))])  # 인덱스 리스트
    priorities = deque(priorities)

    while priorities:
        now = priorities[0]
        if max(priorities) > now:
            now = priorities.popleft()
            priorities.append(now)
            now_index = index_list.popleft()
            index_list.append(now_index)
        else:
            priorities.popleft()
            pop_index = index_list.popleft()
            answer += 1
            if location == pop_index:
                return answer


def solution2(priorities, location):  # enumerate로 간단하게 튜플을 만들 수 있음
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


print(solution2(priorities, location))
