import sys
input = sys.stdin.readline

while True:
    # 기본적으로 readline()은 개행문자를 포함하고 있기 때문에 문자열 마지막 개항문자(즉, 공백) 없이 출력하기 위해 rstrip()함수 사용
    sentence = input().rstrip()
    balance_list = []  # "[" 과 "(" 을 담을 stack

    if sentence == ".":  # 입력 종료 조건
        break

    for i in range(len(sentence)):  # 문장을 돌면서 괄호를 찾기 위한 반복문
        if sentence[i] == "[" or sentence[i] == "(":  # 여는 괄호 인 경우 stack에 push
            balance_list.append(sentence[i])

        # 닫는 괄호는 stack에 push되거나 pop 되는 게 아님
        elif sentence[i] == "]":  # 닫는 괄호 "]" 인 경우
            # stack이 비어있지 않고 stack.peek()가 "[" 이라면 stack.pop()
            if balance_list[-1] == "[":
                balance_list.pop()
            else:  # 아니면 "균형이 맞지 않는 문장"이므로 break
                balance_list.append(sentence[i])
                break

        elif sentence[i] == ")":  # 닫는 괄호 ")" 인 경우
            # stack이 비어있지 않고 stack.peek()가 "(" 이라면 stack.pop()
            if balance_list[-1] == "(":
                balance_list.pop()
            else:  # 아니면 "균형이 맞지 않는 문장"이므로 break
                balance_list.append(sentence[i])
                break

    if not balance_list:  # 리스트에 값이 들어있지 않으면 성공
        print("yes")
    else:
        print("no")
