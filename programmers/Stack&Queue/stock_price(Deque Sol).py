from collections import deque

prices = [3, 1, 4, 5, 2]

# Deque로 푸는 방법
# 시간 복잡도는 O(n^2)


def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:  # prices를 모두 탐색해서 [] 되면 stop
        flag = prices.popleft()  # prices의 첫 숫자를 기준점으로 잡고
        cnt = 0

        for i in prices:  # 나머지 숫자 하나씩 다 살펴보기
            if flag > i:  # 기준 숫자보다 작다면
                cnt += 1
                break
            cnt += 1  # 기준 숫자보다 크거나 같다면 cnt+=1 하고 계속 진행
        answer.append(cnt)

    return answer


print(solution(prices))


# 은진님 코드
# from collections import deque
# def solution(prices):
#     answer = []

#     prices = deque(prices) # que로 캐스팅
#     while prices:
#         cnt = 0
#         price = prices.popleft() # First Out

#         for i in prices:
#             cnt += 1 # 카운팅
#             if price > i:
#                 break

#         answer.append(cnt)
#     return answer
