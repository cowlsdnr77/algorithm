import sys

t = int(sys.stdin.readline())

result_li = []

for i in range(t):
    sentence = sys.stdin.readline().rstrip()
    stack = []

    for j in range(len(sentence)):
        if sentence[j] == "(":
            stack.append(sentence[j])
        else:  # ')'
            # stack이 비어있지 않고 stack 맨 위 값이 '(' 라면 pop
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(sentence[j])

    if len(stack) == 0:
        result_li.append("YES")
    else:
        result_li.append("NO")

for i in result_li:
    print(i)
