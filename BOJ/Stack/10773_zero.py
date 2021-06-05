import sys

k = int(sys.stdin.readline())

stack = []
sum = 0

for i in range(k):
    num = int(sys.stdin.readline())

    if num == 0:  # 0이면 pop
        stack.pop()

    else:  # 0이 아니면 스택에 push
        stack.append(num)


for i in range(len(stack)):
    sum += stack[i]

print(sum)
