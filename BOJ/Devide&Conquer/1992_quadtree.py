import sys
n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
# result = ""  # 출력 문자열
# 전역변수 사용은 되도록 줄이자
# extend 함수 알아보기


def dq(x, y, n):
    # global result
    check = maps[x][y]  # 0 or 1 (현재 시작 위치의 숫자를 나타냄)

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != maps[i][j]:  # 하나라도 check와 숫자가 다르면 쪼갬
                print("(", end="")  # 새로운 분기 시작
                # result += "("

                dq(x, y, n//2)  # 1사분면 (문제 기준:왼쪽 위)
                dq(x, y+n//2, n//2)  # 2사분면(문제 기준: 오른쪽 위)
                dq(x+n//2, y, n//2)  # 3사분면(문제 기준: 왼쪽 아래)
                dq(x+n//2, y+n//2, n//2)  # 4사분면(문제 기준: 오른쪽 아래)

                print(")", end="")  # 새로운 분기 끝
                # result += (")")
                return

    if check == 1:  # 해당 범위가 모두 1일때
        print("1", end="")
        # result += "1"
        return
    else:  # 해당 범위가 모두 0일때
        print("0", end="")
        # result += "0"
        return


dq(0, 0, n)
