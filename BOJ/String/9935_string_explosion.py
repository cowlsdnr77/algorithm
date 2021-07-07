import sys

# 네이버 웹툰 개발 챌린지 코테 3번 문제와 매우 흡사함
# 가장 중요 포인트는 제한사항을 잘 보고 시간 복잡도를 대략적으로 계산한 뒤에 문제를 풀어야된다

# 코딩테스트에서 자료구조 하나 안쓰고 풀리는 문제는 없다!


s = sys.stdin.readline().rstrip()  # 1,000,000 보다 작거나 같다
t = sys.stdin.readline().rstrip()  # 36보다 작거나 같다


def solution(s, t):  # 이렇게 모두 찾아서 바꾸는 식으로 하면 시간 복잡도가 O(N^2M)이 나와 시간초과
    while t in s:
        s = s.replace(t, "")
    if len(s) == 0:
        return "FRULA"
    else:
        return s


def solution2(s, t):
    stack = []

    for i in s:
        stack.append(i)
        if stack[-1] == t[-1]:
            compare = "".join(stack[-len(t):])  # 뒤에서부터 len(t)번째 부터 맨 끝까지
            print("compare: ", compare)
            if compare == t:
                del stack[-len(t):]  # 이게 훨씬 빠르게 동작함
                # for _ in range(len(t)):
                #     stack.pop()

    return "".join(stack) if len(stack) > 0 else "FRULA"


print(solution2(s, t))
