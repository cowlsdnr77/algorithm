import math

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

# 기능개발


def solution(progresses, speeds):
    answer = []

    for i in range(len(progresses)):
        # 작업 일수 [5, 10, 1, 1, 20, 1]
        progresses[i] = math.ceil((100-progresses[i])/speeds[i])

    front = 0  # 기준점

    for i in range(len(progresses)):
        if progresses[front] < progresses[i]:  # front보다 i가 큰 경우에는 기능 배포
            answer.append(i-front)  # 배포되는 기능 개수는 i-front
            front = i  # 기준점을 i로 바꿔줌

    answer.append(len(progresses)-front)  # 마지막에는 전체 개수에서 마지막 기준점 index를 뺴면 됨

    return answer


print(solution(progresses, speeds))


# 은진님 풀이
# deque 로 풀면 popleft해서 시간 절약할 수 있음
# def solution(progresses, speeds):
#     answer = []
#     time = 0
#     count = 0

#     while len(progresses) > 0:
#         if(progresses[0] + speeds[0] * time >= 100): # 진도율 100%가 넘을 경우
#             progresses.pop(0) # 확인한 진도, 속도 제거
#             speeds.pop(0)
#             count += 1 # 카운팅
#         else:
#             if count > 0: # 진도율 100% 안 넘을 경우
#                 answer.append(count)
#                 count = 0
#             time += 1 # 작업 일수 늘리기


#     answer.append(count)
#     return answer
