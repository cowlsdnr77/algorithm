# https://developmentdiary.tistory.com/334 참조
# https://joosjuliet.github.io/2667/ -> bfs 참조
import sys
n = int(sys.stdin.readline())

color_paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white = 0  # 흰색 카운트
blue = 0  # 파란색 카운트


def dq(x, y, n):  # 시작점 (x,y)
    global white, blue
    check = color_paper[x][y]  # 0 은 흰색, 1은 파란색 (현재 시작 위치의 색을 나타냄)

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != color_paper[i][j]:  # 하나라도 check와 색이 다르면 쪼갬
                dq(x, y, n//2)  # 1사분면 (문제 기준:왼쪽 위)
                dq(x, y+n//2, n//2)  # 2사분면(문제 기준: 오른쪽 위)
                dq(x+n//2, y, n//2)  # 3사분면(문제 기준: 왼쪽 아래)
                dq(x+n//2, y+n//2, n//2)  # 4사분면(문제 기준: 오른쪽 아래)
                return

    if check == 0:  # 모두 흰색 일 때
        white += 1
        return
    else:  # 모두 파란색 일 때
        blue += 1
        return


dq(0, 0, n)
print(white)
print(blue)
