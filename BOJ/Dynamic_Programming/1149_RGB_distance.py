# 못풀고 풀이 봄
import sys

N = int(sys.stdin.readline())

result = [[0, 0, 0] for _ in range(N)]  # i 번째로 r,g,b 를 선택했을때 최소값들을 리스트로 저장
r_list = [0 for _ in range(N)]  # r 값들을 저장하는 리스트
g_list = [0 for _ in range(N)]  # g 값들을 저장하는 리스트
b_list = [0 for _ in range(N)]  # b 값들을 저장하는 리스트

for i in range(N):  # N 번째 집까지 각각 r,g,b 값 저장
    r, g, b = map(int, sys.stdin.readline().split())
    r_list[i] = r
    g_list[i] = g
    b_list[i] = b

for i in range(N):
    if i == 0:
        result[i][0] = r_list[i]
        result[i][1] = g_list[i]
        result[i][2] = b_list[i]
    else:
        # i 번째 집을 r로 선택했을때까지의 최소값 저장 -> i-1번째 집까지의 최소값(i-1번째로 g 나 b 를 선택한 경우 중 작은값) + i번째 r 값
        result[i][0] = min(result[i-1][1], result[i-1][2]) + r_list[i]

        # i 번째 집을 g로 선택했을때까지의 최소값 저장 -> i-1번째 집까지의 최소값(i-1번째로 r 나 b 를 선택한 경우 중 작은값) + i번째 g 값
        result[i][1] = min(result[i-1][0], result[i-1][2]) + g_list[i]

        # i 번째 집을 b로 선택했을때까지의 최소값 저장 -> i-1번째 집까지의 최소값(i-1번째로 r 나 g 를 선택한 경우 중 작은값) + i번째 b 값
        result[i][2] = min(result[i-1][0], result[i-1][1]) + b_list[i]

print(min(result[-1]))  # 가장 마지막 리스트의 요소 중 최소값 출력
