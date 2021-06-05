import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

queue = deque()  # 큐
count = 1  # 순서 구하기 위한 카운트, 초기값은 1번째이므로 1
result = []  # 순열 저장
output = ""  # 출력 형태를 만들기 위한 String

for i in range(n):
    queue.append(i+1)

while len(queue) != 0:
    if count == k:  # k번째이면 pop
        result.append(queue.popleft())  # 큐의 맨 앞을 pop
        count = 1  # 카운트 초기화
    else:  # k번째 순번이 나올 때 까지 큐의 맨 앞을 잘라서 맨 뒤로 붙임
        tmp = queue.popleft()
        queue.append(tmp)
        count += 1

for i in result:  # 출력 형태로 만들기 위한 반복문
    if i == result[-1]:
        output += str(i)
    else:
        output += str(i) + ", "

print("<" + output + ">")
