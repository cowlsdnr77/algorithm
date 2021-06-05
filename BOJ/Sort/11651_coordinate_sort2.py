import sys

n = int(sys.stdin.readline())

dots = []

for i in range(n):
    dots.append(list(map(int, input().split()))) ##(x,y)의 형태로 저장

dots = sorted(dots, key=lambda x : (x[1], x[0])) #람다식 => x[1](즉 y 값)으로 정렬하고 정령 안되는 경우 x[0](즉 x 값)으로 다시 정렬

for i in dots:
    print(*i)  ##파이썬의 패킹과 언패킹
              ## * => * 없이 출력 시 [1, 2] 와 같은 형식으로 출력됨
