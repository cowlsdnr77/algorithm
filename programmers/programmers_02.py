import math
from collections import deque

progresses = [93, 30, 55]
speeds = [1, 30, 5]


def solution(progresses, speeds):
    answer = []

    works = [0]*len(progresses)
    complete_list = []
    complete_list = deque(complete_list)
    cnt = 0

    for i in range(len(progresses)):
        works[i] = math.ceil((100-progresses[i])/speeds[i])

    print(works)

    for i in range(len(works)):
        print(works[i])
        if len(complete_list) == 0:
            complete_list.append(works[i])
            print(complete_list)
            continue

        if complete_list[0] >= works[i]:
            complete_list.append(works[i])
            print(complete_list)
        else:
            while len(complete_list) != 0:
                complete_list.popleft()
                print(complete_list)
                cnt += 1
            answer.append(cnt)
            cnt = 0
    return answer


print(solution(progresses, speeds))
