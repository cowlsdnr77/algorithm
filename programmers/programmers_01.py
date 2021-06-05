prices = [1, 2, 3, 2, 3]


def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-2):
        cnt = 1
        for j in range(1, len(prices)-1):
            if prices[i] < prices[j]:
                cnt += 1
            else:
                break
            answer[i] = cnt
    answer[-1] = 1

    return answer


print(solution(prices))
