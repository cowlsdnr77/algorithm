import sys

n = int(sys.stdin.readline())

is_used1 = [False] * n  # 열 비교(y 좌표)
is_used2 = [False] * (2*n-1)  # 좌측 하단->우측 상단 대각선
is_used3 = [False] * (2*n-1)  # 좌측 상단->우측 하단 대각선

cnt = 0


# cur는 x좌표
def search(cur):
    global cnt
    if cur == n:
        cnt += 1
        return

    for i in range(n):  # 0부터 n-1까지 y좌표를 움직임
        if not(is_used1[i] or is_used2[cur+i] or is_used3[cur-i+n-1]):  # 셋 다 false 라면
            is_used1[i] = True
            is_used2[cur+i] = True
            is_used3[cur-i+n-1] = True
            search(cur+1)
            is_used1[i] = False
            is_used2[cur+i] = False
            is_used3[cur-i+n-1] = False


search(0)
print(cnt)
