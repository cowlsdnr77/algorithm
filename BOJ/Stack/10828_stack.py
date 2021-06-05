import sys

N = int(sys.stdin.readline())
stack = []  # 스택
output_li = []  # 출력값 저장할 리스트

for i in range(N):
    command = sys.stdin.readline().rstrip()

    if command == "pop":
        if len(stack) == 0:
            output_li.append(-1)
        else:
            output_li.append(stack.pop())

    elif command == "size":
        output_li.append(len(stack))

    elif command == "empty":
        if len(stack) == 0:
            output_li.append(1)
        else:
            output_li.append(0)

    elif command == "top":
        if len(stack) == 0:
            output_li.append(-1)
        else:
            output_li.append(stack[-1])

    else:  # push 9
        num = int(command.split(" ")[1])
        stack.append(num)

for i in output_li:
    print(i)
