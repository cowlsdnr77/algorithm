import math

progresses = [93, 30, 55]
speeds = [1, 30, 5]

# 스택으로 풀었다고 하기도 뭐하지만 풀기는 풀었다.
# 역시 성능도 My Sol이 더 좋다.


def solution(progresses, speeds):
    answer = []
    stack = []
    cnt = 0

    for i in range(len(progresses)):
        progresses[i] = math.ceil((100-progresses[i])/speeds[i])  # 작업 일수

    stack.append(progresses[0])

    flag = stack[-1]  # 기준 설정

    for i in range(1, len(progresses)):
        if flag >= progresses[i]:
            stack.pop()
            cnt += 1
            stack.append(progresses[i])

        else:
            stack.pop()
            cnt += 1
            answer.append(cnt)
            stack.append(progresses[i])
            flag = stack[-1]  # 새로운 기준
            cnt = 0

    answer.append(cnt+1)
    return answer


print(solution(progresses, speeds))
