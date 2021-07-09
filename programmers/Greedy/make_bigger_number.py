from collections import Counter

# 제한사항
# number은 1자리 이상 1,000,000자리 이하인 숫자
# k는 1 이상 number의 자릿수 미만의 자연수

# PS
# 못풀었다..
# Stack를 생각 못함..

number = "4177252841"
k = 4  # 제거할 수의 개수 k


def solution(number, k):
    stack = []
    for i in number:
        # i와 stack.peek()와 비교해서 i보다 작으면 다 pop하고 k-=1
        while stack and stack[-1] < i and k > 0:
            k -= 1
            stack.pop()
            print(stack)
        stack.append(i)
        print(stack)
    # 만일 충분히 제거하지 못했으면 남은 부분은 뒤에서부터 단순하게 삭제
    return "".join(stack[:len(stack)-k])
    # 이렇게 해도 되는 이유는 이미 큰 수부터 앞에서 채워넣었기 때문


print(solution(number, k))
