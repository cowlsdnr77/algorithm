import math

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    answer = []

    for i in range(len(progresses)):
        progresses[i] = math.ceil((100-progresses[i])/speeds[i])  # 작업 일수

    front = 0

    for i in range(len(progresses)):
        if progresses[front] < progresses[i]:
            answer.append(i-front)
            front = i

    answer.append(len(progresses)-front)

    return answer


print(solution(progresses, speeds))
