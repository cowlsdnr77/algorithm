# 제한 사항
# N은 1이상 9 이하
# number은 1이상 32,000 이하
# 수식에는 괄호와 사칙연산만 가능
# 나머지 연산에서 나머지는 무시
# 최소값이 8보다 크면 -1을 리턴

# 횟수 1인 경우 -> N과 number가 같은 경우
# -> n
# 횟수 2인 경우
# -> n + n, n - n, n * n, n / n
# 횟수 3인 경우
# -> 1인 경우 (사칙연산) 2인 경우, 2인 경우 (사칙연산) 1인 경우

N = 5
number = 12


def solution(N, number):
    # 0번째 인덱스는 None으로 설정
    dp = [None] + [{int(str(N)*i)} for i in range(1, 9)]  # 이미 중괄호로 set 선언

    for i in range(1, 9):
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2:
                        dp[i].add(num1 / num2)
        if number in dp[i]:
            return i
    return -1


print(solution(N, number))
