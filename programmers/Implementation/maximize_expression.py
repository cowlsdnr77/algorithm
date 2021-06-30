from itertools import permutations

expression = "50*6-3"


# 리스트에 숫자, 수식으로 저장
# 가능한 수식 우선순위 -> permutation 사용
# 모든 경우에 대해 계산
# 계산 후 절대값화
# 가장 큰 수 찾기


def solution(expression):
    answer = 0
    total_list = []
    stack = []
    sum_list = []
    exp_list = set()

    num = ""

    for i in range(len(expression)):
        if expression[i] == "*" or expression[i] == "-" or expression[i] == "+":
            total_list.append(num)
            exp_list.add(expression[i])
            num = ""
            total_list.append(expression[i])
        else:
            num += expression[i]
            if i == len(expression)-1:
                total_list.append(num)

    print(total_list)  # ['50', '*', '6', '-', '3', '*', '2']
    print(exp_list)  # {'*', '-'}

    for permute in permutations(list(exp_list), len(exp_list)):
        for exp in permute:
            for i in range(0, len(total_list)):
                if i == 0:
                    stack.append(total_list[i])
                    continue
                if stack[-1] == exp:
                    recent_sik = stack.pop()
                    prev_num = stack.pop()
                    print("temp: ", prev_num + recent_sik + total_list[i])
                    temp = eval(prev_num + recent_sik + total_list[i])
                    stack.append(temp)
                else:
                    stack.append(total_list[i])
        print("stack: ", stack)


solution(expression)
