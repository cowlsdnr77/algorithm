import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
result = []

for i in range(n):
    command = sys.stdin.readline().rstrip()

    if command == "pop":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue.popleft())
    elif command == "size":
        result.append(len(queue))
    elif command == "empty":
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)
    elif command == "front":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[0])
    elif command == "back":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[-1])
    else:
        num = command.split(" ")[1]
        queue.append(num)

for i in result:
    print(i)
