import sys


def sugar(x, y):
    result = 0  # x+y 봉투 개수
    for i in range(0, x+1):
        for j in range(0, y+1):
            if 3*i + 5*j == N:
                tmp = i+j
                if result == 0:  # result가 0일때 (가장 먼저 조건을 만족하는 경우)
                    result = tmp
                result = min(result, tmp)
    # 모든 경우의 수를 다 돌아도 result 가 초기 값(0)과 같다면 만족하는 x,y가 없는 경우 이므로 return -1
    if result == 0:
        return -1

    return result


N = int(sys.stdin.readline())

x = N // 3  # 3킬로 봉투 최대 가능 개수
y = N // 5  # 5킬로 봉투 최대 가능 개수

print(sugar(x, y))
