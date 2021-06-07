# 스택으로 푸는 방법
# 시간복잡도 O(n)
# 참고: https://gurumee92.tistory.com/170

prices = [1, 2, 3, 2, 3]


def solution(prices):
    n = len(prices)
    # 1. answer를 prices 길이와 맞춘다.
    answer = [0] * n
    # 2. 스택 생성
    st = []
    # 3. 0 ~ n-1 초까지 순회
    for i in range(n):
        # 1. 스택 비지 않고, prices[top] > prices[i] 이라면 다음 반복
        # 1-1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 1-2. answer[top]에 i - top을 저장
        while st and prices[st[-1]] > prices[i]:
            top = st.pop()
            answer[top] = i - top
        # 2. 스택에 현재 시간 i 저장
        st.append(i)

    # 4. 만약 스택이 남아있다면, 스택이 빌 때까지 다음 반복
    while st:
        # 1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 2. answer[top]에 가장 마지막 시간 n - i 에서 top을 뺸 시간 저장
        top = st.pop()
        answer[top] = n - 1 - top

    return answer


print(solution(prices))
