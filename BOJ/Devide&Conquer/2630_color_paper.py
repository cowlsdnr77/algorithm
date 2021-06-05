# https://kils-log-of-develop.tistory.com/389 참조

import sys

n = int(sys.stdin.readline())
color_list = []  # 이차원 배열

for i in range(n):  # 입력을 이차원 배열로
    color_list.append(list(map(int, sys.stdin.readline().split(" "))))

white = 0  # 흰색 카운트
blue = 0  # 파란색 카운트


def divide_conquer(x_start, y_start, x_end, y_end):  # start는 (0,0), end는 (n,n)
    global white
    global blue
    color = color_list[x_start][y_start]  # 0 은 흰색, 1은 파란색 (현재 시작 위치의 색을 나타냄)
    compare = color  # 0 은 흰색, 1은 파란색, 2는 색 일치하지 않음을 나타냄
    for i in range(x_start, x_end):  # 쪼개질 수 없어질때는 이 for문이 실행되지 않음
        for j in range(y_start, y_end):
            if color_list[i][j] != color:  # 색이 다른게 나오면
                compare = 2  # compare을 2로 만들어 나눔
                break
    if compare == 2:
        divide_conquer(x_start, y_start,
                       (x_start+x_end)//2, (y_start+y_end)//2)  # 왼쪽 위 (2 사분면)

        divide_conquer((x_start+x_end)//2, y_start,
                       x_end, (y_start+y_end)//2)  # 오른쪽 위 (1 사분면)

        divide_conquer(x_start, (y_start+y_end)//2,
                       (x_start+x_end)//2, y_end)  # 왼쪽 아래 (3 사분면)

        divide_conquer((x_start+x_end)//2, (y_start+y_end)//2,
                       x_end, y_end)  # 오른쪽 아래 (4 사분면)
    elif compare == 0:
        white += 1
    elif compare == 1:
        blue += 1
    return


divide_conquer(0, 0, n, n)
print(white)
print(blue)
